import sys
import time

def ctm():
    print()
    while True:
        try:
            sys.stdout.write(f'\r{time.ctime()}    ')
            sys.stdout.flush()
        except KeyboardInterrupt:
            break
    print()

if __name__ == '__main__':
    ctm()