import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Read input
        Scanner sc = new Scanner(System.in);
        int r_1 = sc.nextInt();
        int r_2 = sc.nextInt();

        // Calculate result
        int result = cube(r_1) - cube(r_2);
        System.out.println(result);
    }

    public static int cube(int a) {
        // Returns cube (a^3) of integer value
        return (a * a * a);
    }
}
