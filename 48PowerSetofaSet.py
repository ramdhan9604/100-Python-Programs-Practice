# def powerset(input_set):
#     # Convert the input set to a list
#     s = list(input_set)
    
#     # Start with the empty set
#     result = [[]]
    
#     # Iterate over each element in the set
#     for elem in s:
#         # For each element, add it to all existing subsets to form new subsets
#         new_subsets = []
#         for subset in result:
#             new_subsets.append(subset + [elem])
#         # Add the new subsets to the result
#         result.extend(new_subsets)
    
#     return result

# # Example usage
# input_set = {1, 2, 3}
# ps = powerset(input_set)

# # Print the powerset
# for subset in ps:
#     print(subset)


def power_set(input_set):
    s = list(input_set)

    result = [[]]

    for elem in s:
        new_subset = []

        for subset in result:
            new_subset.append(subset+[elem])
        result.extend(new_subset)
    return result

input_set = {1,2,3,4,5}
ps = power_set(input_set)

for subset in ps:
    print(subset)
