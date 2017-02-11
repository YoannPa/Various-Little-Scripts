#Chronometer Program Execution :
import time
start_time = time.time()
#Insert Function Here:
for i in range(100):
    print i
print("--- {:f} seconds ---".format(time.time() - start_time))
