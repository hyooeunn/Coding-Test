# 각도기
### 2025. 08. 26. (화)

[문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/120829?language=javascript)

### 문제 설명
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 <code>angle</code>이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

- 예각 : 0 < <code>angle</code> < 90
- 직각 : <code>angle</code> = 90
- 둔각 : 90 < <code>angle</code> < 180
- 평각 : <code>angle</code> = 180

### 제한사항
- 0 < <code>angle</code> ≤ 180
- <code>angle</code>은 정수입니다.

### 입출력 예
|angle|result|
|---|---|
|70|1|
|91|3|
|180|4|

***
### 입출력 예 설명
#### 입출력 예 #1
><code>angle</code>이 70이므로 예각입니다. 따라서 1을 return합니다.
#### 입출력 예 #2
> <code>angle</code>이 91이므로 둔각입니다. 따라서 3을 return합니다.
#### 입출력 예 #3
> <code>angle</code>이 180이므로 평각입니다. 따라서 4를 return합니다.