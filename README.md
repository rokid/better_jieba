# better_jieba

更好的结巴分词，对长词进行了二次分词。

### requirements

- Python3

### 安装

```bash
$ pip install jieba
```

### 使用

如下，与 `HMM=False` 的结果类似。

```py
print(jieba.lcut('丰田太省了', HMM=False))
print(jieba.lcut('我们中出了一个叛徒', HMM=False))
print(jieba.lcut('丰田太省了', HMM=True))
print(jieba.lcut('我们中出了一个叛徒', HMM=True))
```

### License

MIT.
