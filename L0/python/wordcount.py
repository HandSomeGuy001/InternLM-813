import string

text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

def wordcount(text:str):
    # 去除字符串中的标点符号
    text = text.translate(str.maketrans('', '', '\'s'))
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 将文本转换为小写
    text = text.lower()
    # 按空格分割字符串得到单词列表
    words = text.split()
    # 创建一个字典来存储每个单词的计数
    word_count = {}
    
    # 遍历单词列表并更新字典中的计数
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

result = wordcount(text)
print(result)