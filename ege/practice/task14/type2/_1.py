#Арифметическое выражение переводят в N-систему счисления
#https://education.yandex.ru/ege/task/9ea2aa74-8d71-4f81-b955-55e997035e1e
from ege.EGE import *
num = 7*(512**120)-6*(64**100)+(8**210)-255
print(cs_conv(num, 8).count("0"))
