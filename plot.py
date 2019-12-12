import matplotlib.pyplot as plt

x_nums = list(range(0, 100))
def func(x):
    return x**2 +3*x +2
y_nums = []
for x in x_nums:
    y_nums.append(func(x))

plt.plot (x_nums, y_nums)
plt.show()
