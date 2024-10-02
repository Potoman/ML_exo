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

m = len(houses)
n = 2

teta = np.zeros(n)
x = np.zeros((len(houses), n))
y = np.zeros(len(houses))
for i in range(m):
    y[i] = houses[i].price

for i in range(m):
    x[i] = [1, houses[i].area] #, house.bedrooms]

alpha = 0.00000000002

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
#T = np.array([6, 7, 8, 9, 10, 11, 12])
#power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])

plt.scatter(axis_x, y, marker="+", label="start")
pass

increment = 0

def new_increment():
    new_teta()

number_increment = 3
for inc in range(number_increment):
    new_increment()

    plt.scatter(axis_x, new_y(), marker="+", label="increment_" + str(inc))

plt.legend()
plt.show()
