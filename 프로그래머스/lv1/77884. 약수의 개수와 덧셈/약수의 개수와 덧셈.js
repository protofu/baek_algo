function solution(left, right) {
    let answer = 0;
    let cnt = 0;
    for(left;left<=right;left++){
        for(let i=1;i<=left;i++){
            if(left%i==0){
                cnt+= 1
            }
        }
        if(cnt%2){
            answer -= left
        }
        else{
            answer += left
        }
        cnt = 0;
    }
    
    return answer;
}