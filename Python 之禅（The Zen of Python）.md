# Python 的作者：Guido van Rossum

<img src="https://upload.wikimedia.org/wikipedia/commons/6/66/Guido_van_Rossum_OSCON_2006.jpg" alt="Guido van Rossum" title="Guido van Rossum" width="100" height="150" />  [原图](https://upload.wikimedia.org/wikipedia/commons/6/66/Guido_van_Rossum_OSCON_2006.jpg "Guido van Rossum") | [维基百科（英文）介绍](https://en.wikipedia.org/wiki/Guido_van_Rossum/ "Guido van Rossum")   |  [维基百科（中文）介绍](https://zh.wikipedia.org/wiki/%E5%90%89%E5%A4%9A%C2%B7%E8%8C%83%E7%BD%97%E8%8B%8F%E5%A7%86/ "吉多·范罗苏姆")

---

## The Zen of Python
作者：Tim Peters  
[维基百科（中文）介绍](https://zh.wikipedia.org/wiki/Python%E4%B9%8B%E7%A6%85/)   | [维基百科（英文）介绍](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer/))   | [Python 官网链接](https://www.python.org/dev/peps/pep-0020/)   |  [GitHub 链接](https://github.com/python/peps/blob/master/pep-0020.txt)   |  [邮件原文](https://mail.python.org/pipermail/python-list/1999-June/001951.html)

>Python之禅 最早由 Tim Peters 在Python邮件列表中发表，它包含了影响Python编程语言设计的19条软件编写原则。在最初及后来的一些版本中，一共包含20条，其中第20条是“这一条留空（...）请 Guido 来填写“。这留空的一条从未公布也可能并不存在。这些文本属于 公共领域。

>Python之禅作为一个信息条款被录入Python增强建议（PEP）的第20条，在Python语言的官方网站也能找到。它还作为复活节彩蛋被包含在Python解释器中。如果输入 `import this` 就会在Python的编程环境IDLE中显示。


## PEP 20 -- The Zen of Python
Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!  

## 译文版本 1
链接：https://zhuanlan.zhihu.com/p/40950546
## Python 之禅

美 优于 丑  
明确 优于 隐晦 （1）  
简单 优于 复杂  
复杂 也好过 繁复 （2）  
扁平 优于 嵌套  
稀疏 优于 拥挤  
可读性很重要（3）  
固然代码实用与否 比洁癖更重要。  
我们以为的特例也往往没有特殊到必须打破上述规则的程度。  
除非刻意地静默。  
否则不要无故忽视异常（4）  
如果遇到模棱两可的逻辑，请不要自作聪明地瞎猜。  
应该提供一种，且最好只提供一种，一目了然的解决方案  
当然这是没法一蹴而就的，除非你是荷兰人（5）  
固然，立刻着手 好过 永远不做。  
然而，永远不做 也好过 不审慎思考一撸袖子就莽着干  
如果你的实现很难解释，它就一定不是个好主意  
即使你的实现简单到爆，它也有可能是个好办法  
命名空间大法好，不搞不是地球人！  

## 注释
1. 该引入的包一个一个列出来不要合并；不要用星号；不要在方法里藏意想不到的的副作用，等等等等。还一个例子，另外一种著名的软件设计原则 Convention over Configuration（约定优于配置）如果做得不谨慎就会违背这条。  
2. SO: 必要的复杂逻辑是难免的，而繁复啰嗦的代码是不可接受的。  
3. Readability counts 不能翻译成可读性计数啊喂😂  
4. 实操中很多人不注意 catch 完就 log 一下 就不管了，这样不好。软件界一般都讲 Let it fail，学名为 Fail-fast 法则。简而言之就是整个项目周期中越早暴露的问题，其修复成本越低。  
5. 本文作者 Tim peters 解释说这里的荷兰人指的是 Python 的作者 Guido van Rossum。

## 译文版本 2
链接：https://www.jianshu.com/p/0e1f38c2c122

Python 之禅，by Tim Peters

优美胜于丑陋（Python 以编写优美的代码为目标）  
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）  
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）  
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）  
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）  
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）  
可读性很重要（优美的代码是可读的）  
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）  
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）  
当存在多种可能，不要尝试去猜测  
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）  
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）  
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）  
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）  
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）