def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0    
    list=[]
    while i<len(data):
        if data[i]%2==1:
            list.append(data[i])
        i+=1
    return min(list)
print(find_max_odd([1, 4, 3, 8, 5]))