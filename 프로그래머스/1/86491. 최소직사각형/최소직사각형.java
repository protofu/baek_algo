class Solution {
    public int solution(int[][] sizes) {
        int big = 0, small = 0;
        // 배열 돌면서
        for(int[] size : sizes) {
            // 가로가 길다면
            if (size[0] > size[1]) {
                // big을 가장 긴걸로 초기화(가로)
                if (big < size[0]) big = size[0];
                // small을 가장 긴걸로 초기화(세로)
                if (small < size[1]) small = size[1];
            } else {
                // big을 가장 긴걸로 초기화(세로)
                if (big < size[1]) big = size[1];
                // small을 가장 긴걸로 초기화(가로)
                if (small < size[0]) small = size[0];
            }
        }
        return big*small;
    }
}