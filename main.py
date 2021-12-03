# Brianna Berent
# This program will combine all my computer programming knowledge
print("Hello, my name is Brianna Berent")
print("My email is beberent4492", end='@')
print("eagle.fgcu.edu")
# The end-'@' ends the previous statement with a @ and begins the next
# statement
school_Name = "Florida Gulf Coast University"
print("I go to", school_Name)
# schoolName assigns the statement "Florida Gulf Coast University" to the
weight = (221 / 2)
# The / divides 221 by 2 and keeps the decimals to give my weight
print("I weigh", weight, "pounds.")
height_Feet = (10 // 2)
# The // divides 10 by 2 and ignores the remainder to give my height
height_Inch = (19 % 5)
# The % gives only the remainder of 19 divided by 5 to give my height
print("I am", height_Feet, "feet", height_Inch, "inches tall.")
print('I was born on 07', '31', '2003', sep='-')
# The sep='-' seperates each number with a -
location_Birth = "Boca Raton Florida"
print("I was born in", location_Birth)
location_Moved = "Saint Cloud Florida"
age_Moved = (5 - 2)
# The - subtracts 2 from 5 to give how old i was when I moved
print('I moved to', location_Moved, "when I was", age_Moved, "years old.")
sibling = "sister"
print('I have one', sibling, "and no brothers.")
sister_Name = "Heather"
sister_Age = (10 + 4)
print("Her name is", sister_Name, "and she is", sister_Age, "years old.")
# The + function adds 10 and 4 to give my sisters age
high_School = "Saint Cloud High School."
print('I went to', high_School)
graduation_Rank = (8 ** 2)
class_Size = (4 * 139)
print('I graduated ranked', graduation_Rank, 'of', class_Size, "students.")
# The ** put 8 to the power of 2 to give my class rank
# the * multiplied 4 by 139 to give my class size
activityA = "swimming ,"
activityB = "student government,"
activityC = "early childhood education program."
num_Activity = (4 - 1)
Other_Num_Activity = (3 + 2)
print("In high school I participated in", activityA, activityB, "and the",
      activityC)
print("I also participated in", num_Activity, "or", Other_Num_Activity,
      "other activities at", high_School)
# numActivity is the number of other clubs/sports i was in that i did not
# list otherNumActivity is the second number to give a range of numbers
# since i am not sure exactly how many
print("This is just a few facts about me")
print("I hope you enjoyed:)")
print("Thank you!" * 5)
# Thank you*5 is used to print the statement five times

# now I will show how to use different operators by
# allowing the user to enter values
# this will be done in different parts  \

# part one will demonstrate how to use if else statements
# PART ONE
print("PART ONE")
grade = float(input("Enter grade between 0 and 100:  "))
if grade >= 95:
    print("Amazing!!")
elif grade >= 90:
    print("Great!")
elif grade >= 85:
    print("Good")
elif grade >= 80:
    print("Okay")
elif grade >= 75:
    print("Study!!!")
elif grade <= 70:
    print("Do better :(")
# the if statement prints the word amazing if the entered value meets the
# conditions the elif prints the other words if the entered value does not
# meet the previous condition

print("PART TWO")
# Part two will demonstrate how to use a for loop
# PART TWO
# this for lopp will print every letter in my name until it lands on an "n"
for letter in 'Brianna':
    if letter == 'n':
        break
    print(letter)

print("PART THREE")
# part three will demonstrate how to use a while loop
# PART THREE
# this loop keeps on printing numbers until it prints one larger than 5
value = 0
while value <= 5:
    print(value, "is smaller than 5")
    value += 1
else:
    print(value, "is not smaller than 5")
# else is executed once the while loop is false

print("PART FOUR")
# part four fill use the def which is defining a function
# PART FOUR
number = int(input('Enter a number to square: '))


def square(x):
    return x * x


print(square(number))
# the function name is followed by ()
# the function body is started by :
# inside the function body the return statement says what will be returned

# part five will use the "not" function to say true if the entered number
# is greater than 10 and false if it is less
print("PART FIVE")
# PART FIVE
print("Guess my number")
x = int(input("Enter a number between 1 and 10: "))
if not x == 3:
    print("Wrong:(")

else:
    print("Correct!")

# part six will use the in range to count to my age using the range 0 to 19
# PART SIX
# i am 18 years olds
print("PART SIX")
print("Count to my age:)")
for i in range(0, 19, 1):
    print(i, end=", ")
