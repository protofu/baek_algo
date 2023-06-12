function solution(maps) {
    const xLength = maps.length; // 맵의 세로 길이
    const yLength = maps[0].length; // 맵의 가로 길이
    const dx = [0, 0, -1, 1]; // 상하좌우 이동을 위한 x축 방향 배열
    const dy = [-1, 1, 0, 0]; // 상하좌우 이동을 위한 y축 방향 배열

    const bfs = () => {
        const queue = [[0, 0, 1]]; // 시작 지점인 (0, 0)부터 탐색을 시작하며, 카운트 값은 1부터 시작합니다.
        while (queue.length) {
            const [x, y, count] = queue.shift(); // 큐에서 현재 위치와 카운트 값을 가져옵니다.
            if (x === xLength - 1 && y === yLength - 1) {
                return count; // 도착 지점에 도달한 경우, 카운트 값을 반환합니다.
            }
            if (maps[x][y]) {
                maps[x][y] = 0; // 방문한 곳을 표시하기 위해 값을 0으로 변경합니다.
                dx.forEach((dx, i) => {
                    const nx = x + dx; // 다음 이동할 위치의 x 좌표
                    const ny = y + dy[i]; // 다음 이동할 위치의 y 좌표
                    if (nx >= 0 && nx < xLength && ny >= 0 && ny < yLength && maps[nx][ny]) {
                        queue.push([nx, ny, count + 1]); // 다음 이동할 위치를 큐에 추가하고, 카운트 값을 1 증가시켜 함께 저장합니다.
                    }
                });
            }
        }
        return -1; // 도착 지점에 도달하지 못한 경우, -1을 반환합니다.
    };

    return bfs(); // BFS 함수를 호출하여 최단 경로의 카운트 값을 반환합니다.
}
