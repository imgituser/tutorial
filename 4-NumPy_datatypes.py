#4. Numpy data typpes
import numpy as np

# Creating NumPy arrays with specified data types
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
arr_float64 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
arr_complex = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)

# Checking the data types of the arrays
print("Data Type of arr_int32:", arr_int32.dtype)
print("Data Type of arr_float64:", arr_float64.dtype)
print("Data Type of arr_complex:", arr_complex.dtype)

# Creating an array with a custom data type
custom_dtype = np.dtype([('name', 'S20'), ('age', int)])
people = np.array([("Ram", 23), ("Maddy", 20), ("Rajiv", 21)], dtype=custom_dtype)

print("\nCustom Data Type Array:")
print(people)

# Accessing elements with custom data type
print("First person's name:", people[0]['name'])
print("Second person's age:", people[1]['age'])
