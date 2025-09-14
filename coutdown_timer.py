import time
while True:
    try:
        seconds=int(input("Enter your time in seconds: "))
        if seconds<1:
            print("Please enter a member greater than 0")
        break
    except ValueError:
        print("Invalid input, please enter a whole number")
print("\n Timer starts")
for remaining in range(seconds,0,-1):
    mins,secs=divmod(remaining,60)
    time_format=f"{mins:02}:{secs:02}"
    print(f"Time left:{time_format}",end="\r")
    time.sleep(1)
print("\n Time's up, take a break or move on to  the next task")
print("\a")    