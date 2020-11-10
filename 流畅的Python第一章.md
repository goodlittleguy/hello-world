

## 流畅的Python第一章

`Python`严格尊崇鸭子类型,例:

```python
class a:
    b = [1,2,3,4,5]
    def __getitem__(self,index):
        return b[index]
'''我们先正常使用它'''
>>>a()[0]
>>>1
'''因为getitem表达取出数据,由鸭子类型我们也可以取出一堆特定步数的数据,正序取出数据,迭代取出数据(__iter__ 返回生成器),取出数据做比较'''
>>>a()[::2]
[1,3,5]

>>>for i in a():
    ....
    
>>>2 in a()
True 

'''既然能够取出数据,我们能逆序取出数据吗,答案是不能,因为 reversed(self),的实现需要依靠 len() 来实现,而我们现在仅仅继承了取出数据功能,而没有计数功能,要实现上述要求,我们需要..'''
>>>def __len__(self,obj):
	return len(obj)
>>>a().__len__(self,obj) = __len__(self,obj)
```



### `%` 与 `format` 格式化字符串

使用`%`的优点是简单快捷

| %d   | 十进制整数                   |
| ---- | :--------------------------- |
| %f   | 浮点数                       |
| %r   | 用 `repr()` 方法生成的字符串 |
| %s   | 用 `str()` 方法生成的字符串  |



| 对齐元素 | 有 `+`用显示正负符号, `-`表示左对齐(默认右对齐) , ` `空格表示 填充空格(不添加对齐标志默认空格填充) ,` 0`表示用 0 填充 |
| -------- | ------------------------------------------------------------ |
|          |                                                              |

```text
%[数据名称][对齐标志][宽度].[精度]类型
```



```python
>>>print('%08.3f' % (8.9))
00008.90
>>>print('%+8.3f' % 8.9)
000+8.90
```



使用`format`的优点是功能齐全

```python
'{1} {0}'.format('a',1) #支持位置映射

'{sex} {age}'.format(sex='boy',age=17) #支持关键字映射

'{human.sex} {human.age}'.format(human=namedtuple...) #支持对象属性映射

'{0[0]} {0[1]}'.format(lst) #还支持下标映射

```

<img src="https://pic1.zhimg.com/80/v2-0340c7e376d8215515f33c1c05c388f0_1440w.jpg" alt="img" style="zoom:150%;" />

```text
[[填充字符]对齐方式][符号标志][#][宽度][,][.精度][类型]
```

```python
>>>print('{:^+9,.2}'.format(888))
 +888.00 
```



### bisect用法

`bisect` 译为二分法,它的实质就是对一个查看一个元素在升序序列中应有的位置 , `bisect(haystack,hay):找出手上拿的稻草应该在上升的稻草垛中的位置`

```python
import bisect
def grade(score,breakpoints = [60,80,90],grades = "CBA"):
    line = bisect.bisect(breakpoints,score)
    return grades[line]
'''现在我们来试用一下'''
>>>[grade for socre in [60,70,80]]
['B','B','A'] #我们发现60与我们所设想不符,这是因为bisect方法将稻草放在相同大小草垛稻草的上面 , 要想放入它的下面,我们需要使用 biset_left
```

当然我们还有`bisect.insort(stack,hay) :将稻草放入上升的稻草垛上,并保证稻草垛上升`



### 使用数组而不是列表操作大量仅含数字的元素

>   -   Python数组完全继承自 C 语言的数组 , 在事先会规定元素的种类 , 保证内存不浪费 , 并且里面存放的是每个元素机器翻译(也就是字节码)
>   -   Python列表里面存放的是元素的引用 , 取出Python列表里的浮点元素时还要使用 float 将里面元素的引用转变为浮点数 
>
>   这两点决定了数组对数字的处理效率远高于列表

```python
>>>from array import array
>>>from random import randrange
>>>array('b',(randrange(-128,128) for i in range(10**7))) #得到数组
'''让人欣喜的是数组支持所有跟可变序列类型有关操作,其中它还单独提供了更高效的 intance_array.tofile(file) 写入二进制打开的文件的方法,与之对应的也有 intance_array.fromfile(file,number) number为读取文件中元素数目,注意写入与写出都要用二进制形式打开文件'''
```



