function solution(arr) {
    var answer = 0;
    
    arr.forEach(function(arr){
        answer+=arr
    })
    answer/=arr.length
    return answer;
}