function solution(n)
{
    let answer = 0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    let str = n.toString()
    for (let i = 0; i<str.length; i++){
        answer += Number(str[i])
        console.log(i)
    }
    return answer;
}