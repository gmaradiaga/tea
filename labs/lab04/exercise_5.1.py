# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

total = 0
counter = 0
while True:
  try:
    input_str = input("Ingrese un número: ")
    if (input_str == 'done'):
      break
    else:
      total = total + int(input_str)
      counter = counter + 1
      average = total / counter
  except:
    print("Valor no es válido")
    continue
print("Total:", total)
print("Contador:", counter)
print("Promedio:", average)