function solution(strings, skip, index) {
    let answer = '';
    
    const alpha = new Set('abcdefghijklmnopqrstuvwxyz');
    [...skip].forEach(val => alpha.delete(val));
    
    const arr = [...alpha];
    
    for(const s of strings){
        const idx = arr.indexOf(s) + index;
        answer += arr[idx % arr.length];
    }
    
    return answer;
}