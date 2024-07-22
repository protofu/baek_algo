class Solution {
    public int[] solution(int[] emergency) {
        int len = emergency.length;
        int[] answer = new int[len];
        int[] before = new int[len];
        
        for (int i = 0; i<len;i++){
            before[i] = emergency[i];
        }
        
        for (int i = 0;i<len-1;i++){
            for (int j = i+1;j<len;j++){
                if (emergency[i] < emergency[j]){
                    int tmp = emergency[i];
                    emergency[i] = emergency[j];
                    emergency[j] = tmp;
                }
            }
        }
        for(int i=0;i<len;i++){
            for(int j = 0;j<len; j++){
                if (emergency[i] == before[j]){
                    answer[j] = i+1;
                }
            }
        }
        return answer;
    }
}