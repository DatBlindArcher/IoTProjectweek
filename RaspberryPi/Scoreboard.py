import time
import sys
#import stomp

score = 0

try:
    for i in range(21):
        
        score = i
        
        sys.stdout.write("\r" + "[" + "+" * score + "-" * (20-score) + "] : " + str(int((score/20)*100)) + "%")
        time.sleep(1)
        sys.stdout.flush()
    print("    -    [Done]", end="")
    print()
except KeyboardInterrupt:
    print("[Stop]")
