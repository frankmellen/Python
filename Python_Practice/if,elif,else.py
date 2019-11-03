# a = 10
# b = 20
#
# if b > a:
#     print("hello, ok")
#
# if b < 30:
#     print("hello, ng")

# if
# elif
# else



# print(type(age))
# <class 'str'>

# age=input("hi, please enter your age: ")
# print(type(age))


age=int(input("hi, please enter your age: "))

if age<18:
    print("you can not smoke")

elif age==18:
    print("you are now 18, you can go to smoke")
elif age==100:
    print("hey!! you are 100 years old, please quit smoking")
else:
    print("you can smoke")
