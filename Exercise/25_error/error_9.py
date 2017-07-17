#coding: utf-8

import math, cmath
def safe_sqrt(x):
    try:
        num = math.sqrt(x)
    except ValueError:
        num = cmath.sqrt(x)
    return num


if __name__ == "__main__":
    x = float(raw_input('please input a number: '))
    print safe_sqrt(x)