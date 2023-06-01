function solution(price, money, count) {
    let answer = 0;
    let tmp = 0;
    for(let i=0;i<count;i++){
        tmp += price
        answer += tmp
    }
    if(money - answer>=0){
        return 0
    }
    else{
        return answer-money;
    }
    
}