"""Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов 
сделал каждый ребенок, если известно, что Петя и Сережа 
сделали одинаковое количество журавликов, а Катя сделала 
в два раза больше журавликов, чем Петя и Сережа вместе?"""

S = int(input("кол-во журавликов сделанных детьми"))
a = (S//3)//2
b = a
c = 2*(a+b)
#print(a,b,c)
print('кол-во журавликов Пети', a)
print('кол-во журавликов Сережи', b)
print('кол-во журавликов Кати', c)

