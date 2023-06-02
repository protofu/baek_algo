function solution(arr, k) {
    let answer = [];
    
    arr.forEach((s) => {
        if(k%2){
            answer.push(s*k)
        }
        else{
            answer.push(s+k)
        }
    })
    
    return answer;
}