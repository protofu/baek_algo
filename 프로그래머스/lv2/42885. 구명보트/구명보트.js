function solution(people, limit) {
    let answer = 0;

    people.sort((a, b) => b - a); // 내림차순으로 정렬

    // i는 왼쪽 인덱스, j는 오른쪽 인덱스
    for (let i = 0, j = people.length - 1; i <= j; i++) {
        // 왼쪽 사람과 오른쪽 사람의 무게 합이 limit 이하인 경우
        if (people[i] + people[j] <= limit)
            j--; // 오른쪽 인덱스를 한 칸 앞으로 이동하여 다음으로 무거운 사람과 짝을 이룸
        answer++; // 한 쌍의 사람을 구출했으므로 구출된 사람 수 증가
    }

    return answer; // 구출된 사람 수 반환
}
