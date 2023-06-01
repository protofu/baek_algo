function solution(x) {
    let answer = true;
    
    let str = x.toString();
    let tmp = 0;
    for(let i=0; i<str.length;i++){
        tmp += Number(str[i])
    }
    if(x%tmp){
        answer = false;
    }
    
    return answer;
}