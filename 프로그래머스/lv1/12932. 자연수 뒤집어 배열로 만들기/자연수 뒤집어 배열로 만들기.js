function solution(n) {
    let answer = [];
    
    const str = n.toString();
    
    for(let i=str.length-1;i>=0;i--){
        answer.push(Number(str[i]))
    }
    
    return answer;
}