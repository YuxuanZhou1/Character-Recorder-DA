import json
import re

def add(f):
    # open json files and load data
    data = open(f)
    a = json.load(data)

    # set dictionary for storing data
    person = {}
    x = input("Enter user ID:")
    person["ID"] = x
    person["Excel"] = {}
    person["CR"] = {}

    y = int(input("How many Excel mistakes: "))
    person["Excel"]["Mistake"] = y

    # if there are more than 1 mistake, them user should typing where they made mistake
    # and what is the correct answer
    if y >= 1:
        for i in range(1, y+1):
            person["Excel"]["Detail-" + str(i)] = {}
            z = input("Please input wrong answer: ")
            person["Excel"]["Detail-" + str(i)]["user's answer"] = z
            q = input("Please input correct answer: ")
            person["Excel"]["Detail-" + str(i)]["correct answer"] = q

    s = int(input("How many CR mistakes: "))
    person["CR"]["Mistake"] = s

    if s >= 1:
        for i in range(1, y+1):
            person["CR"]["Detail-" + str(i)] = {}
            z = input("Please input wrong answer: ")
            person["CR"]["Detail-" + str(i)]["user's answer"] = z
            q = input("Please input correct answer: ")
            person["CR"]["Detail-" + str(i)]["correct answer"] = q

    # print and add the new matriex into the dictionary (person)
    print(person)
    a['users'].append(person)

    # dump the dictionary into json files
    with open(f, 'w') as c:
        json.dump(a,  c, indent=4, separators = (',', ':'))

def delete(f):
    data = open(f)
    a = json.load(data)

    ID_name = input("Please input the ID you want to delete:")

    # search users Id and delete the whole array
    for i in range(len(a['users'])):
        if a['users'][i]['ID'] == ID_name:
            del a['users'][i]
            break

    # dump the new dictionary into the json files
    with open(f, 'w') as c:
        json.dump(a,  c, indent=4, separators = (',', ':'))


def show(f):
    data = open(f)
    a = json.load(data)

    how_show = input("Show all array, show one array or show array ID (Please type all, ID name or ID):")

    if how_show == str("all"):
    # show the current data in the files
        print(a)
    elif how_show.lower() == str("id"):
        id = []
        for i in range(len(a['users'])):
            id.append(a['users'][i]['ID'])
        print(id)
    else:
    # show the specific data based on the ID
        for i in range(len(a['users'])):
            if a['users'][i]['ID'] == how_show:
                print(a['users'][i])
                break


def main():
    file_name = "mistake.json"

    print("###Select your option (input number): ###")
    print("1> Add")
    print("2> Delete")
    print("3> Show")
    print("4> End" + "\r\n")

    choices = int(input())

    while choices < 5:
        if choices == 1:
            add(file_name)
            choices = int(input())

        elif choices == 2:
            delete(file_name)
            choices = int(input())

        elif choices == 3:
            show(file_name)
            choices = int(input())

    print("Thank you for your using!")

main()
