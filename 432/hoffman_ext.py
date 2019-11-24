+  # This is a program to compress a string using the Hoffman Algorithm
# Implemented using Python 3.6


def hoffman(string):
    k = 0
    coded = []
    letter_sorted = []
    f_sized = dict()
    frequency = dict()
    v_sized = dict()

    for letter in string:
        if letter in f_sized:
            frequency[letter] += 1
            continue
        else:
            f_sized[letter] = bin(k).rjust(5, "0")[2:].replace("b", "0")
            frequency[letter] = 1
            k += 1

    for letter, freq in frequency.items():
        letter_sorted.append(freq)
    letter_sorted.sort()

    for letter in letter_sorted:
        for key, value in frequency.items():
            if letter == value:
                letter_sorted[letter_sorted.index(letter)] = key

    v_sized[0] = 0
    v_sized[1] = 1
    for letter in letter_sorted:
        if letter.index() == 0 | 1:
            continue
        else:
            if letter.index

    for letter in string:
        coded.append(f_sized[letter])
        sorted(frequency)

    print("Fixed Size Encoding Table = ", f_sized, "\nFrequency Table = ", frequency, "\nFixed Size Encoding = ",
          "".join(coded), "\nSorted = ",
          letter_sorted)


hoffman("ABCCABBDDAECCBBAEDDCC")

# Author: Elizabeth Adeotun Adegbaju with Matric Number 16CG021378