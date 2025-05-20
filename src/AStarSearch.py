import heapq
from dataclasses import dataclass, field
from typing import List, Set, Tuple


@dataclass
class Fertilizer:
    name: str
    duration: int
    cost: int
    effect: str

    def affects_type(self, crop_type: str) -> bool:
        if self.effect == "BoostPlant" and crop_type == "Plant":
            return True
        if self.effect == "BoostInsect" and crop_type == "Insect":
            return True
        if self.effect == "BoostMushroom" and crop_type == "Mushroom":
            return True
        return False


@dataclass
class Crop:
    name: str
    baseYield: int
    baseGrowthTime: int
    type: str
    currentGrowth: int = 0
    yield_: int = 0

    def copy(self):
        return Crop(self.name, self.baseYield, self.baseGrowthTime, self.type, self.currentGrowth, self.yield_)


@dataclass
class ActiveFertilizer:
    fertilizer: Fertilizer
    remainingDuration: int

    def copy(self):
        return ActiveFertilizer(self.fertilizer, self.remainingDuration)


@dataclass(order=True)
class Node:
    fCost: int
    crops: List[Crop] = field(compare=False)
    plan: List[Fertilizer] = field(compare=False)
    totalCost: int = field(compare=False)
    activeFertilizers: List[ActiveFertilizer] = field(compare=False)


@dataclass
class Result:
    plan: List[Fertilizer]
    finalCrops: List[Crop]
    totalCost: int


class AStarSearch:

    @staticmethod
    def search(initialCrops: List[Crop], fertilizers: List[Fertilizer], maxCycles: int) -> Result:
        openSet: List[Node] = []
        visited: Set[str] = set()

        start = Node(
            fCost=0,
            crops=AStarSearch.copyCrops(initialCrops),
            plan=[],
            totalCost=0,
            activeFertilizers=[]
        )
        heapq.heappush(openSet, start)

        best = None

        while openSet:
            current = heapq.heappop(openSet)
            stateKey = AStarSearch.generateStateKey(current.crops, current.activeFertilizers)

            if stateKey in visited:
                continue
            visited.add(stateKey)

            if len(current.plan) == maxCycles:
                if best is None or AStarSearch.totalYield(current.crops) > AStarSearch.totalYield(best.crops):
                    best = current
                continue

            for fert in fertilizers:
                nextActive = AStarSearch.copyActiveFerts(current.activeFertilizers)

                alreadyActive = any(
                    a.fertilizer.name == fert.name and a.remainingDuration > 0
                    for a in nextActive
                )
                if fert.name != "None" and alreadyActive:
                    continue

                nextCrops = AStarSearch.copyCrops(current.crops)

                if fert.name != "None":
                    AStarSearch.applyFertilizer(nextCrops, fert, nextActive)

                AStarSearch.simulateCycle(nextCrops, nextActive)

                nextPlan = current.plan + [fert]
                cost = current.totalCost + (0 if fert.name == "None" else fert.cost)

                yieldScore = AStarSearch.totalYield(nextCrops)
                affectedTypes = len({
                    c.type for c in nextCrops if fert.affects_type(c.type)
                })

                heuristic = -(yieldScore + (affectedTypes ** 2) * 1000)
                fCost = cost + heuristic

                heapq.heappush(openSet, Node(fCost, nextCrops, nextPlan, cost, nextActive))

        return Result(best.plan, best.crops, best.totalCost) if best else None

    @staticmethod
    def applyFertilizer(crops: List[Crop], fert: Fertilizer, active: List[ActiveFertilizer]):
        af = ActiveFertilizer(fert, fert.duration)
        active.append(af)

        if fert.effect == "Soft Soil":
            for a in active:
                if a != af:
                    a.remainingDuration += 5

    @staticmethod
    def simulateCycle(crops: List[Crop], activeFerts: List[ActiveFertilizer]):
        for crop in crops:
            growthTime = crop.baseGrowthTime
            yieldBonus = 0

            for af in activeFerts:
                if af.remainingDuration <= 0:
                    continue

                effect = af.fertilizer.effect
                if effect == "Catalyst":
                    growthTime = max(1, growthTime - 1)
                if effect == "AncientCatalyst":
                    growthTime = 1
                if effect == "BoostPlant" and crop.type == "Plant":
                    yieldBonus += crop.baseYield // 2
                if effect == "BoostInsect" and crop.type == "Insect":
                    yieldBonus += crop.baseYield // 2
                if effect == "BoostMushroom" and crop.type == "Mushroom":
                    yieldBonus += crop.baseYield // 2

            crop.currentGrowth += 1
            if crop.currentGrowth >= growthTime:
                crop.yield_ += crop.baseYield + yieldBonus
                crop.currentGrowth = 0

        # activeFerts[:] = [f for f in activeFerts if (f.remainingDuration := f.remainingDuration - 1) > 0]
        new_active_ferts = []
        for f in activeFerts:
            f.remainingDuration -= 1
            if f.remainingDuration > 0:
                new_active_ferts.append(f)
        activeFerts[:] = new_active_ferts

    @staticmethod
    def copyCrops(crops: List[Crop]) -> List[Crop]:
        return [c.copy() for c in crops]

    @staticmethod
    def copyActiveFerts(activeFerts: List[ActiveFertilizer]) -> List[ActiveFertilizer]:
        return [a.copy() for a in activeFerts]

    @staticmethod
    def totalYield(crops: List[Crop]) -> int:
        return sum(c.yield_ for c in crops)

    @staticmethod
    def generateStateKey(crops: List[Crop], activeFerts: List[ActiveFertilizer]) -> str:
        crop_key = ';'.join(f"{c.name}:{c.currentGrowth}:{c.yield_}" for c in crops)
        fert_key = ';'.join(f"{af.fertilizer.name}:{af.remainingDuration}" for af in activeFerts)
        return crop_key + '|' + fert_key
