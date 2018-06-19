Python3
```
pip install jieba
```
原理 是 对 一些 词 比如 长词 等 进行 二 次 分词

事实上和HMM=False的结果貌似差不多
```
print(jieba.lcut('丰田太省了', HMM=False))
print(jieba.lcut('我们中出了一个叛徒', HMM=False))
print(jieba.lcut('丰田太省了', HMM=True))
print(jieba.lcut('我们中出了一个叛徒', HMM=True))
```
