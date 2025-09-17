function solution(sides) {
    let max = Math.max(...sides);
    
    let sum =  sides.reduce((a, b) => a + b, 0 ) - max;
    
    if (max < sum) return 1;
    else return 2;
}