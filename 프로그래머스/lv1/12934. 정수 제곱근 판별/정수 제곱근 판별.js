function solution(n) {
    let answer = 0;
    
    for(let i=1; i<5000000000000; i++){
        if(n===i*i){
            answer = (i+1)*(i+1);
            break;
        }
        if(i*i >n){
            answer = -1
            break
        }
    }
    
    return answer;
}