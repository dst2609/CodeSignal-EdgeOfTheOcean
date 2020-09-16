def adjacentElementsProduct(inputArray):
    multi = []
    for n in range(len(inputArray) - 1):
        multi.append(inputArray[n] * inputArray[n+1])
    
    return (max(multi))
        
