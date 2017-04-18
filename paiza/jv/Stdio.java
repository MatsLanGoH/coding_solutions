import java.util.*;

public class Stdio {

  public static void main(String[] args) {

    System.out.println("Input three numbers, each followed by ENTER:");

    Scanner scan = new Scanner(System.in);
    int a = scan.nextInt();
    int b = scan.nextInt();
    int c = scan.nextInt();
    System.out.println();
    System.out.println(a);
    System.out.println(b);
    System.out.println(c);

  }
}
