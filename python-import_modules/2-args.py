#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len = len(sys.argv) - 1
    i = 1
    if len == 0:
        print(f"{len} arguments.")
        sys.exit(0)
    else:
        print(f"{len} arguments:")
        while i <= len:
            print(f"{i}: " + sys.argv[i])

            i = i + 1
        sys.exit(0)
