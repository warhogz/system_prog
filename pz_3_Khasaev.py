# -*- coding: cp1251 -*-
import time
import threading
from threading import *
print(" �������� �����: 4 5 6 7 2")
def cal_sqre(num):
    print(' ��������� ���������� ������ �������� �����')
    for n in num:
        time.sleep(0.3)
        print(' ���������� : ', n * n)
def cal_cube(num):
    print(' ��������� ���������� ������ �������� �����')
    for n in num:
        time.sleep(0.34)
        print(' ���������� : ', n * n *n)

ar = [4, 5, 6, 7, 2] # ������ ������

t = time.time() # ��������� ������ ������� ��� ���������� �������

th1 = threading.Thread(target=cal_sqre, args=(ar, ))
th2 = threading.Thread(target=cal_cube, args=(ar, ))
th1.start()
th2.start()
th1.join()
th2.join()
print(" ����� �����, ���������� ��������, ���������� :", time.time() - t)
print(" ��������� ���������� ��������� ������")
print(" ����� 1 � ����� 2 ��������� ���� ������.")

