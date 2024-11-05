# def pascal_triangle(n):
#     li =[[1]]

#     for i in range(1,n):
#         prev_row=li[-1]
#         curr_row = [1]+[prev_row[j]+prev_row[j-1] for j in range(i-1)]+[1]
#         li.append(curr_row)


# print("The pascal triangle is: ",li)

def pascal_triangle(n):
    li = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = li[-1]
        # Generate the current row using the previous row
        curr_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        li.append(curr_row)

    return li  # Return the triangle

# Example usage
n = 8
triangle = pascal_triangle(n)
print("The Pascal's triangle is: ")
for row in triangle:
    print(row)
