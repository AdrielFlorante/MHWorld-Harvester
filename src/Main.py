# main.py

from Crop import Crop
from Fertilizer import Fertilizer
from AStarSearch import AStarSearch  # Assuming your A* logic is in astar_search.py

def main():
    # Define the crops (only 3 crops may be planted at a time)
    crops = [
        Crop("Godbug", 3, 8, "Insect"),
        Crop("Might Seed", 2, 4, "Plant"),
        Crop("Devil's Blight", 3, 4, "Mushroom")
    ]

    # Define available fertilizers
    fertilizers = [
        Fertilizer("Soft Soil", 5, 300, "SoftSoil"),
        Fertilizer("Catalyst", 4, 150, "Catalyst"),
        Fertilizer("Ancient Catalyst", 4, 250, "AncientCatalyst"),
        Fertilizer("Plant Fertilizer", 3, 50, "BoostPlant"),
        Fertilizer("Mushroom Substrate", 3, 50, "BoostMushroom"),
        Fertilizer("Summoner Jelly", 3, 50, "BoostInsect"),
        Fertilizer("None", 0, 0, "None")
    ]

    max_cycles = 25

    print(f"\nOptimal Fertilizer Plan over {max_cycles} cycles:")

    result = AStarSearch.search(crops, fertilizers, max_cycles)

    for i, fert in enumerate(result.plan, start=1):
        fert_name = fert.name if fert is not None else "No Fertilizer"
        print(f"Cycle {i:2d}: {fert_name}")

    print("\nFinal Yields:")
    total_yield = 0
    for crop in result.finalCrops:
        print(f"- {crop.name}: {crop.yield_amount}")
        total_yield += crop.yield_amount

    print(f"\nTotal Yield: {total_yield}")
    print(f"Total Cost: {result.total_cost}")
    # print(f"Cost per Unit yielded: {result.total_cost / max(1, total_yield):.2f}")

if __name__ == "__main__":
    main()
