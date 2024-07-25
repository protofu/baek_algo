import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int cnt = 0, tmp = -1;
        // 연속되지 않은 숫자 갯수 구하기
        for(int a : arr){
            if (tmp != a) {
                cnt++;
                tmp = a;
            }
        }
        // 구한 길이로 배열 만들어주고
        int[] answer = new int[cnt];
        tmp = -1;
        cnt = 0;
        // 같은 조건문으로 이제 answer에 넣어주기
        for(int a : arr){
            if (tmp != a) {
                answer[cnt] = a;
                cnt++;
                tmp = a;
            }
        }

        return answer;
    }
}