import time
import random

def countdown():
    sec = random.randint(3,8)
    print(f'Это займет {sec} секунд.')
    for i in range(sec):
        time.sleep(1)
        print(i)
        i-=1