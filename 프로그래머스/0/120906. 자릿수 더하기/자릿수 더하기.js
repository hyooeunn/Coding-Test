function solution(n) {
    let sum = 0;
    let str = String(n);
    
    for (let i = 0; i < str.length; i++) {
        sum += Number(str[i]);
    }
    return sum;
}

// String() : 다른 타입을 문자열로 바꿔주는 함수
// Number() : 다른 타입을 숫자로 바꿔주는 함수
