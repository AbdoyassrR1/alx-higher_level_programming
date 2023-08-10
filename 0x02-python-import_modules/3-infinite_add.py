#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    args_len = len(sys.argv) - 1
    sum = 0

    if args_len == 0:
        print("0")
    else:
        for i in range(args_len):
            sum += int(args[i + 1])
        print(sum)
