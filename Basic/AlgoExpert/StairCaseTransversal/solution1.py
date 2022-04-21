def staircaseTraversal(height, maxSteps):
    # Write your code here.
	return numberOfWaysToTheTop(height, maxSteps)
    
def numberOfWaysToTheTop(height, maxSteps):
	if height <= 1:
		return 1
	
	numberOfWays = 0
	for step in range(1, min(height, maxSteps)+1):
		numberOfWays += numberOfWaysToTheTop(height-step, maxSteps)
		
	return numberOfWays