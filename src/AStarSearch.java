import java.util.*;

public class AStarSearch {

    public static Result search(List<Crop> initialCrops, List<Fertilizer> fertilizers, int maxCycles) {
        PriorityQueue<Node> openSet = new PriorityQueue<>(Comparator.comparingInt(n -> n.fCost));
        Set<String> visited = new HashSet<>();

        List<ActiveFertilizer> activeFerts = new ArrayList<>();
        Node start = new Node(copyCrops(initialCrops), new ArrayList<>(), 0, 0, activeFerts);
        openSet.add(start);

        Node best = null;

        while (!openSet.isEmpty()) {
            Node current = openSet.poll();

            String stateKey = generateStateKey(current.crops, current.activeFertilizers);
            if (visited.contains(stateKey)) continue;
            visited.add(stateKey);

            if (current.plan.size() == maxCycles) {
                if (best == null || totalYield(current.crops) > totalYield(best.crops)) {
                    best = current;
                }
                continue;
            }

            for (Fertilizer fert : fertilizers) {
                List<Crop> nextCrops = copyCrops(current.crops);
                List<ActiveFertilizer> nextActive = copyActiveFerts(current.activeFertilizers);

                if (!fert.name.equals("None")) {
                    applyFertilizer(nextCrops, fert, nextActive);
                }

                simulateCycle(nextCrops, nextActive);
                List<Fertilizer> nextPlan = new ArrayList<>(current.plan);
                nextPlan.add(fert);

                int cost = current.totalCost + (fert.name.equals("None") ? 0 : fert.cost); // Increase cost only if fertilizer is not "None"

                // Estimate heuristics
                int yieldScore = totalYield(nextCrops);
                int affectedTypes = (int) nextCrops.stream()
                        .map(c -> c.type)
                        .filter(type -> fert.affectsType(type))
                        .distinct()
                        .count();

                // int heuristic = -(yieldScore * 1000 + affectedTypes * 900); // small bonus for diversity
                // int heuristic = -(yieldScore * affectedTypes * 1000); // multiply bonus for diversity
                int heuristic = -(yieldScore * 1000 + (int)Math.pow(affectedTypes, 2) * 1500); // exponentially increase bonus for diversity

                int fCost = cost + heuristic;

                openSet.add(new Node(nextCrops, nextPlan, cost, fCost, nextActive));
            }
        }

        return best == null ? null : new Result(best.plan, best.crops, best.totalCost);
    }

    private static void applyFertilizer(List<Crop> crops, Fertilizer fert, List<ActiveFertilizer> active) {
        ActiveFertilizer af = new ActiveFertilizer(fert, fert.duration);
        active.add(af);

        if (fert.effect.equals("Soft Soil")) {
            for (ActiveFertilizer a : active) {
                if (a != af) {
                    a.remainingDuration += 5;
                }
            }
        }
    }

    private static void simulateCycle(List<Crop> crops, List<ActiveFertilizer> activeFerts) {
        for (Crop crop : crops) {
            int growthTime = crop.baseGrowthTime;
            int yieldBonus = 0;

            for (ActiveFertilizer af : activeFerts) {
                if (af.remainingDuration <= 0) continue;

                String effect = af.fertilizer.effect;

                if (effect.equals("Catalyst")) {
                    growthTime = Math.max(1, growthTime - 1); // To avoid growthTime being zero or negative
                }
                if (effect.equals("AncientCatalyst")) {
                    growthTime = 1;
                }
                if (effect.equals("BoostPlant") && crop.type.equals("Plant")) {
                    yieldBonus += crop.baseYield + (crop.baseYield / 2);
                }
                if (effect.equals("BoostInsect") && crop.type.equals("Insect")) {
                    yieldBonus += crop.baseYield + (crop.baseYield / 2);
                }
                if (effect.equals("BoostMushroom") && crop.type.equals("Mushroom")) {
                    yieldBonus += crop.baseYield + (crop.baseYield / 2);
                }
            }

            crop.currentGrowth++;
            if (crop.currentGrowth >= growthTime) {
                crop.yield += crop.baseYield + yieldBonus;
                crop.currentGrowth = 0;
            }
        }

        // Decrement durations
        activeFerts.removeIf(f -> --f.remainingDuration <= 0);
    }

    private static List<Crop> copyCrops(List<Crop> crops) {
        List<Crop> copy = new ArrayList<>();
        for (Crop c : crops) {
            copy.add(c.copy());
        }
        return copy;
    }

    private static List<ActiveFertilizer> copyActiveFerts(List<ActiveFertilizer> list) {
        List<ActiveFertilizer> copy = new ArrayList<>();
        for (ActiveFertilizer f : list) {
            copy.add(f.copy());
        }
        return copy;
    }

    private static int totalYield(List<Crop> crops) {
        return crops.stream().mapToInt(c -> c.yield).sum();
    }

    private static String generateStateKey(List<Crop> crops, List<ActiveFertilizer> activeFerts) {
        StringBuilder sb = new StringBuilder();
        for (Crop c : crops) {
            sb.append(c.name).append(":").append(c.currentGrowth).append(":").append(c.yield).append(";");
        }
        for (ActiveFertilizer af : activeFerts) {
            sb.append(af.fertilizer.name).append(":").append(af.remainingDuration).append(";");
        }
        return sb.toString();
    }

    public static class Result {
        public final List<Fertilizer> plan;
        public final List<Crop> finalCrops;
        public final int totalCost;

        public Result(List<Fertilizer> plan, List<Crop> finalCrops, int totalCost) {
            this.plan = plan;
            this.finalCrops = finalCrops;
            this.totalCost = totalCost;
        }
    }

    private static class Node {
        public final List<Crop> crops;
        public final List<Fertilizer> plan;
        public final int totalCost;
        public final int fCost;
        public final List<ActiveFertilizer> activeFertilizers;

        public Node(List<Crop> crops, List<Fertilizer> plan, int totalCost, int fCost, List<ActiveFertilizer> activeFertilizers) {
            this.crops = crops;
            this.plan = plan;
            this.totalCost = totalCost;
            this.fCost = fCost;
            this.activeFertilizers = activeFertilizers;
        }
    }
}
