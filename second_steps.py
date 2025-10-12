# print("----------------------------------")
# friends = ["John","Kevin","Durant","Oscar","Bob"]
# others = ["Fatih", 2 , False] #Thats also OK
# print(friends)
# print(friends[1])
# print(friends[-1])
# print(friends[1:])
# print(friends[:-1])
# print(friends[2:-1])
# friends[1] = "Emir"
# print(friends[1])
# print("----------------------------------")


# print("----------------------------------")
# friends = ["John","Kevin","Durant","Oscar","Bob"]
# lucky_numbers = [1,2,3,4,5,6,7,8,9]
# # lucky_numbers.extend(friends)
# print(lucky_numbers)
# friends.append("Joe")
# print(friends)
# friends.insert(1,"Fatih")
# print(friends)
# friends.remove("Durant")
# print(friends)
# # friends.clear()
# # print(friends)
# friends.pop()
# print(friends)
# print(friends.index("Oscar"))
# friends.append("Bob")
# print(friends.count("Bob"))
# friends.sort()
# print(friends)
# lucky_numbers.reverse()
# print(lucky_numbers)
# numbers = lucky_numbers.copy()
# print(numbers)
# print("----------------------------------")


# print("----------------------------------")
# coordinates = ((9,5),(2,3))
# print(coordinates)
# print("----------------------------------")

# print("----------------------------------")
# def sayhi(name, age = 0):
#     print(f"Hello " +name + "!" +" You are " + str(age) + " years old.")
#
# sayhi("Mike", age=18)
# sayhi("Steve", age=25)
# print("----------------------------------")

# print("----------------------------------")
# def cube(num):
#     return num * num * num
#
# print(cube(3))
# def topla(a, b):
#     result = a + b
#     print(result)
#
# a = topla(4, 5)
# print(a) #!!!!!!!!!!! if there isnt return in the function you cant save the result
# print("----------------------------------")

print("----------------------------------")

is_male = True
is_tall = False

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are not male or tall")

if is_male and is_tall:
    print("You are tall male")
elif is_male and not is_tall:
    print("You are short male")
elif not is_male and is_tall:
    print("You are long female")
else:
    print("You are not male or tall or both")