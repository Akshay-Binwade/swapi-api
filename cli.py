import argparse

from task1 import task_one
from task2 import task_two
from task3 import task_three


if __name__ == '__main__':
    '''
    All the three tasks can be performed from here by just passing in the options.
    '''
    parser = argparse.ArgumentParser(description='Choose the task you like to perform.(task1, task2, task3)',
                                     epilog="You can just give argument as 1, 2 or 3")
    parser.add_argument("task", type=int, choices=[1,2,3], nargs="*")
    args = parser.parse_args()

    if args.task == 1:
        task_one()
    elif args.task == 2:
        task_two()
    elif args.task == 3:
        task_three()
    elif isinstance(args.task,list):
        if 1 in args.task:
            task_one()
        elif 2 in args.task:
            task_two()
        elif 3 in args.task:
            task_three()
        else:
            print("[ERROR]: Wrong choice...!!!\nPlease choose between (1,2,3)")
    else:
        print("[ERROR]: Wrong choice...!!!\nPlease choose between (1,2,3)")
    # print(args.task)


