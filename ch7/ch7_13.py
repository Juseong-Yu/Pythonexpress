str1 = input()
letter = sum(1 for x in str1 if x.isalpha())
digits = sum(1 for x in str1 if x.isdigit())
print("\"{}\" -> \"LETTERS\":{},\"DIGITS\"{}".format(str1,letter,digits))