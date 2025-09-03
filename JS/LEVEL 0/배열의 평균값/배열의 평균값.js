function solution(numbers) {
  let sum = 0;
  
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  
  let avg = sum / numbers.length;
  return avg;
}

// .length : 배열의 길이를 나타내는 속성