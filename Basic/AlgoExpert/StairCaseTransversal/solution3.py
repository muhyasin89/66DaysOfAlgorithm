def staircaseTraversal(height, maxSteps):
    # Write your code here.
    waysToTop = [0 for _ in range(height+1)]
	waysToTop[0] = 1
	waysToTop[1] = 1
	
	for currentHeight in range(2, height + 1):
		step =1
		while step <= maxSteps and step <= currentHeight:
			waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
			step +=1
	return waysToTop[height]

# O(n* k) time | O(n) space  - where n is height k is max steps