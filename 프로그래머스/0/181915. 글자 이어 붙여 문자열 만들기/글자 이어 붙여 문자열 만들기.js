function solution(my_string, index_list) {
    let answer = '';
    for (let i = 0; i < index_list.length; i++) {
        answer += my_string.charAt(index_list[i]);
    }
    return answer;
}