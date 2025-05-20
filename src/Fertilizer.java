public class Fertilizer {
    public final String name;
    public final int duration;
    public final int cost;
    public final String effect;

    public Fertilizer(String name, int duration, int cost, String effect) {
        this.name = name;
        this.duration = duration;
        this.cost = cost;
        this.effect = effect;
    }

    public boolean affectsType(String cropType) {
        switch (effect) {
            case "BoostPlant": return cropType.equals("Plant");
            case "BoostMushroom": return cropType.equals("Mushroom");
            case "BoostInsect": return cropType.equals("Insect");
            default: return false;  // Catalyst etc.
        }
    }

    @Override
    public String toString() {
        return name;
    }
}
