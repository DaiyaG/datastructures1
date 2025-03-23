def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result  
students =[[1, 'Jean Castro', 'v'], [2, 'Lula Powell','v'], [3,'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConvertedlists to a dictionary:")
print(test(students))