import numpy as np

data = np.array([
    [1250, 1350, 1450, 1550, 1650, 1750],
    [1050, 1120, 1180, 1260, 1330, 1400],
    [1950, 2050, 2150, 2250, 2350, 2450],
    [950, 1020, 1120, 1220, 1320, 1420]
])

branch_totals = np.sum(data, axis=1)
print(branch_totals)

top_branch = np.argmax(branch_totals) + 1
print(top_branch)

average_transactions = np.mean(data)
print(average_transactions)

reshaped_array = data.reshape(3, 8)
print(reshaped_array)
