import java.util.*;

public class c037 {
    public static void main(String[] args) {
        // Read standard input
        Scanner sc = new Scanner(System.in);
        String[] dates = sc.next().split("/");
        String[] times = sc.next().split(":");

        // Process
        int day = Integer.parseInt(dates[1]);
        int hours = Integer.parseInt(times[0]);

        // Convert overlapping hours to days and adjust output.
        if (hours >= 24) {
            day += hours / 24;
            hours = hours % 24;
        }

        // Create output string
        String output = dates[0] + "/" + String.format("%02d", day) + " " + String.format("%02d", hours) + ":" + times[1];

        // Output solution
        System.out.println(output);

    }
}
