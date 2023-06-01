function solution(arr, divisor) {
    let answer = [];
    
    arr.forEach(function(s){
        if(s%divisor === 0){
            answer.push(s)
        }
    })
    
    if(answer.length ===0){
        answer.push(-1)
    }
    else{
        answer.sort((a, b) => a - b)
    }

    return answer;
}