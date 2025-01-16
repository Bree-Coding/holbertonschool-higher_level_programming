#!/usr/bin/python3
for x in range(97, 123):
    if x not in [101, 113]:
        print(f"{chr(x)}", end="")
