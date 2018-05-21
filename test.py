import numpy as np

arr = [1, 1, 2, 5]

print(np.bincount(arr))

a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))

C_s = np.logspace(-10, 0, 10)

print(C_s)

from sklearn.metrics import confusion_matrix

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
