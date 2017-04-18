import java.util.*;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int line;
        for(; sc.hasNext(); ) {
            line = sc.nextInt();
            System.out.println(countConsecMultiples(line));
        }
    }

    public static int countConsecMultiples(int num) {
        if (num % 2 == 0) {
            return 0;
        }
        else {
            int m = 1999999 / num;
            int n = (int)(m / 2.0 + 0.5);
            return n;
        }
    }
}
