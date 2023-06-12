function solution(A, B) {
    let answer = 0; // A의 원소가 B의 원소보다 작은 경우의 개수를 저장할 변수

    A.sort((a, b) => b - a); // A 배열을 내림차순으로 정렬합니다.
    B.sort((a, b) => a - b); // B 배열을 오름차순으로 정렬합니다.

    for (const a of A) {
        const max = B[B.length - 1]; // B 배열의 가장 큰 원소를 가져옵니다.
        if (a < max) { // A의 원소가 B의 가장 큰 원소보다 작은 경우
            answer++; // answer 값을 증가시킵니다.
            B.pop(); // B 배열의 가장 큰 원소를 제거합니다.
        }
    }

    return answer; // A의 원소가 B의 원소보다 작은 경우의 개수를 반환합니다.
}
