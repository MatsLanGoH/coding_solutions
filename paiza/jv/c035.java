import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Read Input
        Scanner sc = new Scanner(System.in);

        // Intialize passing grades
        int PASSING_GRADE = 160;
        int PASSING_TOTAL = 350;
        int passed_students = 0;

        // Set number of input lines
        int numStudents = sc.nextInt();

        // Read input
        for (int i = 0; i < numStudents; i++ ) {
            String category = sc.next();
            int eng = sc.nextInt();
            int math = sc.nextInt();
            int phys = sc.nextInt();
            int jap = sc.nextInt();
            int geo = sc.nextInt();
            int total = eng + math + phys + jap + geo;

            // Check student scores for their categories
            if (category.equals("s")) {
                if ((math + phys) >= PASSING_GRADE && total >= PASSING_TOTAL) {
                    passed_students++;
                }
            } else if (category.equals("l")) {
                if ((jap + geo) >= PASSING_GRADE && total >= PASSING_TOTAL) {
                    passed_students++;
                }
            }
        }

        // Output count of passed students
        System.out.println(passed_students);
    }
}
