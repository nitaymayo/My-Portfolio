import java.util.Scanner;

public class Q2_206663346 {
public static Scanner sc = new Scanner(System.in);
	
	public static int CountOnesInBinary(int num) {
		int count=0;
		   while (num!=0) {
			   if(num%2==1)
				   count++;
			   num = num/2;
		   }
		   return count;
	}
	
	public static void main(String[] args) {
		
		System.out.println("Please enter an integer n, n>0:");
		int num = sc.nextInt();
		
		while (num<0) {
			System.out.println("Error! Try  again:");
			num = sc.nextInt();
		}
		
		System.out.print("Number of ones: "+CountOnesInBinary(num));
	}
	

}
