function solution(money) {
    let count = Math.floor(money / 5500);
    let remain = money % 5500;
    return [count, remain];
}