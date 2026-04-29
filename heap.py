'''
scratch implementation of heap
There are two type of heap
1. max heap - mainly uses during heapsort algorithm
2. min heap - mainly uses during priority queue

Heap representation is like binary tree, nornally array is used to store heap.
if A is an heap array
for ith node
children = left := 2*i
           right := 2*i+1
           parent := floor(i/2)

LEFT PROCEDURE 2*i = left shift bit by one position
RIGHT PROCEDURE 2*i + 1 = left shift bit by one position + 1 
PARENT floor(i/2) = right shift bit by one position

where each child nodes satify heap property:


HEAP PROPERTY
MAX HEAP 
    for each nodes i, except root node:
        A[parent[i]] >= A[i]

MIN HEAP
    for each ndoe i,except root node
    A[parent[i]] <= A[i]



Operation  - heapify and build-heap
insert,heap-extract,heap-increase-key,heap-maximum - time complexity O(logn)


time complexity of heapify - 0(logn)
time complexity of build-heap - O(n*logn)
'''



# implementation of max-heapify



def max_heapify(A,i):

    right = i*2+2
    left = i*2+1

    if left <= len(A)-1 and A[left]>A[i]:
        largest = left

    else:
        largest = i

    if right <= len(A)-1 and A[right]> A[largest]:
        largest = right


    # check i == largest

    if i != largest:
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A,largest)


A = [16,4,10,14,7,9,3,2,8,1]


def build_max_heap(A,n):
    for i in range(n//2-1,-1,-1):
        max_heapify(A,i)


build_max_heap(A,len(A))
print(A)
