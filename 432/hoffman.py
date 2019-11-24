# This is a program to compress a string using the Hoffman Algorithm

def hoffman(string):
    i = 0
    binary = []
    unique = dict()
    freq = dict()

    for letter in string:
        if letter in unique:
            freq[letter] += 1
            continue
        else:
            unique[letter] = bin(i).rjust(5, "0")[2:].replace("b", "0")
            freq[letter] = 1
            i += 1

    for letter in string:
        binary.append(unique[letter])
        sorted(freq)

    print("Encoding Table = ", unique)
    print("Frequency Table = ", freq)
    print("Coded = ", "".join(binary))


hoffman("how are you doing?")
# Output  = 000001010011100101110011111001100001110010011010101111001101