def bubbleSort(arr):
    length = len(arr)-1
	
    for i in range(0,length):
		for j in range(0, length):
			if i > j:
				arr[i], arr[j] = arr[j], arr[i]
				
	return arr


arr = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(arr))