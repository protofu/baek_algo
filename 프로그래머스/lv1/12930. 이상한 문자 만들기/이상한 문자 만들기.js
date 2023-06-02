function solution(s) {
    let answer = '';
    let cnt = 1;
    
    for(let i=0;i<s.length;i++){
        if(s[i]!=' '){
            if(cnt%2){
                answer+=s[i].toUpperCase()
                cnt+=1
            }
            else if(cnt%2==0){
                answer+=s[i].toLowerCase()
                cnt+=1
            }
        }
        else{
            answer += ' ';
            cnt = 1;
        }
    }
    
    return answer;
}