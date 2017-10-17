import re
import jieba
 
FILE = "valid.en-zh.zh.sgm"

# 提取纯文本
output = open("text.txt", "w", encoding='utf8')

with open(FILE, 'r', encoding='utf8') as f:
    lino = 0
    for line in f:
        lino += 1
        try:
            res = re.findall(r'<seg id=".*">(.*?)<\/seg>', line)
            # 分词
            words = jieba.cut(res[0].strip())
            print(' '.join(words), file=output)
        except:
            print(lino)
            print(line)

output.close()


