import time
import os

total_breaks = 3
break_count = 0


print("This program started on"+time.ctime())
while(break_count < total_breaks):
	time.sleep(10)
	os.startfile('Johanna.mp3')
	break_count = break_count + 1