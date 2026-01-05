yourtasks = []
def listmenu():
  print(''' menu:
          1. Add Task
          2. View tasks
          3. Delete tasks
          4. Exit
          ''')

listmenu()
choice = -1
while (choice != 4):
    choice = int(input("what do you want to perform. choose number from the menu above:  "))
    if (choice == 1):
        action = input("add task: ")
        yourtasks.append(action)

    elif (choice == 2):
      print("here's your list of all tasks you need to complete: ")
      for i, task in enumerate(yourtasks, start=1):
          print(f"{i}. {task}")

    elif(choice == 3):
        if not yourtasks:
            print("no item to delete")
        else:
            for i, task in enumerate(yourtasks, start=1):
                print(i, task)

            action=int(input("enter no of task you want to delete: "))

            if 1<=action<=len(yourtasks):
                removed=yourtasks.pop(action-1)
                print(f"deleted: {removed}")

            else:
                print("invalid number. out of list length")


    elif (choice == 4):
      break





