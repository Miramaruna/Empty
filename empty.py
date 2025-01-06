import time


attempt = 0
try:
    while True:
        attempt += 1
        print(F"{attempt}: empty")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting...")