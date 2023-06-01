function solution(x, n) {
    let answer = [];
    let temp = 0;
    

    for(let i=1; i<=n; i++){
        answer.push(x*i)
    }

    
    return answer;
}