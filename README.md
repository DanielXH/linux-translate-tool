## linux-translate-tool
一个在linux系统terminal中使用的翻译工具。
基于python3

注：使用该工具需要联网

![](https://raw.githubusercontent.com/DanielXH/linux-translate-tool/master/src/images/linux-translate-tool-img4.png)

## 开发原因
有时候想要查单词或者翻译，觉得打开网站去查太麻烦，上网找关于linux的翻译工具，似乎很多项目都已经多年没有人维护了。

出于使用方便的考虑，还是自己开发一个小工具吧。

## 下载安装方法
目前所有提供翻译api服务的网站都不会是免费的，但是一般注册api服务后，会提供一定的金额来免费使用。

该工具使用的是有道翻译的api。

### 1） 注册有道智云帐号
进入有道智云http://ai.youdao.com/，注册一个帐号。

可以看到帐号有100元余额，这是我们可以使用的金额。

根据官方计费方式，每一百万字符价格为48元，所以注册一个帐号足以够我们个人使用了。

### 2） 在有道智云上创建应用
在自然语言翻译->翻译实例中，创建一个实例。实例名称随便填。

![](https://raw.githubusercontent.com/DanielXH/linux-translate-tool/master/src/images/linux-translate-tool-img2.png)

在应用管理中->我的应用中，创建一个应用。名称、类别、描述随便填。

![](https://raw.githubusercontent.com/DanielXH/linux-translate-tool/master/src/images/linux-translate-tool-img1.png)

创建应用后，添加刚刚创建的应用实例。

进入该应用，拿到我们需要的应用ID（appKey）和应用密钥（secretKey）。

### 3）下载、添加文件
下载文件：
```
git clone https://github.com/DanielXH/linux-translate-tool.git
```

把`src/translate.py`文件复制到另一目录下。

修改`tranlate.py`文件，将文件内 `youdaoAppKey` 和 `youdaoSecretKey` 的值设置为刚刚拿到的 `appKey` 和 `secretKey` 值：

![](https://raw.githubusercontent.com/DanielXH/linux-translate-tool/master/src/images/linux-translate-tool-img3.png)


给该文件添加执行权限：
```
chmod a+x translate.py
```

这样就可以使用了。文件是用python3编写的，如下：
```
python3 ./translate.py hello
```


### 4） 添加到命令行命令 
如果每次都要像下面一样调用方法，就每次都要进入该文件的目录，难免会觉得比较麻烦。
```
python3 ./translate.py hello
```

下面暂时提供一种解决解决方案，添加永久化的alias自定义命令。

使用root帐号，打开从根目录起，找到`/root/.bashrc`文件，在文件最后添加下面命令：
```
alias tl='tl() {python3 /home/xudongh/Software/terminal-translate-tool/translate.py $1;}; tl'
```
如果无法修改`.bashrc`文件，那就先添加修改权限。

这样我们可以直接如下使用：
```
tl hello
```

不过这种方法有一点比较麻烦，就是我们刚刚只是在root用户下的`.bashrc`添加了`alias`规则，所以只能在root用户使用。

在一般用户下就不能使用该命令，此时还要在一般用户的目录下的`.bashrc`添加`alias`规则。例如我的用户名是`xudongh`，那么就同样修改`xudongh/.bashrc`:
```
alias tl='tl() {python3 /home/xudongh/Software/terminal-translate-tool/translate.py $1;}; tl'
```

这样的话，就能在两个用户下都能使用该翻译工具（一般个人电脑其实就两个用户）。

注意：

- 命令中`tl`是我们用于调用的自定义命令，当然你可以不使用`tl`,用`fy`等也可以，只要你喜欢；
- 文件路径建议使用绝对路径！从根目录`/`开始，不要从用户目录`~`开始，这样可以保证任何一个用户都能访问到这份文件。


### 5）使用方法
如上面所述，只要进入相应该文件目录，运行该py文件就可以了,非常简单：
```
python3 ./translate.py hello
```

如果你配置了`alias`规则，还可以更方便：
```
tl hello
```

目前，调用一次命令只返回一次结果。

如果你要查的是一个单词，那参数可以是hello、'hello'、"hello"，三种方式均可；

如果你要查的是一带有空格的句子，那就要用单/双引号括起来。

> *不过，目前发现，如果使用tl进行翻译查询，传入的参数不能带有空格，即便使用单/双引号也不行。*
> *emmmmmm... 这个问题有时间再搞吧 - -*

可以看到，该翻译工具支持单词或句子;

同时可以自动识别以下八种语言：

- 中文
- 日文
- 英文
- 韩文
- 法文
- 俄文
- 葡萄牙文
- 西班牙文

![](https://raw.githubusercontent.com/DanielXH/linux-translate-tool/master/src/images/linux-translate-tool-img4.png)

当然，你也可以像一般命令一样，使用以下命令查看帮助：
```
python3 ./translate.py -h
python3 ./translate.py -help
```
虽然它没什么卵用，当你真正需要查找帮助的时候，这提示也帮不了你什么哈哈哈 - -

### 6）开发进度

- [ ] 封装linux安装包
- [x] 有道翻译api
- [ ] 百度翻译api
- [ ] google翻译api
- [ ] 离线翻译


