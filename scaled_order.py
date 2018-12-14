#! /usr/bin/python3

""" To be defined by wojtekj """
__version__ = 0.02

# Import Built-Ins
import random
import math


class Cords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Order:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class ScaledOrder:
    def __init__(self, total_amount, order_count, price_low, price_high, amount_variance, price_variance, distribution):
        self.total_amount = total_amount
        self.order_count = order_count
        self.price_low = price_low
        self.price_high = price_high
        self.amount_variance = amount_variance
        self.price_variance = price_variance
        self.orders = []
        if type(distribution) is list:
            self.distribution = self.get_distribution(distribution)

        else:
            self.distribution = 1

        self.get_orders()

    def get_orders(self):
        orders = []
        order_size = self.total_amount / self.order_count
        sum = 0
        price_jump = (self.price_high - self.price_low) / \
            (self.order_count - 1)
        last_price = self.price_low
        print(self.order_count)
        for i in range(0, self.order_count):
            if i == 0:
                price = self.price_low

            elif i == self.order_count - 1:
                price = self.price_high

            else:
                rng = random.uniform(
                    0 - self.price_variance, self.price_variance)
                price = last_price + price_jump + \
                    (last_price + price_jump) * (rng / 100)
                price = math.floor(price)

            size = order_size * (self.distribution[i].y / 100)
            rng = random.randint(0 - self.amount_variance,
                                 self.amount_variance)
            # print(rng)
            size += size * (rng / 100)
            size = math.floor(size)
            # print(size)
            sum += size
            # print(price)
            last_price = price
            self.orders.append(Order(size, price))
            #print("suma " + str(sum))

        dif = self.total_amount - sum
        # print(dif)
        while dif > 0:
            #print("diff " + str(dif))
            chips = dif / self.order_count
            # print(chips)
            for i in range(0, self.order_count):
                self.orders[i].amount += chips * (self.distribution[i].y / 100)
                sum += chips * (self.distribution[i].y / 100)

            dif = self.total_amount - sum
            if dif < 0.0005:
                break

        sum = 0
        for order in self.orders:
            print("order size: " + str(format(order.amount, '.2f')) +
                  ", price: " + str(format(order.price, '.2f')))
            sum += order.amount

        print("sum: " + str(format(sum, '.2f')))

    def get_distribution(self, distribution):
        distribution_cords = []
        order_cords = []
        for i in range(0, 5):
            distribution_cords.append(Cords(i * 25, distribution[i]))

        for i in range(0, self.order_count):
            for j in range(0, 5):
                if distribution_cords[j].x > i * (100 / self.order_count):
                    start = distribution_cords[j - 1]
                    end = distribution_cords[j]
                    break

            order_x = i * (100 / (self.order_count - 1))
            # y=(((yB-yA)(x-xA))/(xB-xA))+yA
            order_y = (((end.y - start.y) * (order_x - start.x)) /
                       (end.x - start.x)) + start.y
            order_cords.append(Cords(order_x, order_y))
            # for oc in order_cords:
            #print(oc.x, " ", oc.y)

        return order_cords


# total_amount, order_count, price_low, price_high, amount_variance, price_variance, distribution
so = ScaledOrder(100, 11, 10, 100, 10, 10, [10, 80, 10, 40, 100])
print(so)
#so = ScaledOrder(10, 5, 10, 100, 5, 5, 1)
