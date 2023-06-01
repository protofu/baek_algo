function solution(s) {
  // s의 길이가 4 혹은 6이 아닐 경우 false를 리턴한다.
  if (s.length !== 4 && s.length !== 6) return false;

  // 문자열을 하나 씩 가져와 숫자로 변환 되는지 확인하고
  // 숫자로 변환되지 못할 경우 false를 리턴한다.
  for (let i = 0; i < s.length; i++) {
    if (isNaN(s[i])) return false;
  }

  // 다 통과 했을 경우 true를 리턴한다.
  return true;
}