function solution(a, b) {
    let answer = 0;
    const arr = [a, b];
    arr.sort((c, d) => c - d)
    
    
    for(let i=arr[0]; i<=arr[1]; i++){
        answer += i
    }
    
    return answer;
}