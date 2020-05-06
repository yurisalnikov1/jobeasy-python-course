# string_1 = 'Python'
# result_1 =string_1[::-1]
# result_2 = string_2[5] + string_2[4]+string_2[3] + string_2[2]+string_2[1] + string_2[0]
# #
# print(result_1)
# print(result_2)

# string_3 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
# result_4 = string_3[::4]
# print(result_4)
#
# result_9 = range (0, 11)
# print(result_9)



# def function_1(number):
#     if number > 10:
#         print(100 - number)
#     else:
#         print (number * 10)
#
#
# number_1= 5
#
# function_1(number_1)

def temerature_convertor(fahrenheit_degree):
    print((fahrenheit_degree - 32) * 5 / 9)

degree_1=52
degree_2=85
temerature_convertor(degree_2)

# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

# def taxi_fare(distance):
#     print(round(distance * 1000 / 140 * 0.25 + 4, 2))
#
# taxi_fare(10)