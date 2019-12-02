'''Given an array of integers, return a new array such that each element at 
    index i of the new array is the product of all the numbers in the 
    original array except the one at i'''
    
input_array = [1,2,3,4,10]
output_array = []
for i in input_array:
 
    prod = 1
    for j in input_array:
        if i!=j:
            prod *= j
    output_array.append(prod)


for k in output_array:
    print(k)
