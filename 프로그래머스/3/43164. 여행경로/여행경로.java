import java.util.*;

class Solution {
    public String[] solution(String[][] tickets) {
        // 경로 딕셔너리로 정리
        // 키 : 출발 || 요소 : 도착
        Map<String, List<String>> routes = new HashMap<>();
        for (String[] ticket : tickets) {
            routes.putIfAbsent(ticket[0], new ArrayList<>());
            routes.get(ticket[0]).add(ticket[1]);
        }

        // 각 출발지에서 도착지 리스트를 사전순으로 정렬
        for (List<String> destList : routes.values()) {
            Collections.sort(destList);
        }

        // 시작을 ICN으로
        Stack<String> stack = new Stack<>();
        List<String> answer = new ArrayList<>();
        stack.push("ICN");

        // stack이 비었단건 다 탐색하고 끝낸 것
        while (!stack.isEmpty()) {
            String top = stack.peek();
            // top에서부터 갈 수 있는 곳이 없으면 answer에 넣기
            if (!routes.containsKey(top) || routes.get(top).isEmpty()) {
                answer.add(stack.pop());
            } else {
                stack.push(routes.get(top).remove(0));
            }
        }

        // 역순으로 저장했으니 역순으로 출력
        Collections.reverse(answer);
        return answer.toArray(new String[0]);
    }
}
