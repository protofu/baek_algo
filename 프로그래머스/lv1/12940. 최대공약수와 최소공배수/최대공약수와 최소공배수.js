function solution(n, m) {
    let answer = [];
    let tmp1 = 0;
    let tmp2 = 0;
    for(let i=1;i<=n*m;i++){
        if(n%i == 0 && m%i ==0){
            tmp1 = i
        }
        if(i%n == 0 && i%m == 0){
            tmp2 = i
            return [tmp1, tmp2]
        }
    }
    
}