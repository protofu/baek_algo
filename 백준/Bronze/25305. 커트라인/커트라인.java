import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();
        // 받고 
        String[] arr = sc.nextLine().split(" ");
        // int 배열 생성
        int[] scores = new int[arr.length];
        // int로 넣고
        for (int i = 0; i < arr.length; i++) {
        	scores[i] = Integer.parseInt(arr[i]);
        }
        // 내림차순
        for (int i = 0; i < scores.length-1; i++) {
        	for (int j = 1; j < scores.length; j++) {
        		if (scores[j] > scores[j-1]) {
        			int tmp = scores[j];
        			scores[j] = scores[j-1];
        			scores[j-1] = tmp;
        		}				
			}
		}
        System.out.println(scores[k-1]);
        sc.close();
    }
}
