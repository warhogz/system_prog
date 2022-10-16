# -*- coding: cp1251 -*-
import time
import threading
from threading import *
def cal_sqre(num):
    print(' Вычислить квадратный корень заданного числа')
    for n in num:
        time.sleep(0.3)
        print(' Квадратный : ', n * n)
def cal_cube(num):
    print(' Вычислить кубический корень заданного числа')
    for n in num:
        time.sleep(0.34)
        print(' Кубический : ', n * n *n)

ar = [4, 5, 6, 7, 2] # данный массив

t = time.time() # получиние общего времени для выполнения функций

th1 = threading.Thread(target=cal_sqre, args=(ar, ))
th2 = threading.Thread(target=cal_cube, args=(ar, ))
th1.start()
th2.start()
th1.join()
th2.join()
print(" Общее время, занимаемое потоками, составляет :", time.time() - t)
print(" Повторное выполнение основного потока")
print(" Поток 1 и поток 2 завершили свою работу.")

