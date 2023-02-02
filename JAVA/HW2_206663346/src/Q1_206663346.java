import java.util.Scanner;

public class Q1_206663346 {

	public static boolean isPrime(int number) {
        int sqrt = (int) Math.sqrt(number) + 1;
        for (int i = 2; i < sqrt; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
	
	public static void PrintAsteriskLine(int Length){
		for (int i = 0; i<Length; i++) {
			System.out.print("*");
		}
	}
	
	public static void PrintAsteriskPyramid(int numline) {
		int lastprime =1;
		for(int i = 0; i<numline;i++) {
			for (int j = lastprime + 1; j < 20;j++) {
				if (isPrime(j)) {
					PrintAsteriskLine(j);
					lastprime = j;
					System.out.println();
					break;
				}
			}
		}
	}
	
	public static Scanner sc = new Scanner(System.in);
	
	
	public static void main(String[] args) {
		System.out.println("Please enter an integer n,   0<n<20 :");
		int num =sc.nextInt();
		int counter = 1;
		while (!((num>0) && (num<20)) && (counter<3)) {
			System.out.println("Error! Try  again:");
			num = sc.nextInt();
			counter++;
		}
		if(!((num>0) && (num<20))) {
			System.out.println("Three mistakes! Bye!");
			System.exit(0);
		}
		
		PrintAsteriskPyramid(num);
		
	}


}
