import java.util.Scanner;
public class Main{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        double [] store = new double[A];
        store[0] = sc.nextInt();
        double B = store[0];
        for(int i = 1; i<A;i++) {
        	store[i] = sc.nextInt();
        	B = Math.max(B, store[i]);
        	
        }
        double total=0;
        for(int j=0;j<A;j++) {
        	store[j]=store[j]/B*100;
        	total = total + store[j];
        }
        System.out.println(total/A);
    }
}