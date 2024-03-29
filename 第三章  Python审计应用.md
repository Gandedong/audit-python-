### 3.1	Py的基础函数
---
很多计算机教材都没有说明函数是什么，这里我介绍一下，计算机语言中的函数与数学中的函数是不一样的。这里我以前经常搞混，后来才搞明白。

数学上函数是假设有两个变量x、y，如果对于任意一个x都有唯一确定的一个y和它对应。这时y为x的函数。

计算机上的函数是一段可以调用的子程序，即输入X能得出Y的程序。

他们都可以输入X得到相同的输出结果Y。而计算机一个程序中可能包含了很多子程序，这个时候会将子程序称作函数，加以区别。

很多计算机语言中，有很多相同名称的函数，如Print函数，无论是C语言，还是B语言，他们的函数名称都是一样的，但可能在输入参数会有些不一样，所以有一定的计算机语言基础下，去学另一种计算机语言不会太难。

我如果将函数比喻为招式，很多不同门派的武学，他们的基础招式都是一样的，直拳就是直拳，冲拳就是冲拳，但是内里会有一些微细的不同，这个不同点就是参数，也就是变化。

我们用一个例子来说明一下什么是函数，什么是参数。

input() 是 Python 的内置函数，目的是获取用户输入的内容，input()函数会把要使用者输入的内容显示出来，然后输入内容后，当成一个数据传回来。就算使用者输入数字，也会显示数字。

在审计中，很多时候会忘记一定设定，这个时候用Input()函数会解决这个问题。

input([prompt])# 输入提示信息

参数prompt为提示信息。用过WPS的话，在输入函数时往往会有很多中文提示，这些中文提示其实是参数。

与input() 相反的函数是Print（）函数，这个是输出函数，目的是将结果输出，也是最常见的内置函数。

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

参数objects 表示为复数，可以一次输出多个对象，当输出多个对象时，需要用逗号分隔。Sep参数表示用来间隔多个对象，默认值是一个空格。end表示用来设定以什么结尾。默认值是换行符 \n，换成其他字符串。file 表示要写入的文件对象。flush 表示输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新，一般为默认False。

   参数符号	描述
   
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      

两个函数如果加起来一起用的代码如下：

name = input("请输入你的姓名")

print("你的姓名是：",name)

运行后，会提示：你的姓名，然后当你输入后，会输出你的名字。当然，看起来很傻，但一般来说，input不会马上直接与Print使用，中间他们会进行赋值，计算，然后再输出。

函数的赋值方法有很多，最普遍的是用“=”，这个不是等于，这个是赋值。

Python语言的等号是让左边的数字“使用”右边的值。Python语言的用法是先计算右边的值，再让左边的函数使用它。

V =1+2+3+4+5

Print(V)

这个时候才会输出为15。

如果是数学上的等于，在python中应该用两个等号表示，即“==”。

这个必须要记得的，我举个列，在引用EXCEL数据上面，“=”表示往往代表单元格的位置，“==”表示单元格的值，多一个与少一个，意思往往有很大的不同，这个也是很多新手会犯的错误。

除此之外，Python中的赋值必须遵守以下规则：

1必须以字母开头; 

2只能包含字母，数字和下划线字符 _

3不能包含空格或标点符号

以上的规则在其他计算机语言中也是有效的，不过相比较，python的赋值比较简单一点，例如在VB当中，我要将a=100的话，我就要写int a=100，但Python 不用，直接赋值就可以了。

Python中最常用的函数是If,elif这两个。用过EXCEL的有时候都会用IF函数进行条件判断。

if 判断条件：

    执行语句A
    
else：

    执行语句B
    
假设条件成立，就执行语句A，否则就执行语句B

结合上面的函数用法，可以做一个小程序说明一下。

"""

age = int(input("假设你妈24岁生你，请输入你的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于你妈25岁生你。")
elif age == 2:
    print("相当于你妈26岁生你。")
elif age > 2:
    human = 24 + age
    print("你妈现在有: %.d岁"%human) 
### 退出提示
input("点击 enter 键退出")

运行结果如下：
 
如果输入0或者负数，结果如下
 
"""

Python中有很多内置函数，使用方法也各不相同。后面我会选一点我们审计时经常用到的函数说明一下。


### 3.2	审计常用的函数应用

　函数是组织好的，可重复使用的子程序，就是如果已经有人发明好了轮子，那么就不要再自己发明。同样的，已经有写好的子程序，不需要再重写一次。只要你会调用就可以了。但实际上，除了轮子，还有一些地方需要自己设计的，如车头灯，这个时候你就要定义你想要什么样的车头灯了。在Python中，我们是用def（）自定义函数的。函数以 def 关键词开头，后接函数标识符名称和圆括号()。圆括号之间可以用于定义参数，return [表达式] 结束函数。

　def 函数名(参数1, 参数2, ……, 参数N):

　    执行语句
     
　在执行语句的过程中，如果加上return，自定义就会立刻中断，将结果返回，如果没有return，就会继续执行。注意，输入冒号和回车之后，下一行会自动缩进。
 
　我以永续年金作为例子，在会计学中，永续年金是指无限期收付款的年金，又称为永久年金，假设我成立了一项奖学金，每年要支出12万元，现时的折现率为10%，那么我的现值为多少呢？永续年金是没有终值的。
　代码如下
 
　def pvA(A, i):
    　p = A *  (1/ i)
    　return p
　result = pvA(120000, 0.1)
　print(result)
 
　这个时候，我们就定义了一个永续年金的函数pvA，其中圆括号()的参数A表示年金，i表示折现率。
 
　很多时候，我们在财务工作过程中需要创建一些自定义的函数，这个时候def定义函数就很有用了。定义完了之后，可以用Import语名进行加载。Import是一个非常重要的命令，也是很多计算机语言都有的命令。
 
　我们如果只需要调用this库下的某个函数，我们可以用from XX import this这种语句。from XX import YY与单纯的improt是不同的，我举个例你就明白了，improt XX指的是将我的XX背包拿给我，from XX 　　import YY指的是将XX背包中的YY拿给我。
 
　from modname import name1[, name2[, ... nameN]]
 
　modname指的是库名称，
 
　name1[, name2[, ... nameN]]指的是该库下的函数名称。
 
　意思就是，我只加载了这个套武功下的某一招式，相对于加载全套武功，我只加载了某个招式，我的运功速度会加快很多。不过对于新手来说，我比较喜欢直接全套武功加载。
 
　除此之外，python还有很多内置函数。
 
 　Python 3.x内置函数
  
　内置函数
 
 |abs()|delattr()|hash()|memoryview()|set()|
 |---|---|---|---|---|
 |all() |	dict()	 |help()	 |min()	 |setattr() |
　 |any()	 |dir() |	hex()	 |()	 |slicea() |
　 |ascii()	 |divmod() |	id()	 | |object() |	sorted() |
　 |bin()	 |enumerate() |	input()	 |()	 |staticmethod() |
　 |bool()	 |eval()	 |int() |	open()	 |str() |
　 |breakpoint()	 |()	isinstance()	 |ord() |	sum() |
　 |bytearray()	 |filter() |issubclass()	 |pow()	 |super() |
　 |bytes()	 |float()	 |iter() |	print()	 |tuple() |
　 |callable() |	format() |	len()	 |property()	 |type() |
　 |chr()	 |frozenset()	 |list()	 |range() |	vars() |
　 |classmethod()	 |getattr()	 |locals()	 |repr()	zip() |
　 |compile() |	globals()	 |map()	 |reversed()	 |__import__() |
　 |complex()	 |hasattr()	 |max()	 |round()	  |

　当然，有时候我们写的函数很多的时候，我们如何查找我编制的函数是否存在呢？我们可以用dir()函数进行检查。
 
　Dir这个命令非常古老了，在没有window的年代，就是用这个命令查找文件的，而在很多的计算机语言当中，dir()函数功能可以说是一样的，也是用来查找文件的。
 
　dir([object])
 
　例如我们在import this之后，用dir()看看内里有什么，这也是可以的。
 ```python
　import this
　dir()
　运行结果如下：
　['In', '_i28','_i29','_i3','_i30','_i31','_i32','_i33','_i4'
 ,'_i5','_i6','_i' '_i8','_i9', '_ih','_ii','_iii','_oh','exit',
 'get_ipython','pvA','quit',
 　'result','this','worker''Out','_','__','___','__builtin__','__builtins__',
 　'__doc__','__loader__','__name__','__package__','__spec__','_dh','_i','_i1',
 　'_i10',… … 
  ```
　不过由于本书不是计算机教材，篇幅有限，我就不逐一介绍各个内置函数了，而且很多时候来说，很多内置函数也不是经常用到，只需理解一下用法就可以了，有兴趣的读者可以通过访问 　https://docs.python.org/zh-cn/3/library/functions.html 进行查看。
 
　这里我要补充一下就是，不要老想要创建自定义函数def，其实函数就像招式一样，每个库当中已经定义好很多有用的招式了，这些招式虽然普通，但往往经过千锤百炼，出错的机会比较少，参数运用得当，往往比自创招式更好用。
 
　网络上有很多关于Python的教程，学费金额从几百元至几千元，但往往教的是最基本的内置函数，然后再让你去编写自定义函数，即自创招式。如果将开发程序比喻为打怪兽，那么你的自创招式很可能会打上好几天，还可能会打输。但如果学好了Python库，就等于学到了一套招式，往往几个回合就打败了怪兽。
 

### 3.3	NumPy库中的审计应用

　我说一下什么是Python库。所谓的Python库其实就是一个小型的Python文件，只是这些文件中包涵了很多事先设定好的函数。即一套武功包含了好几百套招式，到今天为止，Python共有269,771个库，也就是说这个门派中有二十多万套的武功。而更厉害的是，门派的武功是可以兼容的，即可以同时使用，如模拟键盘库+数据分析库+可视化图型库=数据演示系统。即我可以同时使用降龙十八掌、九阴百骨爪、七伤拳等等。
 
　可以说，强大的不是Python语言，而是Python库。很多声称使用Python用仅仅几行代码实现大数据可视化分析，实际上都是使用Python的某个第三方库。
 
　本书先介绍一下NumPy库的原因是由于我们大多数的工作都涉及到财务管理，所以有时候需要做一些数据计算。以往这个工作我们一般在Excel上完成，但如果掌握的NumPy，很多时候就可以超越Excel的限制。如Numpy是可以支持高阶大量的数组与矩阵运算。
 
　用过Excel都知道，其实表格的列和行之间的数字，其实和Numpy库中的数组差不多，空格填上数字，然后列与列之间相加相乘相除，得出的结果与Numpy库的数组与数组之间的运算结果是一样的。如果我要计算好几年的股票数据，单纯的一个表格很可能会崩溃，但Numpy就不会。
 
　所以Numpy库是一个非常重要的库，除了有博大精深的数学计算库，当中涉及到计算的函数就有500多个，是 Python 实现科学计算的基础。不过由于本书不是真的是计算机教材，所以不会逐一介绍，有兴趣的朋友可以网上可以搜索Numpy教程和官方文档。这里只是简单介绍一下。
 
　首先，我要说一下数组是什么？上一章介绍过一些计算机程序中函数的概念和用法，但数学上不止有函数，还有矩阵。什么是矩阵呢？就是一个按照长方阵列排列的数字集合。
 
　但在计算机程序中，计算机程序中，矩阵会被叫做数组。过去我们描述某个物品，我们会将这个物品的特点标出来，如重量，颜色，大小，形状等等，这个物品就是一个数组。如果我有一台车，我要识别行人或车辆，我就要同时计算一组又一组的数组，是否符合特征。如果能成功计算，这个程序就会保留下来，如果不能计算，就会重新计算。这个过程，就是计算机判断过程，也可以叫做人工智能。
 
　所以在《黑客帝国》之中最后一部就叫做《矩阵革命》其实不正确，应该叫做《数组革命》。因为矩阵是一个数学概念（线性代数里的），数组是个计算机上的概念。在接下来的发展中，我估计对数组的计算就越出色，就越有机会成为人工智能的计算机语言，而Python之所以被选作人工智能的开发语言，因为他的Numpy库可以做到多维数组的计算。
 
　相比较Python的内置函数，NumPy库能更快，更紧凑的计算数组，使用起来也很方便。除了在人工智能领域，在经济学、金融学、统计学上，数组的计算也是非常重要。我举一个不是很出名的例子进行说明一下，如投入产出计算，这个是诺贝尔经济学奖获奖者提出的一种经济分析计算方法。
 
  假设，一家农业公司有三样产品：苹果，苹果肉，苹果汁。他们的关系是，苹果会产出苹果肉，苹果肉会产出苹果汁，前者是后者的生产原料，其关系如下：5000元能买到X斤苹果肉和苹果汁，一斤苹果的可以产出0.4单位的苹果肉和0.45单位的苹果汁。
	关系如下图：
	
|X（斤）|	苹果|	苹果肉	|苹果汁|	Y（元）|
|---|---|---|---|---|
|苹果|	0|	0.4|	0.45|	5000|
|苹果肉|	0.25|	0.05|	0.1|	2500|
|苹果汁|	0.35|	0.1|	0.1|	3000|
 
	这个时候，这些关系可以变成两个AB两个数组，代码如下：
```python
	import numpy as np
　A=np.array([[0, 0.4,0.45],
 　        	[0.25,0.05,0.1],
 　       	  [0.35,0.1,0.1]])

　B=np.array([5000,2500,3000])
```
　按产品平衡模型 A x+y=x，式中A是直接消耗系数矩阵；x为各产品总产值向量；y为最终产品向量。
 
　代码说明：
　从上面的例子中首先需要导入numpy库，用的是import命令，在导入numpy库时通常使用“np”作为简写，用的是as命令，这也是Numpy官方倡导的写法。
 
　然后用np.array（）创建一个数组，用逗号隔开，就得到运行结果。
 
　数组通常是一个固定大小的容器，其类型有四个，分别是'整数', '浮点数', '复数' 和'布尔数'，而一个数组通常是由相同种类的数据组成的，这样有一个好处，就是数据运算速度快。
 
　具体参数如下：
 
　np.array(object, dtype = None, copy = True, ndmin = 0)
　参数object为数组，
　dtype为数据类型，
　copy为是否可复制，
　ndmin为最少维度。
　其中数据类型的有整数型int64，浮点数float64，复数型complex，布尔型bool，这些数据类型可以通过设定参数dtype进行调整的。

　如果我们这个时候，将两个数组进行相乘，他们的结果如下：
 
　A*B
　print(A*B)
	[[   0. 1000. 1350.]
	 [1250.  125.  300.]
 　	[1750.  250.  300.]]
　没错，数组发生变化。
 
　当然，为了方便理解，我才举了这么一个苹果例子，现实生活中，如果将苹果变成某只股票，苹果肉变成某只基金，苹果汁变成某只债券，那么就真的非常有意思了——我如何将有限的资金达到投资收益的最大化。
 
　我再举一些比较简单的例子：
 
　我们在审计的时候，一般会用到一些审计专业相关知识，如普通年金的终值和现值的计算，我们可以通过Numpy库内的一些函数计算到。运用熟练的话，比用EXCEL计算快多了。
 
　以下是一些事例：
 
　计算复利终值fv函数
　numpy.fv（rate，nper，pmt，pv，when ='end' ）
　rate为利率
　nper为期数
　pmt为每期固定支付款
　pv为终值
　when为期初还是期末付，1表示期初计数，0表示期末计数，默认为0
　备注一下，负数是付出，正数是收到。
假设，有一个项目，年利率为5%，每年年初现金流入10万元，5年后有多少钱？
```python
import numpy as np
r1=np.fv(0.05, 5-1, -100000, -100000,1)
	print("终值为：%.2f元" % r1)
输出结果—— 终值为：574113.75元
如果为年终现金流入，只需要将FV函数的参数改为0或删除。
r1=np.fv(0.05, 5-1, -100000, -100000)
	终值为：552563.13元
 ```

现值PV函数

numpy.pv(rate, nper, pmt,fv=0.0, when='end') #计算现值
参数与上面相同
计算现值的例子：假设银行的年利率为5%，每月投入1万元，现在需要投入多少本金才可以在5年后得到150万元？
np.pv(0.05/12, 5*12, -10000, 1500000)
	现值为：-638901.02元
现在需要投入63.89万元，5年后就可以有150万。

计算净现值numpy.npv

numpy.npv(rate, values)#计算净现值

这个是财务管理中经常要用到的计算，净现值。净现值主要算的是刨去货币贬值影响最后还能赚多少钱。

净现值>0表示项目实施后，除保证可实现预定的收益率外，尚可获得更高的收益。

净现值<0表示项目实施后，未能达到预定的收益率水平，而不能确定项目已亏损。

净现值=0表示项目实施后的投资收益率正好达到预期，而不是投资项目盈亏平衡。

参数rate为折现率

参数Values为收入，每一期的现金流。

假设A项目的折现率为5%，前期均需投入100万元，最终收益为110万元，其一至五年的收入分别是10、20、20、30、30万元。判断该项目是否值得投资。
代码如下：
```python
import numpy as np
C_A=[-100, 10, 20, 20, 30, 30]
npv_A=np.npv(0.05,C_A)
print("项目A的净现值：%.2f万元" % npv_A)
```
输出结果：
项目A的净现值：-6.87万元

不值得投资。

如果是两个相同的方案，收益相同，投入相同，但现金流入不同呢？这也可以。

假设有A、B两个项目，折现率均为5%，前期均需投入100万， A项目第一年至五年分别收入30、20、40、10、20万，共120万元，而项目B第一至五年分别收入30、40、30、10、10万，也是120万元，判断项目A和B哪个投资价值高？

代码如下：
```python
import numpy as np
C_A=[-100, 30, 20, 40, 10, 20]
C_B=[-100, 30, 40, 30, 10, 10]
npv_A=np.npv(0.05,C_A)
npv_B=np.npv(0.05,C_B)
print("项目A的净现值：%.2f万元" % npv_A)
print("项目B的净现值：%.2f万元" % npv_B)
```
输出结果：
	项目A的净现值：5.16万元
项目B的净现值：6.83万元
项目B的收益大。
 
审计中，除了要计算净现值之外，还需要计算内部报酬率（IRR）, 在考虑货币的通货膨胀下，我们在项目周期内我们能承受的最大货币贬值率有多少，更通俗地说就是假设我们去贷款来投资这个项目，所能承受的年最大利率是多少。比如某项目的内部报酬率IRR是20%，说的是该项目我们最大能承受每年20%的货币贬值率，也就是如果我们去贷款投资该项目所能承受的最大贷款年利率为20%，在贷款年利率是20%的时候投资该项目刚好保本。当实际贷款利率是5%时，那么剩下的15%就将是我们的利润。

计算内部报酬率

numpy.irr(values)

还是以上面为例子，前期均需投入100万， A项目第一年至五年分别收入30、20、40、10、20万，共120万元，这个项目的内部报酬率为多少呢？
```python
import numpy as np
C_A=[-100, 10, 20, 20, 30, 30]
npv_A=np.irr(C_A)
print("项目A的内部报酬率：%.2f" % npv_A)
```
输出结果：
项目A的内部报酬率为0.03

也就是说，我们每年能接受的货币贬值率为3%。

 
计算贷款每期还款金额pmt

如果项目A的投入100万元不是自有资金，而是银行贷款，贷款利率为6%，分五年还清，那么每期应该要还多少钱呢？

numpy.pmt(rate, nper, pv, fv=0, when="end")#计算每期应还的本金加利息
```python
import numpy as np
npv_A=np.pmt(0.06,5,1000000)
print("项目A每年应还贷：%.2f" % npv_A)
```
输出结果：
	项目A每年应还贷：-237396.40
	
即每年还款23.73万元。

如果这个项目我每年不能支付23万元，每年预计只能支付10万元，那么我应该向银行申请多少年还款比较合适呢？

计算付款期数函数：
numpy.nper
numpy.nper(rate, pmt, pv, fv=0, when='end')
参数rate为利率，pmt为每期支付金额，pv为现值。
```python
import numpy as np
npv_A=np.nper(0.06,100000,1000000)
print("项目A计划贷款期数：%.2f" % npv_A)
```
输出结果：
	项目A计划贷款期数：-8.07
那么我会建议向银行申请8年还贷。

 
有人问我，为什么不用EXCEL来计算IRR或PMT，没错，EXCEL是可以计算IRR的，而且计算的方法也简单，不过，如果数据量比较大的话，我还是推荐用Numpy来计算，因为如果要计算的融资项目非常多，融资时间非常长的时候，EXCEL计算还是比较吃力的。
 
例如，你的审计对象是一家普通的公司，可能不需要用Numpy来计算IRR，普通的EXCEL就可以了，但如果你的审计对象是一家融资租赁公司，大大小小有几百个融资项目，这个时候你就要真的用到Numpy了。

### 3.4 NumPy库计算投资风险

风险是预期结果的不确定性，在财务管理中，我们明白到风险是现代企业管理环境中的一个重要特征，也是在审计中不可避免中要面对的。特别在审计投资项目中，审计时需要计算该项目的投资风险，一般而言，由于环境和条件的情况变化，任何的投资都是有风险的，所以有了投资风险之类的概念。

由于投资风险与内部报酬率存在一定的对应关系，如投资风险越高，内部报酬率就越高，所以计算内部报酬率是一个可以衡量投资风险的方法。在之前我已经介绍过专门计算内部报酬率的函数numpy.irr了，但在实际工作中，我们会遇到两个或两上以上内部报酬率相同的项目，这个时候就需要计算方差、标准离差或标准离差率。

#### 什么是方差
方差就是用来表示变量与期望值之间的离散程度，其实就是每个样本值与全体平均值之差的平方值的平均数。公式如下：
	 
X为变量，u为总体平均值，N为总体例数。当数据分布比较分散（即数据在期望值附近波动较大）时，各个数据与期望值的差的平方和较大，方差就较大，
反之，当数据分布比较集中时，各个数据与期望值的差的平方和较小。方差就越少。
在这里我们可以用numpy.var函数来计算方差。
假设我有两个项目，他们的内部报酬率相同，但每一年的现金流入与现金流出不一样，这时要计算其方差。
A项目五年来的投资报酬率为 [-0.1,0.2,0.3,0.4,0.5]
B项目五年来的投资报酬率为 [-0.1,0.1,0.4,0.5,0.4]
这时我们代码为：
```python
import numpy as np
A=[-0.1,0.2,0.3,0.4,0.5]
B=[-0.1,0.1,0.4,0.5,0.4]
x=np.var(A)
y=np.var(B)
print("A项目的方差为：%.2f"%x,"B项目的方差为：%.2f"%y)
	运行结果如下：
	A项目的方差为：0.04 B项目的方差为：0.05
```

#### 什么是标准离差
其实就是是var的平方根，也是反映离散程度的一种量度。我们可以用numpy.std函数直接计算。一个较大的标准离差，代表大部分数值和其平均值之间差异较大；一个较小的标准离差，代表这些数值较接近平均值。 
	按上例，其计算代码如下：
```python
import numpy as np
A=[-0.1,0.2,0.3,0.4,0.5]
B=[-0.1,0.1,0.4,0.5,0.4]
x=np.var(A)  ##方差
y=np.var(B)
x1=np.std(A)  ##标准离差
y1=np.std(B)
print("A项目的方差为：%.2f"%x,"B项目的方差为：%.2f"%y)
print("A项目的标准离差为：%.2f"%x1,"B项目的标准离差为：%.2f"%y1)
```
运行结果如下：
	A项目的方差为：0.04 B项目的方差为：0.05
	A项目的标准离差为：0.21 B项目的标准离差为：0.22
注意：Python语言用符号#来标识注释，#之后的字符就是注释，不会对语句执行产生影响。

#### 什么是标准离差率
标准离差率就是标准离差与内部报酬率之间的比率，其计算公式是：
	在比较投资风险的时候，标准离差是以内部报酬率为中心计算出来的，现实中，内部报酬率大多是不相同的，而这个时候，我们就可以用标准离差多来判断项目的风险大小。
	也是以上面的为例子，假设AB项目内部报酬率分别是50%，60%，如何判断那个项目的风险最大呢？
	我们可以直接用numpy.std函数除以内部报酬率来得出，代码如下：
```python	
import numpy as np
A=[-0.1,0.2,0.3,0.4,0.5]
B=[-0.1,0.1,0.4,0.5,0.4]
A1=0.5   #A项目内部报酬率
B1=0.6  #B项目内部报酬率
x=np.var(A)
y=np.var(B)
x1=np.std(A)
y1=np.std(B)
x2=np.std(A)/A1 #计算标准离差率
y2=np.std(B)/B1 #计算标准离差率
print("A项目的方差为：%.2f"%x,"B项目的方差为：%.2f"%y)
print("A项目的标准离差为：%.2f"%x1,"B项目的标准离差为：%.2f"%y1)
print("A项目的标准离差率为：%.2f"%x2,"B项目的标准离差率为：%.2f"%y2)
```
运行结果如下：
	A项目的方差为：0.04 B项目的方差为：0.05
	A项目的标准离差为：0.21 B项目的标准离差为：0.22
	A项目的标准离差率为：0.41 B项目的标准离差率为：0.37
这时，我们可以认为A项目的投资风险是最大的。

事实上，标准离差率虽然可以评价投资风险的高低，但不能直接衡量风险报酬的多少，所以需要确定风险报酬系数，用来计算风险报酬率。审计的时候可能需要计算，的计算公式：ΚR═β×Ⅴ　式中：KR表示风险报酬率；β表示风险报酬系数；V表示标准离差率。
PS：风险报酬系数是企业承担风险的度量，一般由专业机构评估，如果是上市公司，也可以直接在网上查询。
