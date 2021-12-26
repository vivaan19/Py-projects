import sys

def helper_fun(line):
    line.strip()
    line = line.split()
    mes = " ".join(line[1:len(line)+1])
    prio = int(line[0])
    temp = [prio, mes]
    return temp
    
def reader_fun(par="task"):
    lst1 = []
    if par == "task":
        with open("Plans/task.txt", "r") as list_file:

            while True:
                line = list_file.readline()
                if not line:
                    break
                temp = helper_fun(line)
                lst1.append(temp)
            lst1.sort()

        return lst1
    
    else:
        with open("Plans/complete.txt", "r") as comp_file:
            line = comp_file.readlines()
        return line

def writer_fun(lst1, file = "task"):
    if file == "task":
        with open("Plans/task.txt", "w") as write_file:
            for i in range(len(lst1)):
                for j in range(0, 2):
                    write_file.write(f"{lst1[i][j]} ")
                write_file.write("\n")
    else:
        with open("Plans/complete.txt", "a") as append_file:
            append_file.write(f"{lst1[0][1]}\n")
            
def help():
    """./task help # Show usage"""
    var = """Usage :-
    $ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
    $ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
    $ ./task del INDEX            # Delete the incomplete item with the given index
    $ ./task done INDEX           # Mark the incomplete item with the given index as complete
    $ ./task help                 # Show usage
    $ ./task report               # Statistics"""

    sys.stdout.buffer.write(var.encode('utf8'))

def add(priority, message):
    """./task add 2 hello world # Add a new item with priority 2 and text "hello world" to the list"""

    with open("Plans/task.txt", "a") as write_file:
        write_file.write(f"{int(priority)} {message}\n")
    sys.stdout.buffer.write(f'Added task: "{message}" with priority {priority}'.encode('utf8'))


def ls():
    """./task ls # Show incomplete priority list items sorted by priority in ascending order"""

    lst1 = reader_fun()
    for i in range(len(lst1)):
        sys.stdout.buffer.write(f"{i+1}. {lst1[i][1]} {[lst1[i][0]]}\n".encode('utf8'))

def dele(index):
    """./task del INDEX # Delete the incomplete item with the given index"""

    lst1 = reader_fun()
    if index in [i for i in range(1,len(lst1)+1)]:
        lst1.pop(index-1)
        sys.stdout.buffer.write(f"Deleted item with index {index}\n".encode('utf8'))
        writer_fun(lst1)
    else:
        sys.stdout.buffer.write(f"Error: item with index {index} does not exist. Nothing deleted.\n".encode('utf8'))


def done(index):
    """./task done INDEX # Mark the incomplete item with the given index as complete"""

    lst = []
    lst1 = reader_fun()
    if index in [i for i in range(1,len(lst1)+1)]:
        com_line = lst1.pop(index-1)
        lst.append(com_line)
        sys.stdout.buffer.write(f"Marked item as done.\n".encode('utf8'))
        writer_fun(lst, "done")
        writer_fun(lst1)
    else:
        sys.stdout.buffer.write(f"Error: no incomplete item with index {index} exists.\n".encode('utf8'))


def report():
    """./task report # Statistics"""

    lst2 = reader_fun()
    print(f"Pending : {len(lst2)}")
    ls()
    print()
    lst1 = reader_fun("ntask")
    print(f"Completed: {len(lst1)}")
    for i in range(len(lst1)):
        print(f"{i+1}. {lst1[i].strip()}")

# main
var = """Usage :-
    $ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
    $ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
    $ ./task del INDEX            # Delete the incomplete item with the given index
    $ ./task done INDEX           # Mark the incomplete item with the given index as complete
    $ ./task help                 # Show usage
    $ ./task report               # Statistics"""

try:
    args = sys.argv
    args[1] = args[1].lower()
except IndexError:
    raise SystemExit(sys.stdout.buffer.write(var.encode('utf8')))

if args[1] == "help":
    help()

elif args[1] == "add":
    
    try:
        if int(args[2]) <=0:
            raise SystemExit("Priority should be always greater than or equal to 0")
        add(int(args[2]), args[3])

    except ValueError:
        raise SystemExit(f"{args[2]} -> should be a number")
    except IndexError:
        raise SystemExit("./task add <priority:int> '<message>'")

elif args[1] == "ls":
    ls()

elif args[1] == "del":
    try:
        dele(int(args[2]))
    except ValueError:
        raise SystemExit(f"{args[2]} -> should be a valid index number")
    except IndexError:
        raise SystemExit("./task del INDEX")

elif args[1] == "done":
    try:
        done(int(args[2]))
    except ValueError:
        raise SystemExit(f"{args[2]} -> should be a valid index number")
    except IndexError:
        raise SystemExit("./task done <INDEX>")


elif args[1] == "report":
    report()

else:
    raise SystemExit("Invalid Option") 