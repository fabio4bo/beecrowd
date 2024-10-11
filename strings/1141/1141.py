"""
BEE 1141 - Growing Strings - Level 10 - Strings
"""

while True:
    try:
        n = int(input())

        if n == 0:
            break
        list_words = []
        for i in range(n):
            list_words.append(input())
        
        list_words.sort(key=len)

        miter = iter(list_words)
        count_list = []

        for it in miter:
            smaller = it
            count = 0
            for i in list_words:
                if i.find(smaller) >= 0 and i.find(smaller) + len(smaller) <= len(i):
                    count+=1
                    smaller = i
            count_list.append(count)
            list_words.remove(smaller)
        print(max(count_list))
    except EOFError:  # eof
        break
