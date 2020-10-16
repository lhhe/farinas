import numpy as np

test = np.array([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0])
print(len(test))
location = np.where(test == 1)[0]
print(location)

inicio = location.min()
fin = location.max()
print(inicio)
print(fin)
print("##")
print(np.unique(test, return_index=True))
