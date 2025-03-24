''' Q7. How do you reshape a NumPy array? '''

import pandas as pd
import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)
type(arr)

reshaped = arr.reshape(3,2)
print(reshaped)

reshaped = arr.reshape(2,3)
print(reshaped)
