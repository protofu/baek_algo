function solution(arr) {
    let answer = [];
        
    if(arr.length > 1){
        let tmp = [];
        arr.forEach((s) => tmp.push(s))

        arr.sort((a, b) => a - b);

        tmp.forEach((s) => {
            if(s != arr[0]){
                answer.push(s)
            }
        })
    }
    else{
        answer.push(-1)
    }
    
    
    return answer;
}