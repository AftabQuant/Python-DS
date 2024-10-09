import numpy as np
ar = np.array([1, 2, 3, 4])
print(np.append(ar, 10))

br = np.array([[1,2,3], [4,5,6]])
print(np.append(br, 50))
print(np.insert(br, 0, 60)) # array, index, value

# Delete The Array
print(np.delete(br,0))