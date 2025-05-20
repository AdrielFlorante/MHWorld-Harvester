import java.util.*;

public class Crop {
    public final String name;
    public final int baseGrowthTime;
    public final int baseYield;
    public final String type;

    public int currentGrowth = 0;
    public int yield = 0;

    public List<ActiveFertilizer> activeFertilizers = new ArrayList<>();

    public Crop(String name, int baseGrowthTime, int baseYield, String type) {
        this.name = name;
        this.baseGrowthTime = baseGrowthTime;
        this.baseYield = baseYield;
        this.type = type;
    }

    public Crop copy() {
        Crop clone = new Crop(name, baseGrowthTime, baseYield, type);
        clone.currentGrowth = currentGrowth;
        clone.yield = yield;

        // Deep copy active fertilizers
        for (ActiveFertilizer af : activeFertilizers) {
            clone.activeFertilizers.add(af.copy());
        }

        return clone;
    }
}
