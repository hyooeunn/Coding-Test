function solution(my_string, index_list) {
    let answer = '';
    for (let i = 0; i < index_list.length; i++) {
        answer += my_string.charAt(index_list[i]);
    }
    return answer;
}

// charAt(): 문자열에서 특정 인덱스의 문자를 반환하는 메서드
// 문자열에서 주어진 위치의 문자를 가져오는데 사용함
