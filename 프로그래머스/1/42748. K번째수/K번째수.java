import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0;i<commands.length;i++){
            int cnt = 0;
            int[] tmp = new int[commands[i][1] - commands[i][0]+1];
            for(int j=commands[i][0]-1;j<commands[i][1];j++) {
                tmp[cnt] = array[j];
                cnt++;
            }
            cnt = 0;
            Arrays.sort(tmp);           
            answer[i] = tmp[commands[i][2]-1];
        }
        
        return answer;
    }
}