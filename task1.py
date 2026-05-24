todo_list = []
def add_task():
    task = (input("enter task"))
    todo_list.append({"task":task , "status":"pending"})
    print("TASK ADDED SUCCESSFULLY")

    
        
def view_task():
    print("your todo list:")
    if len(todo_list) == 0:
        print("no task")
    else:
        for index, task in enumerate(todo_list,1):
                 print(f"{index}.{task['task']}-{task['status']}")

            
def delete_task():
    if len(todo_list) == 0:
        print("LIST IS EMPTY !!")
    else:
        search_index = int(input("ENTER TASK NUMBER WHICH IS TO BE REMOVED")) -1
        if 0 <= search_index < len(todo_list):
            remove_task = todo_list.pop(search_index)
            print("task removed !")
        else:
            print("TASK NUMBER INALID")


def done_task():
    if len(todo_list) == 0:
        print("LIST IS EMPTY !!")
    else:
        search_index = int(input("ENTER TASK NUMBER WHICH IS TO BE REMOVED")) -1
        if 0 <= search_index < len(todo_list):
            todo_list[search_index]['status']= 'done'
            print("task marked done!")
        else:
            print("TASK NUMBER INVALID")
    
def menu():
    while(True):
     print("1. Add a new task")
     print("2. View all tasks")
     print("3.delete a task")
     print("4. mark a task as done")
     print("5. Exit")

     choice = input("enter choice")
     if choice == "1":
        add_task()
     elif choice == "2":
        view_task()
     elif choice == "3":
        delete_task()
     elif choice == "4":
        done_task()
     elif choice == "5":
        print("exiting appilication")
        break
     else:
        print("WRONG OPTION")
menu()
      
