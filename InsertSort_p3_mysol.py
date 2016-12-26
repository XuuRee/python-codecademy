# file: insertSort_p3.py
# Example of InsesrSort program 
# that is not inputted by user

def insertSort(array):
    length = len(array)
    i = 0
    while(i < length - 1):
        j = i + 1
        tmp = array[j] 
        while( (j > 0) & (tmp > array[j - 1]) ):
            array[j] = array[j - 1]
            j = j - 1
        array[j] = tmp
        i = i + 1
    return(array)
  
userInput = [ 6, 5, 3, 2, 1, 9, 23, 11 ]
print("Array:               ",userInput)
result = insertSort(userInput)
print("Array after sorting: ",result)
