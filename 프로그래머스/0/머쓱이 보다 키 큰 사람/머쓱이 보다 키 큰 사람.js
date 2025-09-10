function solution(array, height) {
  let count = 0
  
  for (let i = 0; i < array.length; i++) {
    // 그 친구 키가 머쓱이보다 크면 카운트 1을 늘려줌
    if (array[i] > height) count++ 
  }
  
  return count;
}