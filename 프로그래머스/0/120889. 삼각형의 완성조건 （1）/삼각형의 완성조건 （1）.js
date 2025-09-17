function solution(sides) {
    let max = Math.max(...sides);

    // (a + b) => a + b : 누적값(a) + 현재값(b)을 계산 | 0은 초기값
    let sum =  sides.reduce((a, b) => a + b, 0 ) - max;
    
    if (max < sum) return 1;
    else return 2;
}

// reduce : 배열을 하나의 값으로 누적 계산할 때 사용
