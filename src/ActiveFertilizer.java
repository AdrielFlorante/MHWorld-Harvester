public class ActiveFertilizer {
    public final Fertilizer fertilizer;
    public int remainingDuration;

    public ActiveFertilizer(Fertilizer fertilizer, int remainingDuration) {
        this.fertilizer = fertilizer;
        this.remainingDuration = remainingDuration;
    }

    public ActiveFertilizer copy() {
        return new ActiveFertilizer(fertilizer, remainingDuration);
    }

    @Override
    public String toString() {
        return fertilizer.name + " (" + remainingDuration + ")";
    }
}
