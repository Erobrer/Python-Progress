# print("------------------------------------")
# friends = ["Kim", "Kevin", "Durant", "Oscar", "Bob"]
#
# for friend in friends:
#     print(friend)
#
# for index in range(len(friends)):
#     print(friends[index])
#
# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("Not first iteration")
# print("------------------------------------")

# print("------------------------------------")
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(3,4))
#
# print("------------------------------------")
#
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# print(number_grid[2][0])
#
# for row in number_grid:
#     for col in row:
#         print(col)
#
# print("------------------------------------")

# print("------------------------------------")
#
# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()
#
# print("------------------------------------")

print("------------------------------------")
employee_file = open("employees.txt", "a")
employee_file.write("\n" + input("Enter a new employee name: "))
employee_file.close()
print("------------------------------------")
