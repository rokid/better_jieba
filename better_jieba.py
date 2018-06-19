# coding=UTF-8
import jieba

# 判断是否全是中文
def isAllZh(s):
    for c in s:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True

# HMM=True
def fenci_1(one_string):
    for _ in range(len(one_string)): # 去掉所有空格
        try:
            one_string=one_string.replace(" ","")
        except:
            break
    final_result = []
    temp_list = jieba.lcut(one_string)
    for word in temp_list:
        if isAllZh(word)==False:
            continue
        # if len(word)==3: # 根据词频设置阈值
        #     print(word,jieba.get_FREQ(word))
        if jieba.get_FREQ(word)==None \
            or (len(word)>1 and (jieba.get_FREQ(word)==None or jieba.get_FREQ(word)==0)) \
            or len(word)>3 \
            or (len(word)==3 and jieba.get_FREQ(word)!=None and jieba.get_FREQ(word)<100):
            jieba.del_word(word) # 强制
            final_result.extend(jieba.lcut(word))
        else:
            final_result.append(word)
    return final_result

# HMM=False已实际使之缩小了不少粒度
def fenci_2(one_string):
    for _ in range(len(one_string)):
        try:
            one_string = one_string.replace(" ", "")
        except:
            break
    temp_list = jieba.lcut(one_string,HMM=False)
    final_result = []
    for word in temp_list:
        if isAllZh(word) == False:
            continue
        if len(word) > 3:
            jieba.del_word(word)
            final_result.extend(jieba.lcut(word,HMM=False))
        else:
            final_result.append(word)
    return final_result
