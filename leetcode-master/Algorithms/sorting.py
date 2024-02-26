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