import numpy as np

transactions = np.array([[1200, 1500, 1600, 1800, 1700, 2000],
                         [1000, 1100, 1300, 1400, 1500, 1600],
                         [2000, 2100, 2200, 2300, 2400, 2500],
                         [1700, 1600, 1500, 1400, 1300, 1200]])

totals = np.sum(transactions, axis=1)
print(totals)
