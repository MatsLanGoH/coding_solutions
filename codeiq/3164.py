# coding: utf-8
# Compare 2 strings for deviations
# cf. Levenshtein distance


def stringCounter(str_a, str_b):
    count = 0

    if (len(str_a) != len(str_b)):
        count += abs(len(str_a) - len(str_b)) * 2

    for a, b in zip(str_a, str_b):
        resulta, resultb = a == b, a.upper() == b.upper()
        print(resulta, resultb)
        if not resulta:
            count += 1
        if not resultb:
            count += 1

    for i in (max(str_a, str_b)):
        print(i)

    print("Result: {}".format(count))
    print


str_a = "abcde"
str_b = "abcdE"
stringCounter(str_a, str_b)

str_a = "abcdY"
str_b = "abcde"
stringCounter(str_a, str_b)

str_a = "abcd"
str_b = "abcde"
stringCounter(str_a, str_b)

str_a = "abcde"
str_b = "abde"
stringCounter(str_a, str_b)

str_a = "abcde"
str_b = "abcde"
stringCounter(str_a, str_b)
