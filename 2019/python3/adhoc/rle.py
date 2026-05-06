#!/usr/bin/env python3

def rle(s):
    output = []
    prev_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            if count == 1:
                #output.append(prev_char)
                pass
            else:
                output.append(str(count))
            output.append(prev_char)

            count = 1
            prev_char = s[i]

    # Add the last one here.
    if count > 1:
        output.append(str(count))
    output.append(prev_char)

    print(output)

rle("BAAACBB")
rle("AAAAAAAAAAAA")

