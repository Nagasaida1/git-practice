def closestnumber(numbers):
    numbers.sort()
    min_diff=float('inf')
    for i in range(len(numbers)- 1):
        diff =abs(numbers[i]-numbers[i+1])
        if diff < min_diff:
            min_diff=diff
    result=[]
    for i in range(len(numbers)- 1):
        if abs(numbers[i]-numbers[i + 1]) == min_diff:
            result.append((numbers[i],numbers[i+1]))
    for pair in result:
        print(pair[0],pair[1])
numbers=[6,2,4,10]
closestnumber(numbers)
