from time import perf_counter

start = perf_counter()

# while True:
#
#     cal = input("Enter exit to Exit. \nenter two number and one operator seperated by space(2 * 5): ")
#     if cal == "exit": break
#     try:
#         print(eval(cal))
#     except:
#         print("enter numbers correctly")

"""
Second week 
"""

# Practice 1: Age in hours, minutes and seconds
# while True:
#     age = input("Enter age in years. \n To exit enter 0: ")
#     if age == "0": break
#     age = int(age)
#     hour = age * 365 * 24
#     minute = hour * 60
#     second = minute * 60
#     hour = format(hour, ",")
#     minute = format(minute, ",")
#     second = format(second, ",")
#
#     print(f"Hour: {hour} ..... Minute: {minute} ..... Second: {second}")


# Practice 2: Reverse number
# while True:
#     num = input("Enter a number: \n To exit enter 0: ")
#     if num == "0":
#         break
#     if not len(num) == 2:
#         print("Enter a two-digit number.")
#     else:
#         num = int(num)
#         dahgan = num % 10
#         yekan = num // 10
#         print(f"{dahgan * 10 + yekan}")


# # Practice 3:
# while True:
#     num = input("Enter a number: \n To exit enter 0: ")
#     if num == "0":
#         break
#     if not len(num) == 2:
#         print("Enter a two-digit number.")
#     else:
#         num = int(num)
#         yekan = num % 10
#         dahgan = num // 10
#         print(f"{dahgan ** yekan} --- {yekan ** dahgan}")

# # Practice 4: Matrix
# result = []
# rows_a = int(input("Rows number of matrix A: "))
# cols_a = int(input("columns number of matrix A: "))
#
# a = []
# print("numbers of matrix A: ")
# for i in range(rows_a):
#     row = list(map(int, input().split()))
#     a.append(row)
#
#
# rows_b = int(input("Rows number of matrix B: "))
# cols_b = int(input("columns number of matrix B:  "))
#
# b = []
# print("numbers of matrix B: ")
# for i in range(rows_b):
#     row = list(map(int, input().split()))
#     b.append(row)
#
#
# if cols_a != rows_b:
#     print("Error: Number of columns of matrix A should be equal to number of rows of matrix B")
# else:
#     result = [[0 for j in range(cols_b)] for i in range(rows_a)]
#
# for i in range(rows_a):
#     for j in range(cols_b):
#         for k in range(cols_a):
#             result[i][j] += a[i][k] * b[k][j]
#
# for row in result:
#     print(row)


""" Third week """


def strip(string):
    index_first_letter = 0
    index_last_letter = 0
    for x in range(len(string)):
        if string[-(x + 1)] != " ":
            index_last_letter = - (x + 1)
            break

    for x in range(len(string)):
        if string[x] != " ":
            index_first_letter = x
            break

    return string[index_first_letter:index_last_letter + 1]


end = perf_counter()
print(f"Program execution time: {end - start:.2f}")
