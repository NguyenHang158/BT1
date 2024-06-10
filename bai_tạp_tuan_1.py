# -*- coding: utf-8 -*-
"""Bai_Tạp_Tuan_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12-TTJLyb2NiylyE562NtA-rL7251WLIA
"""

def BT1(tp,fp,fn):
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        if not isinstance(tp, int):
            print("tp must be int")
        if not isinstance(fp, int):
            print("fp must be int")
        if not isinstance(fn, int):
            print("fn must be int")
        return

    if tp<=0 or fp<=0 or fn<=0:
        print("tp and fp and fn must be greater than zero")
        return

    P = tp/(tp+fp)
    R = tp/(tp+fn)
    F1_score = 2*P*R/(P+R)

    print("P =", P)
    print("R =", R)
    print("F1-score =", F1_score)

BT1(1,3,2)

"""Bài 2"""

import math
def is_number(n):
    try:
        float(n)

    except ValueError:
        return False
    return True

import math
def calc_sig(x):
    return 1/(1+math.e**(-x))

import math
def calc_relu(x):
    if x>0:
        return x
    else:
        return 0

import math
alpha = 0.01
def calc_elu(x):
    if x>0:
        return x
    else:
        return alpha*(math.e**x - 1)

def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return calc_sig(x)
    elif act_name == 'relu':
        return calc_relu(x)
    elif act_name == 'elu':
        return calc_elu(x)
    else:
        print("Invalid activation function")

def BT2():
    x = input("Input x =  ")
    if not is_number(x):
        print("x must be number")
        return

    act_name = input('Input activaton Function (sigmoid|relu|elu): ')
    x = float(x)
    result = calc_activation_func(x, act_name)
    if result is None:
        print(f'{act_name} is not supportted')
    else:
        print(f'{act_name}: f({x}) = {result}')

BT2()

import math
def is_number(n):
    try:
        float(n)

    except ValueError:
        return False
    return True

assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))

import math
def calc_sig(x):
    return 1/(1+math.e**(-x))

assert round ( calc_sig (3) , 2) ==0.95
print ( round ( calc_sig (2) , 2) )

import math
alpha = 0.01
def calc_elu(x):
    if x>0:
        return x
    else:
        return alpha*(math.e**x - 1)
assert round ( calc_elu (1) ) ==1
print ( round ( calc_elu ( -1) , 2) )

"""Bài 3"""

import random
import math

def calc_ae(y, y_hat):
    return abs(y-y_hat)

y = 1
y_hat = 6
assert calc_ae(y, y_hat)==5

def calc_se(y, y_hat):
    return (y-y_hat)**2

y = 4
y_hat = 2
assert calc_se(y, y_hat)==4

def exercise3():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    loss_name = input('Input loss name: ')

    final_loss = 0
    num_samples = int(num_samples)
    for i in range(num_samples):
        pred_sample = random.uniform(0,10)
        target_sample = random.uniform(0,10)

        if loss_name == 'MAE':
            loss = calc_ae(pred_sample, target_sample)
        elif loss_name == 'MSE' or loss_name == 'RMSE':
            loss = calc_se(pred_sample, target_sample)

        final_loss += loss
        print(f'loss_name: {loss_name}, sample: {i}: pred: {pred_sample} target: {target_sample} loss: {loss}')

    final_loss /= num_samples
    if loss_name == 'RMSE':
        final_loss = math.sqrt(final_loss)
    print(f'{loss_name}: {final_loss}')

exercise3()

"""Bài 4"""

def approx_sin(x, n):
    return sum([(-1)**i * x**(2*i+1) / math.factorial(2*i+1) for i in range(n)])
assert round(approx_sin(x=1, n=10), 4)==0.8415

print ( round ( approx_sin ( x =3.14 , n =10) , 4) )

def approx_cos(x, n):
    return sum([(-1)**i * x**(2*i) / math.factorial(2*i) for i in range(n)])
assert round(approx_cos(x=1, n=10), 2)==0.54

print ( round ( approx_cos ( x =3.14 , n =10) , 2) )

def approx_sinh(x, n):
    return sum([x**(2*i+1) / math.factorial(2*i+1) for i in range(n)])
assert round(approx_sinh(x=1, n=10), 2)==1.18

print ( round ( approx_sinh ( x =3.14 , n =10) , 2) )

def approx_cosh(x, n):
    return sum([x**(2*i) / math.factorial(2*i) for i in range(n)])
assert round(approx_cosh(x=1, n=10), 2)==1.54

print ( round ( approx_cosh ( x =3.14 , n =10) , 2) )

"""Bài 5"""

def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/ n )
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1)