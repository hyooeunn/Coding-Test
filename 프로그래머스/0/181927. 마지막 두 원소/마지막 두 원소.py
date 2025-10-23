def solution(num_list):
    last = num_list[len(num_list) - 1]
    secondLast = num_list[len(num_list) - 2]
    
    if last > secondLast:
        num_list.append(last - secondLast)
    else:
        num_list.append(last * 2)
        
    return num_list