function solution(strlist) {
    let answer = [];
    
    strlist.forEach( function (str){
        answer.push(str.length)
    });
    
    return answer;
}