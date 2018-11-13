# coding=UTF-8
import jieba
import re

def isAllZh(s):# 判断是否全是中文
    if not ('\u4e00' <= s <= '\u9fa5'):
        return False
    return True


def better_cut(one_string, discover_new_word=False):
    one_string = re.sub(r'\s+', '', one_string)# 去掉所有空格
    final_result = []
    temp_list = jieba.lcut(one_string, HMM=discover_new_word)
    if discover_new_word==False:# HMM=False已实际使之缩小了不少粒度
        for word in temp_list:
            if isAllZh(word) == False:
                continue
            if len(word) > 4:
                jieba.del_word(word) # jieba.add_word(word,freq=0) 也行！
                final_result.extend(jieba.lcut(word, HMM=discover_new_word))
            else:
                final_result.append(word)
    else:
        for word in temp_list:
            if isAllZh(word)==False:
                continue
            # if len(word)==4: # 根据词频设置阈值
            #     print(word,jieba.get_FREQ(word))
            if jieba.get_FREQ(word)==None \
                    or (len(word)>1 and (jieba.get_FREQ(word)==None or jieba.get_FREQ(word)==0)) \
                    or len(word)>4 \
                    or (len(word)==4 and jieba.get_FREQ(word)!=None and jieba.get_FREQ(word)<100):
                jieba.del_word(word) # 强制 # jieba.add_word(word,freq=0) 也行！
                final_result.extend(jieba.lcut(word))
            else:
                final_result.append(word)
    return final_result


