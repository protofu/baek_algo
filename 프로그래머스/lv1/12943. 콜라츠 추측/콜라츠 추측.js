function solution(num) {
    let answer = 0;
    let tmp = num;
    
    
    while(tmp != 1){
        if(tmp == 1){
            break;
        }
        else if(answer >= 500){
            answer = -1
            break
        }
        else{
            if(tmp%2==0){
                tmp/=2
            }
            else if(tmp%2){
                tmp= tmp*3 +1
            }
            answer += 1
        }
    }
    
    return answer;
}