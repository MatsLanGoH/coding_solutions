import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Read standard input
        Scanner sc = new Scanner(System.in);
        int noThrows = sc.nextInt();

        int noBalls = 0;
        int noStrikes = 0;

        for (int i = 0; i < noThrows; i++) {
            String play = sc.next();

            // count plays
            if (play.equals("ball")) {
                noBalls++;
                if (noBalls > 3) {
                    play = "fourball";
                }

            } else if (play.equals("strike")) {
                noStrikes++;
                if (noStrikes > 2) {
                    play = "out";
                }
            }

            // count
            System.out.println(play += "!");
        }

    }

    }
}
