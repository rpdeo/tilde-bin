#!/usr/bin/env python2

"""This file implements a ROT-N algorithm for scrambling/unscrambling ascii
text, only alphabets are scrambled. N can be anything.

Only considers lower-case alphabets for now.
"""

import sys

def getblock(n):
    chars = 'abcdefghijklmnopqrstuvwxyz,'
    nc = len(chars)
    times,rem = (nc / n, nc % n)
    # print n, times, rem, n-rem
    if rem == 0:
        j = 0
        for i in range(times):
            yield chars[j:j+n]
            j = j + n
    else:
        j = 0
        for i in range(times):
            yield chars[j:j+n]
            j = j + n
        yield chars[j:j+rem]+chars[:(n-rem)]


content = str(sys.stdin.read().strip())
n_rot = int(sys.argv[1])

transpose_blocks = []
gen_blocks = getblock(n_rot)
for block in gen_blocks:
    transpose_blocks.append(block)

translated = []
for char in content:
    for i, block in enumerate(transpose_blocks):
        from_block = block
        if i < len(transpose_blocks)/2:
            to_block = transpose_blocks[i + len(transpose_blocks)/2]
        else:
            to_block = transpose_blocks[i - len(transpose_blocks)/2]

        if char in from_block:
            translated.append(to_block[from_block.index(char)])
            break
        elif char in to_block:
            translated.append(from_block[to_block.index(char)])
            break
        else:
            translated.append(char)
            break

print ''.join(translated)
