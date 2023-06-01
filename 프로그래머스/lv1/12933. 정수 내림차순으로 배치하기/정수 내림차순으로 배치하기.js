function solution(n) {
    let answer = '';
    
    const str = n.toString()
    let arr = [];
    
    for(let i=0; i<str.length; i++){
        arr.push(Number(str[i]));    
    };
    
    arr.sort((a, b) => b - a).forEach((s) => answer+=s)
    answer = Number(answer)
    
    return answer;
}