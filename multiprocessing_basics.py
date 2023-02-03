import os

# new interface with good abstraction also covers with threading

from multiprocessing import Process

pid_list = []

# basic fork() way for multiprogramming
# it spawns a new processes and split into with seperate interpreter
# that is runs twice i.e tow diffferent processes
# def main():
#     pid_list.append(os.getpid())
#     child_pid = os.fork()
#
#     if child_pid == 0:
#         pid_list.append(os.getpid())
#         print()
#         print("CHLD: hey ,i am the child process")
#         print("CHLD: all the pids i know %s"%pid_list)
#     else:
#         pid_list.append(os.getpid())
#         print()
#         print("PRNT: hey i am the parent process" )
#         print("PRNT: the child pid ia %d"%child_pid)
#         print("PRNT: all the pids i know %s"%pid_list)


def work(identifier):
    print(f"Hey, i am the process",f"{identifier}, pid: {os.getpid()}")

def new_main():
    processes = [
            Process(target=work,args=(number,))
            for number in range(5)
        ]
    for process in processes:
        process.start()

    while processes:
        processes.pop().join()


if __name__=="__main__":
    # main()
    new_main()
