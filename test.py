import json

def add(f):
    data = open(f)
    a = json.load(data)

    person = {}
    x = input("Enter user ID:")
    person["ID"] = x
    person["Excel"] = {}

    y = int(input("How many Excel mistakes: "))
    person["Excel"]["Mistake"] = y

    if y >= 1:
        for i in range(1, y+1):
            person["Excel"]["Detail-" + str(i)] = {}
            z = input("Please input wrong answer: ")
            person["Excel"]["Detail-" + str(i)]["user's answer"] = z
            q = input("Please input correct answer: ")
            person["Excel"]["Detail-" + str(i)]["correct answer"] = q        

    print(person)

    a['users'].append(person)

    with open(f, 'w') as c:
        json.dump(a,  c, indent=4, separators = (',', ':'))

def delete(f):
    data = open(f)
    a = json.load(data)

    ID_name = input("Please input the ID you want to delete:")

    for i in range(len(a['users'])):
        if a['users'][i]['ID'] == ID_name:
            del a['users'][i]
            break
        else:
            print("we don't have this ID")

    with open(f, 'w') as c:
        json.dump(a,  c, indent=4, separators = (',', ':'))


def show(f):
    data = open(f)
    a = json.load(data)
    print(a)


def main():
    file_name = "1.json"

    print("###Select your option (input number): ###")
    print("1> Add")
    print("2> Delete")
    print("3> Show")
    print("4> End" + "\r\n")

    choices = int(input())

    while choices < 4:
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
