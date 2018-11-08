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

from better_jieba import fenci
print(fenci('你手机号码是多少'))  # ['你', '手机', '号码', '是', '多少']

from recursive_cut import *
print(jieba.lcut("一二三四五六七八九十")) # ['一二三四五六七八九十']
print(fenci("一二三四五六七八九十")) # ['一二三四五', '六七八九十']
print(cut("一二三四五六七八九十")) # ['一二三', '四', '五', '六七', '八九十']

```

### License

MIT.
