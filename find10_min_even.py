def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i=0    
    list=[]
    while i<len(data):
        if data[i]%2==0:
            list.append(data[i])
        i+=1
    return min(list)
print(find_min_even([1, 4, 3, 8, 5]))
