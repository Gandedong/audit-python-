## 第二章	Python的前置工具
　　本章主要介绍一下Python这个计算机语言，个人觉得Python的语法是比较简洁的，比较接近英语的书写习惯。对于我们做财务或审计的人来说，即使自己能写代码，对代码要求也不会太高，能跑起来就行了。
  
　　很多财务人员想学习Python，但不知从何着手，其实学习计算机语言与学习书本知识最大的不同是，学习一门计算机语言最重要的是动手去实践，不能靠死记硬背。最好的方法是跟着别人将代码一个一个的敲上去。就像学习驾使一样，开头可能很慢很难，但时间长了，就会开得飞快。
另外，不要去学习全部的计算机理论和代码分析之类的深奥知识，我们是财务，我们是审计，我们的工作不是计算机工程师，掌握一定的操作水平就可以了，我之前就没有经验，学了一大堆没有派上用场的知识，浪费了时间。

---
### 2.1	 Python安装
　　Python的安装没有什么好说的，去Python的官方网站http://www.python.org，选择Downloads就可以了，如果不喜欢最新版本，也可以下载其他历史版本的。但是我不推荐这样的操作。
  
 ![2 1](https://user-images.githubusercontent.com/57973589/124725795-c078ad80-df3f-11eb-9dc1-0482c1b08c4a.png)
 ![2 2](https://user-images.githubusercontent.com/57973589/124725857-ccfd0600-df3f-11eb-94d6-d87dcca35653.png)

　　因为官网中有很多个Windows的版本，让很多不是程序员出身的朋友不好选择。而且我们只是拿Python作为我们做数据分析，自动计算的工具，不是真的玩编程，所以我推荐大家去安装Anaconda（Python发行版）水蟒。
Anaconda适用于Windows，Linux和macOS系统，目的是简化软件包管理。我举个例子大家就明白了，你正在用Python做数据分析，然后你将分析的过程打包发给另一个同事，但同事是用MacOS系统，所以他不能打开。但这个时候，如果你们俩都安装了Anaconda，这个问题就不存在了。
 
 ![2 3](https://user-images.githubusercontent.com/57973589/124725997-f1f17900-df3f-11eb-9c0a-5ab65421eb50.png)
 

 
　　对很多不懂程序的人来说，安装一个软件总比安装几个软件更简单。因为你只需安装了Anaconda，就附带了：
一个名为Conda的开源软件包和环境管理系统，可轻松加载系统环境。
一套机器学习库，例如TensorFlow、scikit-learn和Theano。
一套数据分析库，例如pandas、NumPy和Dask。
一套可视化库，例如Bokeh、Datashader、matplotlib和Holoviews。
一套Python的IDE，例如一个Jupyter Notebook可共享的IDE，结合了实时代码、可视化效果和文本。一个名为JupyterLab的进阶IDE，一个名为Spyder的数据分析IDE。

![2 4](https://user-images.githubusercontent.com/57973589/124726138-14839200-df40-11eb-9f67-93765f7fe4f3.png)

 
　　在Windows安装的步骤如下：
1、	访问Anaconda.com/downloads

![2 5](https://user-images.githubusercontent.com/57973589/124726190-206f5400-df40-11eb-8015-e61718d68adb.png)

 
注意一下，不要下错了，要下个人版，这个是免费的，如果下了商业版，这个是要收费的，很多朋友就下错了。

![2 6](https://user-images.githubusercontent.com/57973589/124726274-2ebd7000-df40-11eb-9263-683f409f117b.png)

 
2、	选择Windows安装程序下载

![2 7](https://user-images.githubusercontent.com/57973589/124726316-3846d800-df40-11eb-8980-ef13c76a3f68.png)

 
3、	打开并运行安装程序

![2 8](https://user-images.githubusercontent.com/57973589/124726365-439a0380-df40-11eb-8b40-b6cc93c56ccf.png)

 
　　后面安装时的选项一个都不要勾，不要动，均选择默认。
  
4、	打开Anaconda Prompt并运行一些Python代码

![2 9](https://user-images.githubusercontent.com/57973589/124726450-58769700-df40-11eb-9d47-4e2d509f7685.png)

 
在Anaconda提示符下，键入python并回车，启动Python解释器，
 
再输入import this，就会弹出Python内核开发者蒂姆·皮特斯（Tim Peters）的格言：

![2 99](https://user-images.githubusercontent.com/57973589/124726573-747a3880-df40-11eb-8bea-81080a21e4c5.png)

 
优美优于丑陋， 
明了优于隐晦； 
简单优于复杂， 
复杂优于凌乱，
扁平优于嵌套，
稀疏优于稠密，
可读性很重要！
即使实用比纯粹更优，
特例亦不可违背原则。
错误绝不能悄悄忽略，
除非它明确需要如此……

这个也是Python语言的设计原则。

在在MacOS上安装Anaconda大体与Windows一样，点击官网的“Download”，然后下载MacOS的.pkg安装程序文件。但有一点不同的是安装后，您需要在PATH将Anaconda加载到环境变量中。
打开MacOS终端并输入：

$ cd ~

$ source .bashrc

完成安装。

对审计人员来说，由于不是专业程序员，所以很难管理已经安装的库，而且分析完一套数据后往往需要其他人员进行后续操作，这时Anaconda的重要性就不言而喻了。

其实，本人希望中国的软件企业能开发出一个适合国人使用的资源管理系统，当然，最好是不用钱的，如果要钱的话，也希望能便宜一点。因为一个软件管理系统真的对外行非常有用。
