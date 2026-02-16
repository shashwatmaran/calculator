public class Hello {

    public static void main(String[] args) {

        System.out.println("=== Jenkins Java Demo ===");

        // If user passed a name
        if (args.length > 0) {
            System.out.println("Hello, " + args[0] + "!");
        } 
        else {
            System.out.println("Hello, World!");
        }

        // Show Java runtime info (useful in CI debugging)
        System.out.println("\nRunning on:");
        System.out.println("Java Version: " + System.getProperty("java.version"));
        System.out.println("OS: " + System.getProperty("os.name"));

        System.out.println("\nBuild Successful ✅");
    }
}
