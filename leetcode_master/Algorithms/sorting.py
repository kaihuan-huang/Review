# Sorting - Insertion Sort
for (i from 1 to arr.length){
    j = i - 1
    while (j > 0 and arr[j + 1] < arr[j]){
        tmp = arr[j + 1]
        arr[j + 1] = arr[j]
        arr[j] = tmp
        j -= 1
    }
}

# Sorting - Merge Sort - two branch recursion - Divide & Conquer
# TC: O(nlogn) SC: O(n)
# common used algorithms
int[]
def mergeSort(int[] arr, int s, int e){
    if (e - s + 1 <= 1)
    return arr;
    
    m = (s + e) / 2;
    mergeSort(arr, s, m);
    mergeSort(arr, m + 1, e);
    
    merge(arr, s, m, e);
    return arr;
}

# Sorting - Quick Sort 
# 
int[]
quickSort(int[] arr, int s, int e){
    if (e - s + 1 <= 1)
    return arr

    pivot = arr[e]
    left = s
    
    # Partition: elements smaller than pivot on the left side
    for i form s to e {
        if (arr[i] < pivot){
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1
        }
    }
    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot
    
    quickSort(arr, s, left - 1)
    quickSort(arr, left + 1, e)
    return arr
}