
from modifying_list import ArrayList
List = ArrayList()
Location = int()
name = str()
state = True
while state:
    state = False
    print("1-Add name to list")
    print("2-Delete name from list")
    print("3-Remove name from list at location")
    print("4-Add name to list at location")
    print("5-Find location name in list")
    print("6-Search for name in list")
    print("7-Number of names in list")
    print("8-First name in list")
    print("9-Last name in list")
    print("10-Show list")
    print("11-Clear list")
    print("0-Exit")
    print("----------------------------------")
    number = int(input("Enter number:"))

    if number == 1:
        name = input("Enter name: ")
        List.add(name)
        state = True
    if number == 2:
        name = input("Enter name: ")
        List.remove(name)
        state = True
    if number == 3:
        name = input("Enter name: ")
        List.remove_at(name)
        state = True
    if number == 4:
        name = input("Enter name: ")
        Location = int(input("Enter location: "))
        List.insert(name,Location)
        state = True
    if number == 5:
        name = input("Enter name: ")
        Location = List.find(name)
        print("Location: ", Location)
        state = True
    if number == 6:
        name = input("Enter name: ")
        Location = (List.find(name) + 1)
        if Location != -1:
            print("Name found at location: ", Location)
        else:
            print("Name not found.")
        state = True
    if number == 7:
        print("Number of names in list: ", List.length)
        state = True
    if number == 8:
        print("First name in list: ", List.first())
        state = True
    if number == 9:
        print("Last name in list: ", List.last())
        state = True
    if number == 10:
        print(List)
        state = True
    if number == 11:
        List.clear()
        state = True
    if number == 0:
        state = False









