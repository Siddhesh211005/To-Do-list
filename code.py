task = []
print ("hello there")
print("------------------------------------")

def Addtask():
    a=input ("what would you like to add?:")
    task.append(a)
    print("task has been added to list")
def Display():
    print("your To-Do list is:")
    print("",task)
while True:
    print("welcome")
    print("1.Add tasks")
    print("2.display tasks")
    choice =input("add/display?:")
    if(choice =="1"):
        Addtask()
    elif(choice=="2"):
        Display()
    else:
        break
