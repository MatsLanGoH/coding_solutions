# By! N'ary!


def chunks(line, length):
    for i in range(0, len(line), length):
        yield line[i:i+length]


def convertBinToChar(bins):
    output = ""
    for bin in bins:
        output += chr(int(bin, 2))
    return output

bin_string = input()
bins = [chunk for chunk in chunks(bin_string, 8)]
print(convertBinToChar(bins))
