from collections import deque

def Merge(arr1, arr2):
	if len(arr1) == 0:
		return arr2
	if len(arr2) == 0:
		return arr1
	if arr1[0] > arr2[0]:
		return [arr2[0]] + Merge(arr1, arr2[1:])
	else:
		return [arr1[0]] + Merge(arr1[1:], arr2)

# recursive version
def MergeSort(array):
	n = len(array)
	if n <= 1:
		return array
	return Merge(MergeSort(array[:n//2]), MergeSort(array[n//2:]))

# iterative version
def IterativeMergeSort(array):
	queue = deque()
	for i in array:
		queue.append([i])
	while len(queue) > 1:
		m = Merge(queue.popleft(), queue.popleft())
		queue.append(m)
	return queue.popleft()


if __name__ == '__main__':
	arr = [534,6,7,32,68,6523,56,9989,34,2536]
	print(MergeSort(arr))
	print(IterativeMergeSort(arr))