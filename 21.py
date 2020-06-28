"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 
"""

def get_fib_nums_lst(n):
	"""
	n - количество чисел в списке 
	"""
  lst = [0, 1, 1]
  fib1, fib2 = 1, 1
  if n == 0:
    quit()
  if n == 1:
    print(lst[0])
  if n == 2:
    print(lst[0:2])
  else:
    for i in range(3, n):
      fib1, fib2 = fib2, fib1 + fib2
      lst.append(fib2)
  print(lst)
  return lst

n = int(input('Введите количество чисел: '))
get_fib_nums_lst(n)
