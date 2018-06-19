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
from better_jieba import fenci_1,fenci_2
print(fenci_1('我爱北京天安门'))
print(fenci_2('我爱北京天安门'))
print(jieba.lcut('我爱北京天安门', HMM=False))
print(jieba.lcut('我爱北京天安门', HMM=True))

```

### License

MIT.
