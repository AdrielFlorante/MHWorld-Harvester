import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Crop> crops = Arrays.asList( // You may only plant three crops at a time
                new Crop("Herb", 1, 2, "Plant"),
                // new Crop("Honey", 1, 2, "Insect"),
                new Crop("Godbug", 3, 8, "Insect"),
                // new Crop("Blue Mushroom", 2, 1, "Mushroom")
                new Crop("Mandragora", 3, 4, "Mushroom")
        );

        List<Fertilizer> fertilizers = Arrays.asList(
                new Fertilizer("Soft Soil", 5, 300, "SoftSoil"),
                new Fertilizer("Catalyst", 4, 150, "Catalyst"),
                new Fertilizer("Ancient Catalyst", 4, 250, "AncientCatalyst"),
                new Fertilizer("Plant Fertilizer", 3, 50, "BoostPlant"),
                new Fertilizer("Mushroom Substrate", 3, 50, "BoostMushroom"),
                new Fertilizer("Summoner Jelly", 3, 50, "BoostInsect"),
                new Fertilizer("None", 0, 0, "None") // We are allowed to wait out a cycle if it means saving costs
        );

        int maxCycles = 20
                ;

        System.out.println("\nOptimal Fertilizer Plan over " + maxCycles + " cycles:");

        AStarSearch.Result result = AStarSearch.search(crops, fertilizers, maxCycles);

        int cycle = 1;
        for (Fertilizer fert : result.plan) {
            System.out.printf("Cycle %2d: %s\n", cycle++, fert == null ? "No Fertilizer" : fert.name);
        }

        System.out.println("\nFinal Yields:");
        int totalYield = 0;
        for (Crop crop : result.finalCrops) {
            System.out.println("- " + crop.name + ": " + crop.yield);
            totalYield += crop.yield;
        }

        System.out.println("\nTotal Yield: " + totalYield);
        System.out.println("Total Cost: " + result.totalCost);
        // System.out.printf("Cost per Unit yielded: %.2f\n", result.totalCost / (double) Math.max(1, totalYield));
    }
}
