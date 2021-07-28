# chinese-vocab-cluster
If you're an intermediate Chinese student, you need to constantly grow your vocabulary by learning new words. But over time, it becomes harder to find new words to learn. When you do learn new words, it's easy to forget them because of how scattered they are: today your friend talked about their favorite pet, so you learned some new words about pets; yesterday, you read an article online that used a 成语 (idiom) that you did not know.

如果你是中级的中文学生，你就一直要学新的词汇。但是你的中文水平越好，新的词汇越难找。而且，学了新的词汇会更容易忘掉因为它们都是很七七八八的。譬如，今天你的朋友聊了他最爱的宠物，所以你学了一些关于宠物的词汇；昨天，你读的一篇文章有一个你以前不知道的成语。

When you try to learn vocabulary that is all scattered and unrelated, it is more difficult to remember long-term. On the other hand, if you learn words by theme, you might miss some domains entirely. For example, I forgot to study names of common chemicals until recently. These are the key challenges of Chinese language learning that this repo aims to solve.

一方面是如果你试图学会很七七八八的词汇，就会更难以长期记得。另一方面，如果你按照主题学词汇，你可能就会错过一些你想不到的领域的词汇。譬如，我很久忘了学常见的化学词汇。这两个挑战是本仓库想解决的问题。

In this repo, we take a list of the 56,000 most frequently used Chinese words, and programmatically divide it into categories of 20 words or less. The categories contain related words, so if you study 1 or 2 categories per day, it will be much easier for you to remember the new words. Because we use the 56,000 most common Chinese words, you won't miss any important words either!

本仓库把56000个常用的中文词汇给程序性放在至多20个词汇的聚类。一个聚类所包含的词汇都是相关的。你可以每天学一两个聚类。这样会更容易记下新的词汇，因为是相关的。而且，因为本仓库使用的是56000最常用的中文词汇，你就不会错过任何常用的词汇。

Not all the categories are perfect, but here are some examples of the categories that this code repo outputs for you:

不是所有的聚类都完毕，不过以下例子都是本仓库的脚本输出的比较有逻辑的聚类：

Category 2265: Continents, Countries, Regions, and Cities | 2265号聚类：洲，国家，地区，和城市
澳大利亚 (Australia), 巴基斯坦 (Pakistan), 北美洲 (North America), 大西洋 (Atlantic Ocean), 哈萨克斯坦 (Kazakhstan), 呼和浩特 (Hohhot, Inner Mongolia), 加拿大 (Canada), 拉丁美洲 (Latin America), 马来西亚 (Malaysia), 孟加拉 (Bengal region), 莫斯科 (Moscow), 南美洲 (South America), 塔吉克斯坦 (Tajikistan), 太平洋 (Pacific Ocean), 乌鲁木齐 (Urumqi, Xinjiang), 新加坡 (Singapore), 伊斯兰堡 (Islamabad, Pakistan), 意大利 (Italy), 印度尼西亚 (Indonesia)

Category 7044: Fingers | 7044号聚类：手指
拇指 (thumb), 食指 (index finger), 手指 (finger), 小指 (pinky)

Category 6928: Holidays | 6928号聚类：节日
重阳节 (Double Nine Day, for celebrating elders), 倒计时 (to count down time, as on New Year's Eve), 端午节 (Dragon Boat Festival), 感恩节 (Thanksgiving), 古尔邦节 (Eid al-Adha), 国庆节 (Chinese National Day), 黄金周 (Golden Week, one of 2 week-long holidays in China, for 国庆节 and 春节), 教师节 (Teachers' Day), 母亲节 (Mothers' Day), 清明节 (Tomb Sweeping Day), 圣诞节 (Christmas), 圣诞卡 (Christmas card), 游园会 (a type of outdoor carnival), 元宵节 (Lantern Festival), 阅兵式 (military parade, as on 国庆节), 中秋节 (Mid-Autumn Festival)

You can take the results from the `output.txt` file and study 1 or 2 categories per day to keep expanding your Chinese vocabulary. You can also make flashcards, or digital flashcards with Anki.

你可以每天学习输出文件`output.txt`的一两个聚类。这样你可以一直扩展你的词汇知识。你还可以自己做记忆卡片，或者Anki APP的电子记忆卡片。

Another benefit of this repo is that the `output.txt` file is sorted by the average frequency of words in a category. So, the categories with the most common words appear near the top of the file, with more obscure terms appearing near the end of the file.

况且，输出文件`output.txt`的聚类是依平均频率排序。所以，最常见的词汇在`output.txt`初，而比较罕见的词汇在文件末。

## Dependencies | 依赖
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

The code takes about 80 seconds to run on my computer, a 2017 model with an Intel i7 processor running on Windows Subsystem for Linux.

用我的个人电脑，脚本需要耗时大概80秒钟的时间。我的个人电脑是一台2017年的，有英特尔i7处理器的电脑，而脚本是在适用于Linux的Windows子系统执行的。

The code uses the same seed value for the randomization in the K-Means algorithm, so the code is deterministic. If you want to randomize it, simply remove the `random_state = rand_state` from every line of code that calls `KMeans`.

代码使用固定的K均值聚类算法的随机种子，使用代码具有确定性。假设要随机的代码，则可以在每个引用`KMeans`函数的行省略`random_state = rand_state`。

## Overview | 要略

The code in this repo takes the 现代汉语常用词表 56,000 most frequently used modern Chinese words, finds the corresponding word vectors in FastText's language model for Chinese, then iteratively breaks the word collection down into smaller and smaller groups of words until all the groups have 20 or fewer words in them.

本仓库的代码的输入是现代汉语常用词表的56000最常用的现代中文词汇。代码在FastText的中文语言模型找词汇的对应词向量、然后迭代地把词库分别为越来越小的团。在所有团有最多20个词汇的时候，算法结束。

At each iteration, we apply the K-Means clustering algorithm to the group of words with the most words in it. By doing this, we divide the entire collection of words into smaller and smaller groups until every cluster of words has at most 20 words in it. Because of how the language model and K-Means clustering work, the end result is thousands of mini-collections of words that all belong to the same category! For example, one of the clusters has about 18 words for different holidays; another cluster has 20 words for different countries; and so on. It's easier to study and remember new words if they're related to each other.

每次迭代，我们对有最多的词汇的团应用K均值聚类算法。这么做，我们把全部的词汇放在越来越小的词团，直到每个团有至多20个词汇。由于语言模型和K均值聚类算法的本质，最后结果是成千属于一个类型的词汇小团！例如，一个词团有大概18个节日词汇；另一个词团有20个国家的名字；等等。这样会更容易记得你学的新词汇，因为在一个词团之内，所有的词汇都属于一个类型。