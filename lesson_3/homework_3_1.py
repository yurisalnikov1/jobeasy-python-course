# Input two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

if first_number > second_number:
    result_1 == first_number
else:
    result_1 == second_number


# Input a number that is under 20 in number_1 variable. If this number is 20 or
# # higher save “Too high” text to result_2, otherwise save “Thank you”.
if number_1 >= 20:
    result_2 == 'Too High'
else:
    result_2 == 'Thank you'



# Input your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = Yuri
last_name = Salnikov
if len(first_name) <5
    result_3 == f'{first_name}{last_name}'.upper()
else:
    result_3 == f'{first_name}'.lower()


# Input a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.


if 10<= number_2 <=20:
    result_4 == f'Thank you'
else:
    result_4 == f'Incorrect answer'


# Input your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = 18
if age >=18:
    result_5 == f'You can vote'
elif age =17:
    result_5 == f'You can learn to drive'
elif age =16:
    result_5 == f'You can buy a lottery ticket'
else:
    result_5 == f'You can go Trick-or-Treating'

# Input a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, July, August, September, October, November, December)
# Write answer in result_decade in lower case

month = 1
result_month = 'January'
if month =1:
    result_month == f'January'.lower()
if month =2:
    result_month == f'February'.lower()
if month =3:
    result_month == f'March'.lower()
if month =4:
    result_month == f'April'.lower()
if month =5:
    result_month == f'May'.lower()
if month =6:
    result_month == f'June'.lower()
if month =7:
    result_month == f'July'.lower()
if month =8:
    result_month == f'August'.lower()
if month =9:
    result_month == f'September'.lower()
if month =10:
    result_month == f'October'.lower()
if month =11:
    result_month == f'November'.lower()
if month =12:
    result_month == f'December'.lower()
if month >12:
    result_month == f'Please select a value between 1 and 12'