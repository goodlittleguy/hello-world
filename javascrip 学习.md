## javascrip 学习

>   javascrip 的字典的键必须为字符串,此时为了创建键也可为其他格式的映射对象,我们可以使用Map

```javascript
var m = new Map([[1,2],['sex','boy'],]);
m.get(1);
2
m.set('age',12); #为map添加元素
m.delete('age'); #删除元素
```



当然我们还有 set 集合对象

```JavaScript
var s = new Set([1,1,2,3]);
s; // set {1,2,3}
s.add(4); //为set添加元素
s.delete(4); //删除元素
```



>   iterable 对象可以使用 `for of` 方法得到对像的值
>
>   而 `for in `方法得到的是对象的属性

```javascript
var iter = [1,2,3];
iter.name = 'boy';
for(var i in iter){
    console.log(i) //这时遍历出i的值是iter的属性 0,1,2,name 
}
for(var i of iter){
    console.log(i) //遍历出的是iter的value即 1,2,3
}
```



当然我们还有更好的方法遍历 iterable 对象, 就是使用forEach方法

```javascript
#标准格式
set_object = new Set([1,2,3]);

map_object.forEach(function (value,key ,map){
    console.log(key + ' value is ' + value);
}); 
//这时显示出来的是 sex value is boy ....

map_object = new Map([['sex','boy'],['age',12]]);

set_object.forEach(function (value,index ,set){
    console.log(value + ' index is ' + index);
}); 
//结果是 1 index is 0 ....

//list 的 foreach 的参数是 value,samevalue,list 这里就不作介绍了

#当然JavaScript不要求参数全部补齐,故我们也可以仅仅写出我们需要的参数
```







### 函数

###### 关键字

`arguments`

>   它只在函数内部起作用，并且永远指向当前函数的调用者传入的所有参数

```javascript
function foo(x) {
    console.log(x) //显示出第一个参数
    for(var i=0;i<arguments.length;i++){
        console.log(arguments[i] + "'s index is'" + i);
    }
}
foo('a','b','c')
//这时候显示出 a 
//a's index is 0 
//b's index is 1 ....
```



`rest`

>   rest是定义在函数的参数, 表示其余的参数,在使用时要注意在前面加入 "..." 

```javascript
function foo(a,b,...rest){
    for(var i of rest){
        console.log(i)}
}
foo(1,2,3,4)
//3,4
```



#### 变量作用域

javascript 在 执行函数时,会先将所有声明变量的函数提升到函数顶部,但注意:**是提升了变量的声明，但不会提升变量的赋值**。

```JavaScript
function foo(){
    var x='hello ,'+y;
    console.log(x);
    var y = 'world';
}
//结果不会报错,但会显示 hello ,undefined
```

故我们应严格遵守,**所有变量首先声明**原则



不在函数定义体中定义的变量就是全局变量 , 实际上所有的全局变量都是`Window` 的属性

```javascript
var a = 'hello';
console.log(window.a); //返回hello

window.alert(a) //浏览器显示 hello

function foo(){
    console.log('hello')
}
window.foo() //返回hello
```



如果我们不同的JavaScript文件使用了名字相同的全局变量, 由于所有的全局变量都绑定在`window`上,这样会造成**命名冲突**

我们可以自己定义一个全局变量来有效避免这种情况

```JavaScript
var global_var = {};
global_var.name = "burry";

global_var.foo = function (){
    return 'foo';
} 
```



`for`循环中的局部作用域

我们在`for`循环中无法用`var`定义局部作用域 , 但我们可以使用`let` 定义

```JavaScript
function foo(){
    for(let i=0;i<2;i++){}
    console.log(i); //此时因为i为循环变量里的局部作用域,故出了循环体后浏览器报错,显示 i 还未定义
}
```



使用`const`关键字声明常量

```JavaScript
const PI = 3,14;
PI = 3.145 ;//此时报错
```



#### 元素的解构赋值

我们可以像 `Python`拆包一样对JavaScript进行解构赋值

```JavaScript
[var x,var y] = ['hello','javascript']; //得到预想值


{name,age} = {name:'小明',age:12}; //系统报错,因为JavaScript将 { 开头的语句当块处理,此时将其整体用 () 围起来即可
//其中name和age虽为变量,但必须与字典的键值相同

```



高级用法:

```JavaScript
[,var y] = ['hello','javascript']; //单独得到后面值

[,,[,var y]] = [1,2,[3,4]] //拆包需与原容器格式对应


{name,age:thing} = {name:'小明',age:12}; //此时即可将变量名不是键名的 thing 赋值 12 ,而中间的age显示 undefined

{name,sex='男'} = {name:'小明'}; //如果容器没有sex键,则默认变量名sex为男
```





### 方法

在一个对象中绑定函数,就称为该对象的方法

方法中有一个 `this`参数 , 它始终指向该对象 , 该参数如果是在函数里用的话 , 则指向`windows`

```javascript
var prerson = {
    birth : 2000,
    age : function(){
        var y = new Date().getFullyear(); //得到当前年数
        return y - this.birth; //this 在方法中指代 person
    },
}

person.age // 显示为20岁

//当我们将含 this 的 person.age 方法赋给一个变量,该变量无法得到得到值:
var fun = person.age; 
fun(); //在strict条件下直接报错,非strict条件返回NaN

'''所以利用 this 应慎之又慎,该必要情况下,先用一个 that 变量保存this在此情况下所指代的对象,后使用 thar 变量'''
```



使用 `apply`指定函数中的 `this`指向

```javascript
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth; //正常情况下 this 指向 windows
 }
getage() //返回NaN

var person{
    birth : 2000,
}
getage.apply(person,[]); //这下apply方法将this指向person对象,后面是可能用到的参数,参数要用列表表示
    
    
'''还有与apply功能相同的call方法,只是该方法的参数不用用[]括起来'''

Math.max.apply(null,[1,2,3]) //当我们对普通函数调用时,通常把this改为null
//该函数与 Math.max.call(null,1,2,3) 和 Math.max(1,2,3) 功能相同
    

```



JavaScript也像Python一样能使用高阶函数

```JavaScript
function foo(a,Math.abs){
    return Math.abs(a);
}
```





`map/reduce`方法

Javascript 中的这两个方法还是与Python完全相同

```javascript
'''我们先将字符串'1234'变为array,再将其转化为Number函数'''
function toNumber(s){
    var arr = s.split('').map(x => x*1); //先将其变元素为数字的为array,当然我们还可以使用 Number(x) 或 parseInt(x) 直接将元素变为数字
	return arr.reduce((x,y) => x*10 + y); //
    
}
```

