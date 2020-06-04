# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        #start on current Value  loop thru rest to the  right 
        # if smaller value is found store that index location as smallest 
        # swap the smallest index with the current inder in the array 
        # current index moves to the right and continues loops   
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
    # temp = arr[cur_index]     
    # arr[cur_index] = arr[smallest_index]
    # arr[smallest_index] = temp 

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
# swap count to track swaps during for loop, if no swap occurs , array is ordered 
#start with first  index, compare  with next index in list, if grater than index, switch  the two indexes
#increment swap count 
#move the next index and restart the loop
#when at the end of the list, if there are swaps continue, if not swapt you are done
    # swapcount = 0
    # while swapcount > 0:
    #     swapcount  = 0 
    #     for i in range(0, len(arr)-1):
    #         if arr[i] >arr[i+1]:
    #             temp = arr[i]
    #             arr[i] = arr[i+1]
    #             arr[i+1] = temp
    #             swapcount = 1  

    for i in range (len(arr)-1):
        for j in range (len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr