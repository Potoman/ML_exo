import csv
import numpy as np
import matplotlib.pyplot as plt


# For data set, download this : https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

class House:
    def __init__(self, price, area, bedrooms):
        self.price = int(price)
        self.area = int(area)
        self.bedrooms = int(bedrooms)

    def __repr__(self):
        return f"Price(price={self.price}, area={self.area}, bedrooms={self.bedrooms})"

houses = []

with open('Housing.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
    for row in reader:
        houses.append(House(price=row['price'], area=row['area'], bedrooms=row['bedrooms']))

houses = houses

m = len(houses)
n = 3

teta = np.zeros(n)
x = np.zeros((len(houses), n))
y = np.zeros(len(houses))
for i in range(m):
    y[i] = houses[i].price

for i in range(m):
    x[i] = [1, houses[i].area, houses[i].bedrooms]

alpha = 0.0000000001

def h(i):
    _h = 0
    for j in range(n):
        _h = _h + teta[j] * x[i][j]
    return _h

def new_teta():
    global teta
    for j in range(n):
        total = 0
        for i in range(m):
            total = total + (h(i) - y[i]) * x[i][j]

        teta[j] = teta[j] - alpha * total


def new_y():
    tmp_y = np.zeros(m)
    for i in range(m):
        tmp_y[i] = h(i)
    return tmp_y


axis_x = np.zeros((m, 1))
for i in range(m):
    axis_x[i] = x[i][1]

axis_y = np.zeros((m, 1))
for i in range(m):
    axis_y[i] = x[i][2]


def new_increment():
    new_teta()


if n == 2:
    plt.scatter(axis_x, y, marker="+", label="start")

    number_increment = 10
    for inc in range(number_increment):
        new_increment()
        plt.scatter(axis_x, new_y(), marker="+", label="increment_" + str(inc))

    plt.legend()
    plt.show()

elif n == 3:
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    sampling = 10

    ax.scatter(axis_x[::sampling], axis_y[::sampling], y[::sampling], marker='x', label="real")

    number_increment = 100
    for inc in range(number_increment):
        new_increment()
        #if inc == 0:
        #    ax.scatter(axis_x[::sampling], axis_y[::sampling], new_y()[::sampling], marker='.', label="increment_" + str(inc))

    ax.scatter(axis_x[::sampling], axis_y[::sampling], new_y()[::sampling], marker='.', label="increment_" + str(inc))

    ax.set_xlabel('area')
    ax.set_ylabel('bedrooms')
    ax.set_zlabel('price')

    plt.legend()
    plt.show()