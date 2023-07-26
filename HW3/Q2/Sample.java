public class NestedLoops {
    public static void printCombinations() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 5; k++) {
                    System.out.printf("i=%d, j=%d, k=%d\n", i, j, k);
                }
            }
        }
        for (int i = 0; i < 3; i++) {
            System.out.printf("i=%d, j=%d, k=%d\n", i, j, k);
        }
    }
}
