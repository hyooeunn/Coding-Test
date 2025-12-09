function solution(numbers, num1, num2) {
    return numbers.slice(num1, num2 + 1);
}

// 다른 풀이
// return numbers.splice(num1, num2 - num1 + 1)
