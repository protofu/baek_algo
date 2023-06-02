function solution(numbers) {
    let answer = [];
    
    for(let i=0;i<numbers.length-1;i++){
        for(let j=i+1;j<numbers.length;j++){
            if(!answer.includes(numbers[i]+numbers[j]))
            answer.push(numbers[i]+numbers[j]);
        }
    }
    answer.sort((a,b) => a-b)
    return answer;
}