from time import time
import sys

def main():
    total = 0
    start = time()
    number_list = [x for x in range(1,50000001)]
    for number in number_list:
        total += number
    print(total)
    end = time()
    print("Execute Time:%.3fs" % (end-start))

if __name__ == "__main__":
    main()