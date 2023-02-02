
public class binaryrecursive {
	public static String Add(String str, int n) {
		str = str + n;
		return str;
	}
	public static boolean p1(int n, String str) {
		if (n==1) {
			System.out.println(str);
			return true;
		}
		return p1(n-1,Add(str,1)) && p1(n-1,Add(str,0));
	}
	public static void main(String[] args) {
		p1(6,"1");
	}

}
