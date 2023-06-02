function solution(d, budget) {
    let answer = 0;
    
    d.sort((a, b) => a - b).forEach((s) => {
        if(budget-s>=0){
            budget -= s
            answer += 1
        }
    })
    
    return answer;
}