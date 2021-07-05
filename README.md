# chinese-vocab-cluster
This repo contains a Python script to divide the 现代汉语常用词表 (list of frequently used modern Chinese vocabulary) into groups of 20 words or less. If you are an intermediate student of Chinese and you want to continue studying new words daily, but aren't sure where to find new words to study, then this repo is ideally suited for you.

本仓库的Python脚本的功能是将“现代汉语常用词表”分别为至多20个词汇的子团。如果你是一位认真的中级中文学生，而你希望能够继续天天学习新的词汇，但你不知道哪里找新的词汇，那么本仓库完全适合你的要求。

## Dependencies | 
* [FastText](https://fasttext.cc/docs/en/support.html)
* [SciPy](https://docs.scipy.org/doc/scipy/reference/)
* [NumPy](https://numpy.org/doc/)
* [Python 3.6+](https://www.python.org/)

## References | 参考资料

### FastText
* [FastText word vectors | FastText的词向量（英文）](https://fasttext.cc/docs/en/crawl-vectors.html)

### SciKit
* [SciKit clustering algorithms overview | SciKit聚类算法要略](https://scikit-learn.org/stable/modules/clustering.html)
* [SciKit K-Means clustering API documentation | SciKit K均值聚类算法的应用程序接口文件](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans)

### Chinese Language Resources | 学习中文的资料
* [Frequently used Chinese words | 现代汉语常用词表](https://gist.github.com/indiejoseph/eae09c673460aa0b56db)
* [Pleco Chinese-English dictionary app | Pleco中英词典APP](https://www.pleco.com/)
* [Anki flashcards app with spaced repetition | Anki记忆卡片的APP：使用间隔重复](https://apps.ankiweb.net/)

## How to Use | 如何使用本仓库

Use this code to divide the list of Chinese vocabulary into bite-sized categories of 20 words or fewer for you to study. If 20 words per day is too many (or too few) for you, you can change the value of `cluster_size` in the Python file `chinese-vocab-cluster.py`.

用本仓库的代码来以至多20个词汇的聚类归类现代汉语常用词表的56000个词汇，适合个人学习的用途。如果想调节聚类的大小，请调节Python文件`chinese-vocab-cluster.py`的`cluster_size`变量的价值。

To run the script in this repository, you will need to follow the instructions on FastText (see the References section of this Readme) to download and extract the word vectors. Make sure the files are all in the same directory as the word vectors that you download.

为了执行本仓库的脚本，首先需要按照FastText的指示（请看本Readme的参考资料）下载并解压缩词向量。

The code takes about 5 minutes to run on my computer, a 2017 model with an Intel i7 processor running on Windows Subsystem for Linux.

用我的个人电脑，脚本需要耗时大概5分钟的时间。我的个人电脑是一台2017年的，有英特尔i7处理器的电脑，而脚本是在适用于Linux的Windows子系统执行的。

The code uses the same seed value for the randomization in the K-Means algorithm, so the code is deterministic. If you want to randomize it, simply remove the `random_state = rand_state` from every line of code that calls `KMeans`.

代码使用固定的K均值聚类算法的随机种子，使用代码具有确定性。假设要随机的代码，则可以在每个引用`KMeans`函数的行省略`random_state = rand_state`。

## Overview | 要略

The code in this repo takes the 现代汉语常用词表 56,000 most frequently used modern Chinese words, finds the corresponding word vectors in FastText's language model for Chinese, then iteratively breaks the word collection down into smaller and smaller groups of words until all the groups have 20 or fewer words in them.

本仓库的代码的输入是现代汉语常用词表的56000最常用的现代中文词汇。代码在FastText的中文语言模型找词汇的对应词向量、然后迭代地把词库分别为越来越小的团。在所有团有最多20个词汇的时候，算法结束。

At each iteration, we apply the K-Means clustering algorithm to the group of words with the most words in it. By doing this, we divide the entire collection of words into smaller and smaller groups until every cluster of words has at most 20 words in it. Because of how the language model and K-Means clustering work, the end result is thousands of mini-collections of words that all belong to the same category! For example, one of the clusters has about 18 words for different holidays; another cluster has 20 words for different countries; and so on. It's easier to study and remember new words if they're related to each other.

每次迭代，我们对有最多的词汇的团应用K均值聚类算法。这么做，我们把全部的词汇放在越来越小的词团，直到每个团有至多20个词汇。由于语言模型和K均值聚类算法的本质，最后结果是成千属于一个类型的词汇小团！例如，一个词团有大概18个节日词汇；另一个词团有20个国家的名字；等等。这样会更容易记得你学的新词汇，因为在一个词团之内，所有的词汇都属于一个类型。