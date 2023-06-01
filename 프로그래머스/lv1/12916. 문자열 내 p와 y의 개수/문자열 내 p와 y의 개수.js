function solution(s){
    let answer = true;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    const str = s.toUpperCase();
    let check = 0;
    
    for(let i=0; i<s.length; i++){
        if(str[i] ==='P'){
            check += 1
        }
        else if(str[i] === 'Y'){
            check -= 1
        }
    }
    if(check!=0){
        answer = false;
    }
    return answer;
}