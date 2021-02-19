
#simple word counting
sentence = input("what's on your mind today? ")
count = 0
for character in sentence:
    if character == " ":
        count = count + 1
total = count + 1
print("oh nice, you just told me what's on your mind in " , total , " words!")
