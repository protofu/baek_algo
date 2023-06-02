function solution(arr, cmd) {
    let answer = [];
    
    cmd.forEach((s) => {
        let nums = [];
        for(let i=s[0]-1;i<=s[1]-1;i++){
            nums.push(arr[i])
        }
        console.log(nums)
        answer.push(nums.sort((a, b) => a-b)[s[2]-1])
    })
    
    return answer;
}