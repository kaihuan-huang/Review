import heapq

# heapq: data structure to find Min and Max of a set of values
# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 6)
heapq.heappush(minHeap, 2)

print(minHeap)
# Min is always at index 0, by default: heap in python are Min heap
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap)) #the value will be print from smallest to largest
    
# No Max heap by default, use min heao and multiply by -1 when push & pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
# Max is always at index 0
print("maxHeap = ", -1 * maxHeap[0])
# Using while loop to get the mapHeap from largest to smallest
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# build heap from initial values: linear time by using heapify method
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr)) # by defaule printind the arr from smallest

while arr:
    print(-1 * heapq.heappop(arr)) # reverse
    

