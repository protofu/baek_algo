function solution(sizes) {
    let answer = 0;
    let width = [];
    let height =[];
    sizes.forEach((s) => {
        const max = Math.max(s[0], s[1]);
        const min = Math.min(s[0], s[1]);
        width.push(max);
        height.push(min);
    })

    answer = Math.max(...width)*Math.max(...height)
    return answer;
}