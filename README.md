# better_jieba

更好的结巴分词，对长词进行了二次分词。

### requirements

- Python3

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

```

### License

MIT.
