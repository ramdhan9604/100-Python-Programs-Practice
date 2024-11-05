def power_set_iterative(s):
    power_set =[[]]
    for elem in s:
        for subset in power_set[:]:
            power_set.append(subset+[elem])
    
    return power_set


input_set = [1,2,3,4]

print("The power set of the given input set is : ",power_set_iterative(input_set))