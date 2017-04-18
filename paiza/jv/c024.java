import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Read Input
        Scanner sc = new Scanner(System.in);

        // initialize mini computer values
        HashMap vals = new HashMap(2);
        vals.put(1, 0);
        vals.put(2, 0);

        // Set number of inputs
        int numCommands = sc.nextInt();

        // Parse input
        for (int i = 0; i < numCommands; i++) {
            String cmd = sc.next();
            int cmd_bit;
            int cmd_mod;

            if (cmd.equals("SET")) {
                    cmd_bit = Integer.parseInt(sc.next());
                    cmd_mod = Integer.parseInt(sc.next());
                    vals.put(cmd_bit, cmd_mod);
            } else if (cmd.equals("ADD")) {
                    cmd_mod = Integer.parseInt(sc.next());
                    vals.put(2, (Integer)vals.get(1) + cmd_mod);

            } else if (cmd.equals("SUB")) {
                    cmd_mod = Integer.parseInt(sc.next());
                    vals.put(2, (Integer)vals.get(1) - cmd_mod);
            }
        }

        // Output result
        System.out.println(vals.get(1) + " " + vals.get(2));



        // Output
        // System.out.println(inp_line);
    }
}
