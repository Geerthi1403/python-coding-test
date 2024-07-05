def squre_evens(numbers:list)-> list:
    return [x**2 for x in numbers if x % 2==0]
print(squre_evens([1,2,3,4]))
