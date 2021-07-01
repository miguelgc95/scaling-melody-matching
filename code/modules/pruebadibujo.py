# import matplotlib as plt
# import numpy as np

# x, x2 = [], []
# y, y2 = [], []

# R = [[0, 4, 120], [4, 6, 400], [6, 9, 700], [9, 12, 350], [12, 15, 550]]
# Q = [[0, 5.5, 300], [5.5, 8.5, 550], [8.5, 10.5, 750],
#      [10.5, 13.5, 400], [13.5, 20, 600]]

# if Q[-1][1] > R[-1][1]:  # en caso de que Q sea más grande que R, intercambiamos sus papeles para poder aplicar el algoritmo y escalamos R en vez de Q
#     P = Q[:]
#     Q = R[:]
#     R = P[:]

# maxeps = (R[-1][1]-Q[-1][1])/len(Q)
# Q[-1][1] = R[-1][1]

# x.append(R[0][0])
# y.append(R[0][2])
# for i in R:
#     x.append(i[1])
#     y.append(i[2])

# x2.append(Q[0][0])
# y2.append(Q[0][2])

# for j in Q:
#     x2.append(j[1])
#     y2.append(j[2])

# x = np.array(x)
# y = np.array(y)
# x2 = np.array(x2)
# y2 = np.array(y2)

# plt.pyplot.step(x, y, x2, y2)
# # plt.pyplot.fill(x,y, step="pre")
# plt.pyplot.fill_between(x2, y2, step="pre")
# plt.pyplot.show()

# import glob

# print(glob.glob("./DB_files/deblas/*.csv")[0][21:-4])

import numpy as np

dicti = {'a': 1}
print(np.list(dicti.values()).flat())
