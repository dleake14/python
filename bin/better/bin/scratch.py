import time, sys



# while True:
#     print(time.ctime(), end="\r")
#     #sys.stdout.write("\r" + time.ctime())
#     #sys.stdout.flush()
#     time.sleep(1)
print(sys.version)
for i in range(1, 100):
    print("attempt {0} of 100".format(i), end="\r", flush=True)
    time.sleep(.05)