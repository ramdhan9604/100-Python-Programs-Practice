list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25},
{'name': 'Bob', 'age': 35}]

sorted_dict = sorted(list_of_dicts,key=lambda x:x['age'])
print("Sorted list: ",sorted_dict)