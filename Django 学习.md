## `django` 学习:

>   web（World Wide Web） 是各个局域网的主线 , 将各个局域网整合成全球的共享网络 ，它是一种基于超文本和HTTP（（超文本传输协议））的、全球性的、动态交互的、跨平台的分布式 （信息不在一个页面上完全呈现，而是可以通过链接形式让用户进入另一页面的形式）图形信息系统

它基于: 

1. 超文本 : 超文本是一种用户接口方式 , 它表现形式为点击一段文本文字的链接 (学名:超文本链接) 即可跳入另一网址 （web 的主要特征）
2. 超媒体 : 在网址内不仅仅可以看文本 , 还可以看图片 , 听声音 , 看视频 , 例如哔哩哔哩 

的信息组织方式



虚拟环境的创建与退出:

```python
&virtualenv <虚拟环境名> 用于创建虚拟环境
#当需要指定Python版本下的虚拟环境时 virtualenv -p Python3.x  <虚拟环境名>

&<虚拟环境名>\Scripts\activate 进入虚拟环境

&deactivate 退出虚拟环境 或
#&<虚拟环境名>\Scripts\deactivate.bat 
```



Django服务运行:

```python
&python manage.py runserver #Python直接运行Django的manage.py 
```





##### Django的实现方式

接收请求 -> 解析请求 -> 查找有无对应方法 -> 无方法(返回404 page not find) -> 有方法 ->返回处理好的数据 

枢纽:

URL.py

>   它接受客户端请求,并向客户端返回处理后的响应



##### 创建网站时的小建议:

先在脑海中想好应该实现怎样的主要功能和主要对象模块 

例如创建一个实时聊天系统 : 

>   我们需要的功能是聊天 , 聊天功能里我们需要保证消息实时 <WebSocket>方法实现 和 消息提醒 <网页弹出消息提醒,声音显示>
>
>   在对象模块里我们需要有最少两个对象在聊天 , 对象的容纳 , 昵称的设置也是对象模块中必不可少的组成
>
>   这些就是核心功能和对象 , 以后我们完成核心功能和对象后才能试着拓展 , 例如: 离线消息的发送 , 多人聊天的实现

我们可以使用思维导图帮助我们将想法理顺



#####  

##### 开发实时聊天功能相关的网络概念

`TCP`:

>   TCP : <传输控制协议 Transmission Control Protocol> 是为了在不可靠的互联网网络上提供**可靠的**端到端**字节流**而专门设计的



主要工作原理:

>   将8位字节表示的数据流分成适当长度的报文段 , 后将报文编号后传给 IP 层 , 由 IP 层通过网路将数据包传给端口的 TCP 层 , 结束数据的TCP层根据报文编号正确排序后得到完整报文 , 如一段报文丢失 , 接收端口的 TCP 会提醒发送端口的 IP 重发



`WebSocket`:

>   `WebScoket` 是建立在单个 `TCP`连接上的可双向通信的协议 , 它使得服务器端可以主动向客户端发起请求 , 在`WebSocket API` 中服务器与客户端仅需一次握手就可以建立持久性的连接



在网页上点击`f12` , 点击 `Application` 会发现 `Storage` 里有 

![image-20200717101734668](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20200717101734668.png)

这里面是各种本地存储的数据库 : 

>   local storage 是永久性存储库 , 单次存储量为 1M ~ 10M 
>
>   session storage 是临时存储库 , 其余性质与 local storage相同
>
>   `IndexedDB` 是永久存储库 , 单次存储量很大 , 但操作较麻烦
>
>    Web SQL 现在已经几乎废弃
>
>   cookies 是临时小存储库 , 单次存储量为 4k





### HTTPS使用Django的小技巧

在创建项目时Django自带 `urls.py` 与 `setting.py `和 `wsg.py` 模块

其中 url.py :

>   接受客户端请求 , 并返回处理后的数据 , url.py 就是总枢纽 .
>
>    其他处理数据的模块通过导入 `url.py` 实现数据处理 , 其中url.py 常常将处理数据的方法放入 views.py 中 <我们自建的与url.py 同级的文件> , 而 views.py 在返回页面数据时会常常将包含html的区域单独放在与项目文件夹同级 <也就是views.py父目录的区域> 的名为 static 的文件中 <其中 static 的名字由来是 setting.py 文件中提前定义的>  



setting.py:

>   内含多种设置参数 , 值得关注的是:
>
>    setting.py 中的 BASIC_DIR 变量名内存的根目录 , 使得views.py 能通过绝对路径找到位于它父目录的 static 中的 html 文件
>
>   setting.py 中 STATIC_URL 中定义的静态文档名`static` , 决定了 Django 如果想通过静态方法 而不是 以url.py为枢纽再处理得到动态页面 , 直接得到静态页面 , 就必须将 HTML 文件放在 static 文档中















