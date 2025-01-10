def maximumFinal(arr):
    # Sort the array
    arr.sort()

    # Adjust values based on constraints
    arr[0] = 1
    for i in range(1, len(arr)):
        arr[i] = min(arr[i], arr[i-1] + 1)

    # Return the last element
    return arr[-1]