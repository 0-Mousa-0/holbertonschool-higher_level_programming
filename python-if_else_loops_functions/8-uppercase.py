#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - 32) if ord(c) in range(97, 123) else c), end="")
    print()

      #  if ord(c) in range(97, 123):
     #       print("{}".format(chr(ord(c) - 32)), end="")
    #    else:
   #         print("{}".format(chr(ord(c))), end="")

    #print("")
