#!/usr/bin/env python3

# Python3 program to print 
# given matrix in spiral form 
def spiralPrint(m, n, a):
	r = 0; c = 0

	''' r - starting row index 
		m - ending row index 
		c - starting column index 
		n - ending column index 
		i - iterator '''
	

	while (r < m and c < n) : 
		
		# Print the first row from 
		# the remaining rows 
		for i in range(c, n) : 
			print(a[r][i], end = " ") 
			
		r += 1

		# Print the last column from 
		# the remaining columns 
		for i in range(r, m) : 
			print(a[i][n - 1], end = " ") 
			
		n -= 1

		# Print the last row from 
		# the remaining rows 
		if ( r < m) : 
			
			for i in range(n - 1, (c - 1), -1) : 
				print(a[m - 1][i], end = " ") 
			
			m -= 1
		
		# Print the first column from 
		# the remaining columns 
		if (c < n) : 
			for i in range(m - 1, r - 1, -1) : 
				print(a[i][c], end = " ") 
			
			c += 1

# Driver Code 
a = [ [1, 2, 3, 4, 5, 6], 
	[7, 8, 9, 10, 11, 12], 
	[13, 14, 15, 16, 17, 18] ] 
		
R = 3; C = 6
spiralPrint(R, C, a) 

