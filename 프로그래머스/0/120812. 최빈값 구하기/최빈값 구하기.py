def solution(array):
    set_list = list(set(array))
    
    num_count = [0] * len(set_list)
    
    for i in range(len(set_list)):
        num_count[i] = array.count(set_list[i])
    
    mode_idx = num_count.index(max(num_count))
    
    if num_count.count(max(num_count)) != 1:
        answer = -1
    
    else:
        answer = set_list[mode_idx]
        
    return answer