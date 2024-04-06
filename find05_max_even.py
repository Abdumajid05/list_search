def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0    
    list=[]
    while i<len(data):
        if data[i]%2==0:
            list.append(data[i])
        i+=1
    return max(list)
print(find_max_even([1, 4, 3, 8, 5]))