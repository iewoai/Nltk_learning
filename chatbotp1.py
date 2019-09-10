import nltk
# nltk.download()
from nltk.book import *
nltk.download('averaged_perceptron_tagger')
# 输出书籍标题
# 这里面的text*都是一个一个的书籍节点，直接输入text1会输出书籍标题
# print(text1)

# 搜索20个包含(former)语句的上下文
# print(text1.concordance("former"))

# 搜索相关词ship(近义词)
# print(text1.similar("ship"))

# 查找某个词在文章出现的位置
# print(text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]))

# 返回text1总字数
# print(len(text1))

# 返回文本的所有词集合
# print(set(text1))

# 返回文本总词数
# print(len(set(text4)))

# 返回“is”这个词出现的总次数
# print(text4.count("is"))

# 统计文章的词频并按从大到小排序存到一个列表里
# for i in FreqDist(text1):
# 	print(i)

# 统计词频，并输出累计图像
# fdist1 = FreqDist(text1);fdist1.plot(50, cumulative=True)

# 返回只出现一次的词
# print(fdist1.hapaxes())

# 频繁的双联词
# print(text4.collocations())

# 返回Gutenberg语料库的文件标识符
# nltk.corpus.gutenberg就是gutenberg语料库的阅读器
# print(nltk.corpus.gutenberg.fileids())

# 输出chesterton-brown.txt文章的原始内容
# print(nltk.corpus.gutenberg.raw('chesterton-brown.txt'))

# 输出chesterton-brown.txt文章的单词列表
# print(nltk.corpus.gutenberg.words('chesterton-brown.txt'))

# 输出chesterton-brown.txt文章的句子列表
# print(nltk.corpus.gutenberg.sents('chesterton-brown.txt'))

'''
from nltk.corpus import webtext：网络文本语料库，网络和聊天文本

from nltk.corpus import brown：布朗语料库，按照文本分类好的500个不同来源的文本

from nltk.corpus import reuters：路透社语料库，1万多个新闻文档

from nltk.corpus import inaugural：就职演说语料库，55个总统的演说
'''

'''
fileids()：返回语料库中的文件

categories()：返回语料库中的分类

raw()：返回语料库的原始内容

words()：返回语料库中的词汇

sents()：返回语料库句子

abspath()：指定文件在磁盘上的位置

open()：打开语料库的文件流
'''

'''
# 加载自己的语料库
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/tmp'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
'''

'''
# 比如要输出在布朗语料库中每个类别条件下每个词的概率
import nltk
from nltk.corpus import brown

# 链表推导式，genre是brown语料库里的所有类别列表，word是这个类别中的词汇列表
# (genre, word)就是类别加词汇对
genre_word = [(genre, word)
		for genre in brown.categories()
		for word in brown.words(categories=genre)
		]

# 创建条件频率分布
cfd = nltk.ConditionalFreqDist(genre_word)

# 指定条件和样本作图
cfd.plot(conditions=['news','adventure'], samples=[u'stock', u'sunbonnet', u'Elevated', u'narcotic', u'four', u'woods', u'railing', u'Until', u'aggression', u'marching', u'looking', u'eligible', u'electricity', u'$25-a-plate', u'consulate', u'Casey', u'all-county', u'Belgians', u'Western', u'1959-60', u'Duhagon', u'sinking', u'1,119', u'co-operation', u'Famed', u'regional', u'Charitable', u'appropriation', u'yellow', u'uncertain', u'Heights', u'bringing', u'prize', u'Loen', u'Publique', u'wooden', u'Loeb', u'963', u'specialties', u'Sands', u'succession', u'Paul', u'Phyfe'])
'''

'''
# 我们还可以利用条件频率分布，按照最大条件概率生成双连词，最终生成一个随机文本
# 这可以直接使用bigrams()函数，它的功能是生成词对链表。
import nltk
# 循环10次，从cfdist中取当前单词最大概率的连词,并打印出来
def generate_model(cfdist, word, num=10):
	for i in range(num):
		
		word = cfdist[word].max()
		print(word)
# 加载语料库
text = nltk.corpus.genesis.words('english-kjv.txt')

# 生成双连词
bigrams = nltk.bigrams(text)

# 生成条件频率分布
cfd = nltk.ConditionalFreqDist(bigrams)

# 以the开头，生成随机串
generate_model(cfd, 'the')
'''

'''
有一些仅是词或短语以及一些相关信息的集合，叫做词典资源。

词汇列表语料库：nltk.corpus.words.words()，所有英文单词，这个可以用来识别语法错误

停用词语料库：nltk.corpus.stopwords.words，用来识别那些最频繁出现的没有意义的词

发音词典：nltk.corpus.cmudict.dict()，用来输出每个英文单词的发音

比较词表：nltk.corpus.swadesh，多种语言核心200多个词的对照，可以作为语言翻译的基础

同义词集：WordNet，面向语义的英语词典，由同义词集组成，并组织成一个网络
'''

'''
import nltk
# 提取词干（即原型）
porter = nltk.PorterStemmer()
print(porter.stem('lying'))
'''


# import nltk
# # 标注一句话的词性
# # word_tokenize将一句话转化成序列
# text = nltk.word_tokenize("And now for something completely different")
# # pos_tag根据一个词序列来动态判断词性
# print(nltk.pos_tag(text))
