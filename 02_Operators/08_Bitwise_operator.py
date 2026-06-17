# Bitwise operators are used to compare (binary) numbers.

# AND (&) = sets each bit to 1 if both bits are 1.

print(6 & 3)

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

Firstly it converts number into binary:
6 = 0000000000000110
3 = 0000000000000011

2 = 0000000000000010

only 1 & 1 is 1, else it will be 0.
"""


# OR (|) = sets each bit to 1 if one of the bit two bits is 1.

print(6 | 3)


"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

Converting the number into binary:
6 = 0000000000000110
3 = 0000000000000011

7 = 0000000000000111

watch the value of 6 and 3. If there is 1 and other is 0, it gives the value 1. Else 0.
"""


# XOR (^) = sets each bit to 1 if only one of two bits is 1.

print(6 ^ 3)

"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0

Here number converts to 4 bit binary number:
6 = 0110
3 = 0011

5 = 0101
"""


# NOT (~) = Inverts all the bits

print(~3)


"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100         (flip the number)

Here is the process how it becomes -4:
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""