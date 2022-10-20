# Python3 program for the above approach

# Function to find the permutation of
# array elements such that the sum of
# elements at odd āindices is greater
# than sum of elements at even indices
def rearrangeArray(arr, n):
	
	# Sort the given array
	arr = sorted(arr)

	# Initialize the two pointers
	j = n - 1
	i = 0

	# Traverse the array arr[]
	for k in range(n):
		
		# Check if k is even
		if (k % 2 == 0):
			print(arr[i], end = " ")
			
			# Increment the value
			# of i
			i += 1
		else:
			print(arr[j], end = " ")

			# Decrement the value
			# of j
			j -= 1

# Driver Code
if __name__ == '__main__':

	arr = [ 123, 45, 67, 89, 60, 33 ]
	N = len(arr)
	
	rearrangeArray(arr, N)

