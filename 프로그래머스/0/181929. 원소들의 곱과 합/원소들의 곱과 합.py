def solution(num_list):
    total = 0
    product = 1
    
    for i in range(len(num_list)):
        total += num_list[i]
        product *= num_list[i]
        
    if product < total * total:
        return 1
    else:
        return 0