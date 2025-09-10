function solution(n, k) {
  let service = Math.floor(n / 10);
  
  return (n * 12000) + ((k - service) * 2000);
}

// Math.floor() : 소수점 이하를 내림하여 정수로 반환