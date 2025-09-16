import time
def logger(args, response):
    timeNow = time.ctime()
    logs = [str(timeNow),"\n", str(args), "\n", str(response), "\n", "-------------------------------------------------\n"]
    print("logs\n",logs)
    with open("logs.txt", "a") as file:
        file.writelines(logs)