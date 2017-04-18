import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Read Input
        Scanner sc = new Scanner(System.in);

        // Intialize counter variables
        int x = sc.nextInt();
        int y = sc.nextInt();
        int z = sc.nextInt();

        // Empty output
        String[] output = new String[z+1];

        // Iterate from low to high (Z-axis)
        for (int m = 0; m < z; m++) {
            char[] out_line = new char[y]; // create empty line
            for (int p = 0; p < y; p++) {
                out_line[p] = '.';
            }

            // Throw away division line --
            sc.nextLine();

            // Iterate from back to front (X-axis)
            for (int n = 0; n < x ; n++) {

                String s = sc.nextLine();
                for (int o = 0; o < s.length(); o++) {
                    if (s.charAt(o) == '#') {
                        out_line[o] = '#';
                    }
                }

            }

            // Add finished line to output (we want reverse)
            String lineup = new String(out_line);
            // output = lineup + "\n" + output;
            output[m] = lineup;
        }

        // Print output
        for (int ln = 0; ln < z; ln++) {
            System.out.println(output[z-1-ln]);
        }
    }
}
