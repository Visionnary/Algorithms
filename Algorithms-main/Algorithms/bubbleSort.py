def bubbleSort(arr):
    temp = 0;
    for i in range(len(arr)):
      
        ## (n-k-1) is for ignoring comparisons of elements which have already been compared in earlier iterations
        for j in range(len(arr)-1):
            if(arr[ j ] > arr[j+1]):
                ## here swapping of positions is being done.
                temp = arr[ j ];
                arr[ j ] = arr[ j+1 ];
                arr[ j + 1] = temp;
