function solution(n) {
    let sum = 0;
    let str = String(n);
    
    for (let i = 0; i < str.length; i++) {
        sum += Number(str[i]);
    }
    return sum;
}