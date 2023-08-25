Input_Text = input("Enter text:")

#Total number of characters
Length_InTt = len(Input_Text)
s = 0
for x in Input_Text:
    if x == " ":
        s += 1
print(f"Number of characters:{Length_InTt-s}")

#Duplicate characters
dic = {}
for x in Input_Text:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
dic.pop(" ")
Du_chr = 0
for x in dic:
    if dic[x] >= 1:
        dic[x] -= 1
for x in dic:
    Du_chr += dic[x]
print(f"Total number of duplicate characters:{Du_chr}")

#Number of words
words = Input_Text.split()
print(f"Total number of words: {len(words)}")
print(words)

#Number of duplicate words
Du_rm_words = []
for x in words:
    if x not in Du_rm_words:
        Du_rm_words.append(x)
print(Du_rm_words)
print(f"Number of duplicate words: {len(words) - len(Du_rm_words)}")

#Reversed characters
Reversed_Statement = Input_Text[::-1]
print(f"Reversed_Statement:{Reversed_Statement}")

#Reversed words
Reversed_words = []
for x in words:
    Reversed_words.append(x[::-1])
for x in Reversed_words:
    print(x, end=' ')

#Reversed words statement
Reversed_words_statement = " ".join(Reversed_words)
print(f"\nReversed words statement:{Reversed_words_statement}")

#Duplicates removed reversed statement
Du_chr_rm_Reversed_words_statement = []
for x in Reversed_words_statement:
    if x not in Du_chr_rm_Reversed_words_statement or x == " ":
        Du_chr_rm_Reversed_words_statement.append(x)
Rslt_wtsp = "".join(Du_chr_rm_Reversed_words_statement)
Rslt_wtotsp = ""
for i in range(len(Rslt_wtsp)-1):
    if Rslt_wtsp[i] != Rslt_wtsp[i+1]:
        Rslt_wtotsp += Rslt_wtsp[i]
print(f"Duplicates removed reversed statement:{Rslt_wtotsp}")
