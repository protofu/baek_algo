class Solution {
    public int[] solution(int[] emergency) {
        int len = emergency.length;
        // 순서 배열
        int[] answer = new int[len];
        // 원래 값 배열
        int[] before = new int[len];

        // 원래값 채워넣기
        for (int i = 0; i<len;i++){
            before[i] = emergency[i];
        }
        
        // 내림차순 정렬 
        for (int i = 0;i<len-1;i++){
            for (int j = i+1;j<len;j++){
                if (emergency[i] < emergency[j]){
                    int tmp = emergency[i];
                    emergency[i] = emergency[j];
                    emergency[j] = tmp;
                }
            }
        }

        // 원래값을 탐색하며 등수 집어넣기 (등수 = 내림차순 배열의 인덱스+1)
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
