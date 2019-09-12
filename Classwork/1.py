import os
import sys
import math
import re


def input_date():
    P1 = input("Введите общее растояние >>")
    S1 = input("Введите среднюю скорость >>")
    T1 = input("Введите время работы >>")

    return P1, S1, T1

# def check_date():
#     try:
#         if "." in P1:
#             P1 = float(P1)
#         else:
#             P1 = int(arg1)
#     except ValueError:
#         raise CalcException("Error P1")
#
#     try:
#         if "." in S1:
#             S1 = float(S1)
#         else:
#             S1 = int(S1)
#     except ValueError:
#         raise CalcException("Error S1")
#
#     try:
#         if "." in T1:
#             T1 = float(T1)
#         else:
#             T1 = int(T1)
#     except ValueError:
#         raise CalcException("Error T1")

    return T1, P1, S1

def calc_func(P1, S1, T1):
    P2 = S1*T1
    P3 = P1/P2
    P4 = P3/365

    return P1, S1, T1, P3, P4

if __name__ == '__main__':
    P1, S1, T1 = input_date()
    # try:
    #     m_P1, m_S1, m_T1 = check_date(m_P1, m_S1, m_T1)
    # except CalcException as e:
    #     print(e)
    #     exit(1)
    try:
        input_date()

    Calc = calc_func()
    print(Calc)
