## 流畅的Python第三章



为什么字典的键和集合的元素都必须是可散列的呢?

>    通常来说可散列对象的定义是它不可变 : 就比如无可变元素的元组 , 或者一个字符或字符串
>
>   Python实现字典类型的实现实际上是通过散列表 (稀疏的数组) , 散列表的单元是表元 , 字典的表元是由键和值组成 , 所以我们通过字典的键查找其映射实际上是通过散列表查找其对应的表元.
>
>   `my_dict[search_key]`利用 hash 方法将`search_key` 转化成数字,然后根据字典所占内存取出该数字后几位当作偏移量 , 最后通过偏移量在字典散列表中查找对应的表元 , 当未找到返回 `keyerror` 错误 , 找到表元后 Python 会检验 `search_key`是否等于表元里的键值 , 若发生散列冲突 , Python会再取出数字中另外几位 , 处理后重新查找 

通过上述解释我们发现字典的键必须是不可变的 , 这样hash出来的值才会保持恒定 , 以保证我们能找到对应的表元 , 集合也同理 , 实际上字典和集合的查找元素的高效性是通过散列表实现的 , 这是典型的空间换时间的做法. 

同时字典为了保证总有大约过量三分之一的内存存储数据 , 在我们往字典中添加数据时字典有可能进行扩容 (新建一个更大的散列表,将原数据复制到更大散列表中) , 这样会导致原数据的位置错乱 , 所以我们在迭代导出数据的同时不要试着修改或添加数据 , 这样可能带来迭代时跳过某些元素的错误



 

```python
''' setdefault 方法在找不到字典对应的键时 , 该方法会返回该默认值后自动为该键添加该默认值 , 其中defaultdict类型自动有该方法'''
>>>a = {}
>>>a.setdefault(1,2)
2
>>>a
>>>{1:2}
'''现在我们试试default方法'''
>>>from collections import defaultdict
>>>a = defaultdict(lambda : "sorry i can't find it")
>>>a[1]
"sorry i can't find it"
>>>a
{1,"sorry i can't find it"}


'''get 方法,找不到字典中的值时返回默认值'''
>>>a.get(2,3)
3
>>>a
{1:2}

'''同时我们还可以通过update方法让批量添加可迭代元素元素进字典成为可能'''
>>>a = {}
>>>a.update([(1,2),(3,4)])
>>>a
{1:2,3:4}
```

 当我们也希望别人不能更改字典的不可散列的值时 , 我们可以使用`MappingProxyType`方法创建不可变的动态映射对象

```python
from types import MappingProxyType
'''我们可以吧不可变动态映射对象看作原对象的影子'''
>>>a = {1:2}
>>>b = MappingProxyType(a)
>>>b.get(1)
2
b[2] = 3
TypeError: 'mappingproxy' object does not support item assignment #不支持改变影子
>>>a.update([(1,3),(3,4)])
>>>b
{1:3,3:4} #原对象变影子也会变
```



## 流畅的Python的四章

#### 解码和编码字符串有两个通用

`string.encode(encoding = 'utf8' ,*errors = '...')` ==  `bytes(string , encoding = 'utf8',*errors = '...')`

`byte.decode(encoding = 'utf8')` == `str(byte , encoding= 'utf8')`



#### bytes码的注意事项

在IDLE上的bytes码实际上是16进制处理后8字节的每位二进制码 , 这样更有利于操作者一目了然具体有几个字节与字节的具体大小

因为`Unicode`编码和 `Ascll` 编码通用,所以英文的bytes编码就是它的`Ascll`码(它本身)



bytes方法还可以处理一个实现了缓冲协议的对象 (如 `bytes` , `bytearray` , `array.array`) , 将里面元素转化为相应的位数处理的例:

```python
>>>import array
>>>bytes(array.array('h',[1,2,3])) #h代表转化为16进制
b'\x01\x00\x02\03
```



#### 处理字符串

```python
>>>a = 'é'
>>>b = 'e\u0301'
>>>a == b
True #表明Python在处理变音符号字符时,是普通对应字符加上unicode编码

'''有时我们会将变音符号转化成普通字符'''
>>>import unicodedata
>>>def shave_marks(txt):
    normal_txt = unicodedata.normalize('NFD',txt) #用最多码位构成等价字符串
    shaved = ''.join(c for c in normal_txt if not unicodedata.combining(c)) #过滤掉Unicode字码
    return unicodedata.normalize('NFC',shaved) #用最少码位构成等价字符串

'''我们还可以利用casefold进行字符串的大小写折叠'''
```





## 第五章:一等函数



```Python
'''我们可以使用signature来观察函数的普通参数与关键字参数'''
>>>from inspect import signature
>>>def fun(i,j=9):
       pass
>>>sig = signature(fun)
>>>str(sig)
'(i,j=9)'
'''查看各个关键字参数的名字,默认参数'''
>>>for name,param in sig.parameters.items():
    print(param.kind,':',name,'=',param.default)
POSITIONAL_OR_KEYWORD : i = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : j = 9
```



我们还能利用函数里的 `__annotation__`提取函数里的注释

```python
>>>def fun(i:'str',j:'int > 0' = 8) -> str:
    pass
>>>fun.__annotations__
{'i': 'str', 'j': 'int > 0', 'return': <class 'str'>}
'''其中inspect模块中的signature能将注释单个提取出来,这里我们就不作过多介绍'''
```



在Python的operator模块中有许多预先设置好的函数 , 了解这些函数可以有效避免我们重复造轮

```Python
>>>import operator
'''itemgetter可以提取可迭代容器中的某个值,它一般用作根据单个容器中的某个值给容器群排序'''
>>>a = [1,2,3]
>>>b = '121'
>>>c = {1:2,3:4}
>>>d = operator.itemgetter(1) #也可以将多个位置传给它,此时它返回一个元组
>>>print(d(a),d(b),d(c))
2 2 1

'''相同的,attrgetter也可以得到一个对象的属性'''
>>>class a:
    b = 1
    c = 2
>>>operator.attrgetter('b','c')(a)
(1,8)
```



使用`partial`固定函数参数

```python
>>>from functools import partial
>>>from unicodedata import normalize
>>>be_smallest = partial(normalize,'NFC')
>>>string = 'cafe\u0301'
>>>be_smallest(string)
café
>>>be_smallest.func #查找partial内封存的函数
<built-in function normalize>
>>>print(be_smallest.args,be_smallest.keywords) #查找partial封存函数的参数与固定参数
('NFC',) {} #我们没有固定参数故为{}
```





