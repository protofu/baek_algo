class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = {};
        int a = slicer[0], b = slicer[1], c = slicer[2];
        
        switch (n) {
            case 1:
                // 0부터 b까지 슬라이싱
                answer = new int[b + 1];
                for (int i = 0; i <= b; i++) {
                    answer[i] = num_list[i];
                }
                break;
            case 2:
                // a부터 끝까지 슬라이싱
                answer = new int[num_list.length - a];
                int idx = 0;
                for (int i = a; i < num_list.length; i++) {
                    answer[idx] = num_list[i];
                    idx++;
                }
                break;
            case 3:
                // a부터 b까지 슬라이싱
                answer = new int[b - a + 1];
                idx = 0;
                for (int i = a; i <= b; i++) {
                    answer[idx] = num_list[i];
                    idx++;
                }
                break;
            case 4:
                // a부터 b까지 c 간격으로 슬라이싱
                int size = (b - a) / c + 1;
                answer = new int[size];
                idx = 0;
                for (int i = a; i <= b; i += c) {
                    answer[idx] = num_list[i];
                    idx++;
                }
                break;
        }
        
        return answer;
    }
}
