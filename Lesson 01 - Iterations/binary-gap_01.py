def solution(N):

    binary = f'{N:b}'
    count_zeros = 0
    before_sequence_element = binary[0]
    results = []

    for ind in range(1, len(binary)-1):

        if binary[ind] == '0':

            count_zeros += 1

        else:

            final_sequence_element = binary[ind]
            results.append((before_sequence_element, final_sequence_element, count_zeros))
            before_sequence_element = final_sequence_element
            count_zeros = 0

    
    if binary[-1] == 0:
        
        count += 1
        final_sequence_element = binary[-1]
        results.append((before_sequence_element, final_sequence_element, count_zeros))
        
    else:
        
        final_sequence_element = binary[-1]
        results.append((before_sequence_element, final_sequence_element, count_zeros))
    
    sorted_list = sorted(results, key=lambda x:x[-1], reverse=True)
    
    sorted_list = [value for value in sorted_list if (value[0] == '1') & (value[1] == '1')]
    
    return sorted_list[0][-1] if len(sorted_list) != 0 else 0