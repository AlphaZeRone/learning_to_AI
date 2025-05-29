import numpy as np

nums = np.array([1, 2, 3])
print(nums)
print(nums.size)

matrix_num1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_num2 = np.array([[10, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_num1[0]) # [1 ,2, 3]
print(matrix_num1[1][0]) # 4

print(nums + matrix_num2) #ช่วยให้สามารถดึงค่ามาใช้งานได้ง่ายกว่าการใช้ List


