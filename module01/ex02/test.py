from vector import Vector 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)
# Expected output:
print(bcolors.OKCYAN, "Vector([[0.0], [5.0], [10.0], [15.0]])", bcolors.ENDC)
# Row vector of shape 1 * n
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
# Expected output:
print(bcolors.OKCYAN, "Vector([[0.0, 5.0, 10.0, 15.0]])", bcolors.ENDC)
v2 = v1 / 2.0
print(v2)
# Expected output:
print(bcolors.OKCYAN, "Vector([[0.0], [0.5], [1.0], [1.5]])", bcolors.ENDC)
try :
    v1 / 0.0
except ZeroDivisionError as err:
	# Expected output:
	print(bcolors.OKCYAN, err, bcolors.ENDC)
try :
	2.0 / v1
except TypeError as err:
      # Expected output:
	print(bcolors.OKCYAN, err, bcolors.ENDC)





# Column vector of shape (n, 1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Expected output:
print(bcolors.OKCYAN, "(4,1)", bcolors.ENDC)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
# Expected output:
print(bcolors.OKCYAN, "[[0.0], [1.0], [2.0], [3.0]]", bcolors.ENDC)
# Row vector of shape (1, n)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
# Expected output:
print(bcolors.OKCYAN, "(1,4)", bcolors.ENDC)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
# Expected output:
print(bcolors.OKCYAN, "[[0.0, 1.0, 2.0, 3.0]]", bcolors.ENDC)




# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
# Expected output:
print(bcolors.OKCYAN, "(4,1)", bcolors.ENDC)
print(v1.T())
# Expected output:
print(bcolors.OKCYAN, "Vector([[0.0, 1.0, 2.0, 3.0]])", bcolors.ENDC)
print(v1.T().shape)
# Expected output:
print(bcolors.OKCYAN, "(1,4)", bcolors.ENDC)
# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
# Expected output:
print(bcolors.OKCYAN, "(1,4)", bcolors.ENDC)
print(v2.T())
# Expected output:
print(bcolors.OKCYAN, "Vector([[0.0], [1.0], [2.0], [3.0]])", bcolors.ENDC)
print(v2.T().shape)
# Expected output:
print(bcolors.OKCYAN, "(4,1)", bcolors.ENDC)


# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
print(bcolors.OKCYAN, "18.0", bcolors.ENDC)
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
print(bcolors.OKCYAN, "14.0", bcolors.ENDC)
v1
# Expected output: to see what __repr__() should do
print(bcolors.OKCYAN, "[[0.0, 1.0, 2.0, 3.0]]", bcolors.ENDC)
print(v1)
# Expected output: to see what __str__() should do
print(bcolors.OKCYAN, "[[0.0, 1.0, 2.0, 3.0]]", bcolors.ENDC)