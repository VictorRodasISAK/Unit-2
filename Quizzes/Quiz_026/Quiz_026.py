import matplotlib.pyplot as plt

data = {
    'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    'y': [24, 1, 2, 25, 26, 21, 23, 34, 49, 2, 19, 32, 7, 17, 36, 7, 45, 28, 40, 46]
}

if 'title' in data:
    print(data['title'])
else:
    data['title'] = "Quiz_data_science"

plt.title(data['title'], color="red")
plt.plot(data['x'], data['y'])
plt.show()
