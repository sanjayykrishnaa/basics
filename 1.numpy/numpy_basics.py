import numpy as np

arr = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
print("Array:", arr)  # Print the array
print("Type:", type(arr))  # Print the type of the array
print("First element:", arr[0])  # Print the first element of the array
print("Second element:", arr[1])  # Print the second element of the array
print("Sum of third and fourth elements:", arr[2] + arr[3])  # Print the sum of the third and fourth elements
print("First four elements:", arr[:4])  # Print the first four elements of the array
print("Elements from index 4 onwards:", arr[4:])  # Print the elements from index 4 onwards
print("Elements from index 1 to 5 with step 2:", arr[1:5:2])  # Print the elements from index 1 to 5 with step 2
print("Every second element:", arr[::2])  # Print every second element of the array
x = np.where(arr == 4)
print("Indices where element is 4:", x)  # Print the indices where the element is 4
print("Sorted array:", np.sort(arr))  # Print the sorted array

print("Data type of the array:", arr.dtype)  # Print the data type of the array

two_d_arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', two_d_arr[1, 4])  # Print the 5th element on the 2nd row
print("Elements from index 0 to 1 on both rows:", two_d_arr[0:2, 2])  # Print the elements from index 0 to 1 on both rows
print("Elements from index 1 to 3 on both rows:", two_d_arr[0:2, 1:4])  # Print the elements from index 1 to 3 on both rows

three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Element at index (0, 1, 2):", three_d_arr[0, 1, 2])  # Print the element at index (0, 1, 2)
print("Shape of the array:", three_d_arr.shape)  # Print the shape of the array
print("Sorted array:", np.sort(three_d_arr))  # Print the sorted array

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
newarr = np.concatenate((arr1, arr2))
print("Concatenated array:", newarr)  # Print the concatenated array

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print("Array split into 3 parts:", newarr)  # Print the array split into 3 parts
