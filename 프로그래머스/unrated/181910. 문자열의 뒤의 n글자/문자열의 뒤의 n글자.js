function solution(s, n) {
    let answer = '';
    
    for(let i=s.length-n;i<s.length;i++){
        answer+=s[i]
    }
    
    return answer;
}