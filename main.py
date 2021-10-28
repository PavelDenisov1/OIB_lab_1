import mpmath
import random
import math
import re


def test_1():
    sum = 0
    for i in arr:
        if i == '0':
            sum = sum - 1
        else:
            sum = sum + 1
    s = 1 / math.sqrt(128) * sum
    p = math.erfc(s / math.sqrt(2))
    print("Test_1\n" + "Sn: " + str(s) + "\nP: " + str(p))


def test_2():
    sum = 0
    v = 0
    for i in arr:
        sum = sum + int(i)
    z = sum / 128
    if abs(z - 1 / 2) <= 2 / math.sqrt(128):
        for i in range(128 - 1):
            if arr[i] != arr[i + 1]:
                v += 1
    else:
        print(str(abs(z - 1 / 2)) + " > " + str(2 / math.sqrt(128)) + " P=0")
        return
    p = math.erfc(abs(v - 2 * 128 * z * (1 - z)) / (2 * math.sqrt(2 * 128) * z * (1 - z)))
    print("Test_2\n" + "z: " + str(z) + "\nV: " + str(v) + "\nP: " + str(p))


def test_3():
    v1, v2, v3, v4 = 0, 0, 0, 0
    begin = 0
    end = 8
    counter = 0
    while counter != 16:
        if re.findall(r'[1]{4}', arr[begin:end]):
            v4 += 1
        elif re.findall(r'[1]{3}', arr[begin:end]):
            v3 += 1
        elif re.findall(r'[1]{2}', arr[begin:end]):
            v2 += 1
        elif re.findall(r'[1]?', arr[begin:end]):
            v1 += 1
        begin += 8
        end += 8
        counter += 1
    print("Test_3\n" + "v1: " + str(v1) + "\nv2: " + str(v2) + "\nv3: " + str(v3) + "\nv4: " + str(v4))
    p1, p2, p3, p4 = 0.2148, 0.3672, 0.2305, 0.1875
    xi = ((v1 - 16 * p1) ** 2) / (16 * p1) + ((v2 - 16 * p2) ** 2) / (16 * p2) + ((v3 - 16 * p3) ** 2) / (16 * p3) + (
                (v4 - 16 * p4) ** 2) / (16 * p4)
    p = mpmath.gammainc(3 / 2, xi / 2)
    print("Xi^2: " + str(xi) + "\nP: " + str(p))


def split_out():
    begin = 0
    end = 8
    counter = 0
    while counter != 16:
        print(arr[begin:end])
        counter += 1
        begin += 8
        end += 8
    print("\n")


if __name__ == "__main__":
    # последовательность на пайтоне
    print("\nPython")
    arr = str(''.join(random.choice('0' + '1') for i in range(128)))
    split_out()
    test_1()
    print("\n")
    test_2()
    print("\n")
    test_3()
    # последовательность на джаве
    print("\nJava")
    arr = "10101000000000100101001100110101101001010100111101001001000101011010111111011101101101111111000101010010010011000010010110011110"
    split_out()
    test_1()
    print("\n")
    test_2()
    print("\n")
    test_3()
