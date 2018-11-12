# better_jieba

更好的结巴分词，对长词进行了二次分词。

### requirements

- Python3 / Python2
- jieba

### 安装

```bash
$ pip install jieba
$ git clone git@github.com:Rokid/better_jieba.git
```

### 使用

```py
import jieba
print(jieba.lcut('你手机号码是多少')) # ['你', '手机号码', '是', '多少']

from better_cut import *
print(better_cut('你手机号码是多少'))  # ['你', '手机', '号码', '是', '多少']

from recursive_cut import *
print(jieba.lcut("一二三四五六七八九十")) # ['一二三四五六七八九十']
print(better_cut("一二三四五六七八九十")) # ['一二三四五', '六七八九十']
print(recursive_cut("一二三四五六七八九十")) # ['一二三', '四', '五', '六七', '八九十']

```

### 注意

对同一句话重复调用，结果不一致，因为前面的调用会改变后面调用时的词典

### License

MIT.
