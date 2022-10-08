import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A ,B,i,C;
        B =-1;
        i = 0;
        A = sc.nextInt();
        sc.close();
        C = A;
        while(A!=B){
            B  = C % 10 + C / 10;
            C = C% 10 * 10 + B % 10;
        	i +=1;
            B = C;
        }
        System.out.println(i);
    }
}