import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print("done")
    time.sleep(0.85)
    print("now done")

x = threading.Thread(target= func);

x.start();
print(threading.active_count())
time.sleep(2);
print("finally");