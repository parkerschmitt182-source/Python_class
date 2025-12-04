import time

def gotimer():
     
    print("Hello how long would you like to set this timer for in seconds?")

    timer = int(input())
    print(f"starting {timer} sec timer")
     
    while timer != (0):
        time.sleep(1)
        
        print(timer)
        timer = timer - 1
gotimer()
while True:
    print("Times Up!")
    again = input("go again y/n")
    if again == ("y"):
        gotimer()

    else:
        import sys
        sys.exit()