def staircaseTraversal(height, maxSteps):
    # Write your code here.
	return numberOfWaysToTheTop(height, maxSteps, {0:1, 1:1})
    
def numberOfWaysToTheTop(height, maxSteps, memoize):
	if height in memoize:
        return memoize[height]
	
	numberOfWays = 0
	for step in range(1, min(height, maxSteps)+1):
		numberOfWays += numberOfWaysToTheTop(height-step, maxSteps)
    
    memoize[height] = numberOfWays
		
	return numberOfWays

# Time Complexity O(K^N)  | Space Complexity O(n)