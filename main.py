#以下是Python3.0+的测试代码
#python空行也是程序代码的一部分。
""""""

'''
python的序列（元组、集合等）和字符串的处理按照“左闭右开”的原则
4654
1456
23213
'''
print(r"this is string \n",end="")      #不换行输出，python的写法
print("this","is","string")             #字符串连接

"""
x = "a"     #python2的写法
print x     #换行输出
print x,    #不换行输出
"""

"""
word = 'nihao'
sentence = "this is string"
print(word)
print(sentence)
"""

#字符串切片，左闭右开
str1 = '123456789'
val = 'nihao'
print(str1[0 : -1])                  #不包含-1
print(str1[-len(str1) : -1])          #不包含-1
print(str1[-len(str1) : -1] + '9')    #补齐‘9’,字符串可以用+运算符连接在一起
print(str1[2:7])                     #不包含七
print(str1[2:9:1])                   #输出3-9，步长为1
print(str1[0:9:2])                   #输出13
print(val * 2)                      #用*运算符重复两次
print(str1[2:])                      #打印第三个字符开始到末尾
print(str1[-1])                      #获取最后一个元素，类似于matlab中的end；
print(str1[:-1])                     #除了最后一个元素，获取其他所有的元素；

print(str1[::-1])                        #对第一个到最后一个元素进行倒序之后取出，步长为-1
print(str1[::])                          #步长默认为1
print(str1[5::-1])                       #对第一个到第n个元素进行倒序后取出，步长为-1
print(str1[5::])                         ##步长默认为1
print(str1[-1::-1])                      #全部元素倒序取出，步长为-1
print(str1[-1::])                        #步长默认为1

print('hello\nmlgbz')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nmlgbz')      # r指的是raw string

a, b, c = 1, True, "runoob"
print(a,b,c)
print(type(a),type(b),type(c))      #type()不会认为子类是一种父类类型
print(isinstance(a,int))
print(isinstance(b,int))            #bool是int类型的子类，isinstance()会认为子类是一种父类类型
#Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 issubclass 来判断类型。
print(issubclass(bool,int))          #issubclass(class, classinfo)方法用于判断参数 class 是否是类型参数 classinfo 的子类。

#input("\n\n按下 enter 键后退出。")

help('sys.stdout.write')
import sys
sys.stdout.write("wocaonima")        #只能输出一个字符串str

#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *

#argv即argument value的简写，是一个列表对象，其中存储的是在命令行调用 Python 脚本时提供的“命令行参数”
from sys import argv, path  # 导入特定的成员

#上一行的延续
print('================python from import\
===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
print(sys.path)

print(2 / 4)    #除法，浮点型
print(2 // 4)   #除法，整数
print(14 % 3)   #取余
print(2 ** 3)   #乘方

word = "Python"
print(word[0],word[5])
print(word[-6],word[-1],word[-4])

#比较运算符
print(4 > 2)
print(4 == 2)


#逻辑运算符
"""
在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，
只有 0、空字符串、空列表、空元组等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。
"""
#布尔型数据
print(True and False)
print(True or False)
print(not True)

#整型数据，先判断左，再判断右，左不满足，再返回右
efe = 123
dqd = 456
print(efe and dqd)      #与，如果 x为 False，x and y 返回 x 的值，否则返回 y 的计算值。
print(efe or dqd)       #或，如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
print(not efe)          #非，如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。

"""
list列表的使用
1、列表写在方括号之间，元素用逗号隔开。
2、和字符串一样，列表可以被索引和切片。
3、列表可以使用 + 操作符进行拼接。
4、与Python字符串不一样的是，列表中的元素是可以赋值改变的
你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项
"""
m = [2.0,'string',['a','b','c']]                    #列表的嵌套
n = [1,2,3]
print('m列表更新前的内容：',m)
print('访问第三个子列表的第三个元素：',m[2][2])        #嵌套列表的访问
m.append('刘')
m.append('六')
print('添加两个元素后的m列表：',m)
del m[3]                                        #删除列表第四个元素
print('删除第四个元素后的m列表：',m)
print(len(m))       #列表的长度

m[2] = 250
print('m列表第三个元素赋值后的内容：',m)
print(n[0],n[1],n[2])
print(m[0],m[1],m[2])
print(m)
print(m[0])
print(m[0:2])       #列表的截取，左闭右开，Python 的列表截取与字符串操作类似
print(m[2:])
print(n + m)        #列表的拼接
print('六' in m)    #元素是否在列表中
print(m * 2)        #列表的重复
for t in m:         #列表的迭代,默认间隔为换行
    print(t,end = ' ')   #设置为空格

u,v =2,3            #同时对多个变量赋值
print(u)
print(v)
print(2 + 3 /2.0)   #混合计算时，Python会把整型转换成为浮点数

#复数的表示
q = 2
w = 3
z = complex(q,w)
print(type(z))
print(z.real)   #复数的实部和虚部都是浮点型
print(z.imag)
print(type(q))
print(type(z))
print(complex(1))       #数字处理
print(complex("1"))     #字符串处理
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex("1+6j"))

#元组的表示
"""
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
元组中的元素类型也可以不相同
元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作数学运算符的括号使用
"""

tuple2 = (123,2.55,"hahaha",'nishishui')
tuple1 = ('nima',)
tup = ()                        #空元组
not_a_tuple = (42)              #一个普通的数字
print(not_a_tuple)
print(tuple[2],tuple[3])        #打印元组的元素
print(tuple2 + tuple1)           #连接两个元组

"""
Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
另外，也可以使用 set() 函数创建集合。
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

sites = {12,34,56,78,9}
if 12 in sites :
    print("12在集合中")
else :
    print("12不在集合中")

x = set("123456789t")
y = set("2468w")
print(x - y)        #x的差集
print(x | y)        #二者的并集
print(x & y)        #二者的交集
print(x ^ y)        #两个集合的交集的（补集），两集合中不同时存在的元素

#字典的表示
"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""
"""
数字类型用作键时遵循数字比较的
一般规则:如果两个数值相等(例如 1和1.0)则两者可以被用来索引同一字典条目。
(但是请注意，由于计算机对于浮点数存储的只是诉似值，因此将其用作字典键是不明智的。)
"""
dict1 = {}               #创建一个空字典
dict1['one'] = 666       #空字典中创建字典的键和对应的值
dict1[2] = "nima"        #数字不建议作为键名
print(dict1['one'])
print(dict1[2.0])        #数字不建议作为键名
print(dict1[2])          #数字不建议作为键名

dict6 = {"英语":80,"数学":100,"物理":150}
dicttest = {1:"吃饭",2:"拉屎",3:"睡觉"}
print(dict6["英语"],dict6["数学"],dict6["物理"])      #输出键名对应的值
print(dicttest[1],dicttest[2],dicttest[3])          #输出键名对应的值
print(dict6)           #输出完整的字典
print(dict6.keys())    #输出键名
print(dict6.values())  #输出所有值

#字典构建函数dict()
dict2 = dict([(1,"刘"),(2,"兴"),(3,"恩")])
print(dict2)
print(dict2[1],dict2[2],dict2[3])

#bytes类型的数据的定义方式
oicban = bytes("liuxingen",encoding="utf-8")
gufg = b"2345"
print(oicban)       #二进制数
print(gufg)
#ord() 函数用于将字符转换为相应的整数值。
if oicban[2] == ord('u'):
    print("this letter is u")
else:
    print("this letter is not u")
"""
py3的数据类型转换
"""
#int() 函数用于将一个字符串或数字转换为整型。
print(type(int('100',16)))    #默认为十进制
print(type(int('12')))
#float() 函数用于将整数和字符串转换成浮点数。
print(type(float(666)))
#将对象x转换为字符串
print(type(str(1236)))
print(hex(100))

#隐式类型转换
num1 = 123
num2 = 1.6
print(num1 + num2)

#repr() 函数将对象转化为供解释器读取的形式。
dit_iw = {1:'wo',2:'shi',3:'ni',4:'die'}    #将一个字典转化为字符表达式
print(type(repr(dit_iw)))

#eval() 函数将字符串转换为相应的对象，并返回表达式的结果。
wad = 2
print(eval("pow(2,wad)"))

#tuple() 可以将字符串，列表，字典，集合转化为元组；（集合可变，元组不可变）
print(tuple('wnm'))                             #这是字符串
print(tuple({"111":222,"333":444,"555":666}))   #这是字典字典，只保留键名
print(tuple({1,3,'w','r'}))                     #这是集合
print(tuple({1,2,3,4,5}))                       #这是也是集合
print({1,2,3,4,5})                              #这是元组

tuple_cia = {12,'dsd',11,45}                    #创建一个不可变的元组
print(type(list(tuple_cia)))                    #元组转换为元素可变的列表

str_aaa = "wo lei ge sao gang"                  #创建一个字符串
print(list(str_aaa))                            #字符串转换为可变列表，列表用[]圈起来

dict_wer = dict(x = 1,y = 2,z = 3)               #关键字参数创建字典
print(dict_wer)                                  #打印键名和字典

dict_uiy = dict(zip(['ni','hao','a'],[11,22,33]))         #映射方式创建字典，两列表打包映射为字典
print(dict_uiy)

#frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
#set(),转变为可变合集
#集合可以使用大括号{ }创建
print(frozenset([1,56,58,'we']))
print(set('liuxingen'))

#chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
#数值为10进制或16进制
print(chr(48),chr(97))
print(chr(0x30),chr(0x61))          #0x30 => 3*(16^1) + 0*(16^0) = 48

#ord(),返回字符对应的 ASCII 数值
print(ord('0'),ord('a'))

#hex()返回16进制数，以字符串形式表示
print(hex(255),type(hex(255)))

#海象运算符:=，这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增运算符。
"""
variable := expression，
其中，expression 是一个任意的表达式，而 variable 则是一个变量名。
该运算符允许将表达式的结果赋值给变量，并且在同一行中进行这两个操作。
在某些情况下，使用海象运算符可以使代码更加简洁、易读和高效。
例如，当你需要反复计算一个值并检查它是否满足某种条件时，可以使用海象运算符来减少重复代码。
"""
#写法1
huafs1 = 15
if huafs1 > 10:
    print('Not a walrus operator')
#写法2
if huafs2 := 15 > 10:       #赋值的同时进行比较
    print('It‘s a walrus operator')

"""位运算符"""
#整数二进制位与，或运算符，或者集合set的交并补差
fjj = 10            #1010,2^3+2
dj = 8              #1000,2^3
print(fjj & dj)     #与，依然是1000，2^3 = 8
print(fjj | dj)     #或，1010，2^3 + 2^1 = 10
#”^“异或运算符，相异为1，相同为0
print(fjj ^ dj)         #0010,2

"""
”~“按位取反运算符：对数据的每个二进制位取反，1变0，0变1
二进制数在内存中以补码的形式存储！！！
正数原反补一样，正数的反码和原码一样，负数的反码就是在原码的基础上符号位保持不变，其他位取反。
"""
"""
<<：左移是将一个二进制操作数对象按指定的移动位数向左移，左边溢出的位数（高位）被丢弃，右边的空位（低位）用0补充。
（高位丢弃低位补0）
左移相当于乘以2的幂次。∫将一个运算对象的各二进制位，全部左移若干位（左边的二进制丢弃，右边补0）
"""
"""
>>：右移是将一个二进制操作数对象按指定的移动位数向右移，右边溢出的位数被丢弃，正数时左边的空位用0补充，
负数时则左边的空位用1补充。右移相当于除以2的幂次。将一个运算对象的各二进制位全部右移若干位，正数左补0，负数左补1.
"""
print(~fjj,bin(~fjj))                 #~x取反操作后得到整数-(x+1)
print(fjj >> 1,bin(fjj >> 1))         #1010->0101右移一位
print(fjj << 1,bin(fjj << 1))         #10100,2^4 + 2^2 = 20,左移一位,左溢丢，右0补

#abs()返回一个负数
print(abs(-156))

#ceil(x) 函数返回一个大于或等于 x 的的最小整数。
import math
print(math.ceil(3.2))

#floor(x),返回数字的下舍整数
print(math.floor(6.9))

#exp(x)	返回e的x次幂(e^x),如math.exp(1),返回2.718281828459045
print(math.exp(1))


#fabs()以浮点数形式返回数字的绝对值
print(math.fabs(-223))

#log() 方法返回x的自然对数（以e为底）,x>0
print(math.log(math.exp(1)))

#log10(x),返回以10为基数的x的对数，如
print(math.log10(10 ** 6))

"""
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
"""
print(max(12,25,4,86,44))
print(min(12,25,4,86,44))

#modf(x),返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print(math.modf(100.32))

#pow(x, y)	x**y 运算后的值。
print(pow(2,3),2 ** 3)

"""
round(x [,n])	
返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。
其实准确的说是保留值将保留到离上一位更近的一端。
"""
print(round(2.5658,2))

#sqrt()方法返回数字x的平方根。
print(math.sqrt(9))

#choice() 方法返回一个列表，元组或字符串的随机项。
import random
print(random.choice(range(50)))
print(random.choice([11,'ni',22,65]))
print(random.choice('imaliuxingen'))

#randrange(开始，结束，步长) 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
print(random.randrange(1,100,2))
print(random.randrange(100))

#shuffle()，所有元素随机排序。
hds = [1,2,3,4,5,6,7,8,9]
random.shuffle(hds)     #打乱排序
print(hds)              #打印排序后的列表

#uniform() 方法将随机生成一个随机浮点数，它在 [x,y] 范围内。
print(random.uniform(2,10))

"""
实例省略
Python包括以下三角函数：
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
"""

"""
进度百分比效果
import time
for i in range(101):
    print("\r{:3}%".format(i),end=' ')
    time.sleep(0.05)
"""

print("\110","\x48")    #\yyy八进制，\xyy十六进制
print("l" in "liu")
print("l" in "L")
print(5 not in [1,2,3,4,5])

#详见python3字符串格式化符号
water = 122
print("%s传感器数据是 %d mL" % ("流量",water))

shili = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (shili)

"""
f-string 格式化字符串以 f 开头，后面跟着字符串，
字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
"""
name = 'Runoob'
print(f'Hello {name}')

"""
以下函数详见Python的字符串内建函数
"""
#首字母大写
abakd = "ni cai wo shi shui?"
print(abakd.capitalize())

#返回一个指定的宽度width居中的字符串，如果 width小于字符串宽度直接返回字符串，否则使用 fillchar去填充。
nbc = "qwertyui"
print(nbc.center(20,'*'))
print(nbc.center(8,'*'))

#该方法返回子字符串在字符串中出现的次数。
vbvn = 'my name is liuliuliu'
sc = 'u'
print(vbvn.count(sc))


"""
bytes.decode(encoding="utf-8", errors="strict")
encoding -- 要使用的编码，如"UTF-8"。
errors -- 设置不同错误的处理方案。
decode()方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
encode() 方法对原字符串进行编码
UTF-8 是一种国际化的编码方式，包含了世界上大部分的语种文字（简体中文字、繁体中文字、英文、日文、韩文等语言），
也兼容 ASCII 码。
GBK 是在国家标准 GB2312 基础上扩容后兼容 GB2312 的标准（好像还不是国家标准），
专门用来解决中文编码的，是双字节的，不论中英文都是双字节的。
"""
fhf = 'nihaoliuxingen'
tut = fhf.encode('utf-8')
pop = fhf.encode('gbk')
print(tut)
print(pop)
print(tut.decode('utf-8','strict'))
print(pop.decode('gbk','strict'))


#append() 方法用于在列表末尾添加新的对象。
#pop()从队列的开头删除元素并返回
shd = ['ni',1,'hao',2,'a','ha']    #创建一个列表
shd.append('22')
shd.append(66)
shd_delete = shd.pop(1)
print(shd_delete)       #返回这个删除的元素
print(shd)              #返回操作后的列表

#endswith()方法语法：
#str.endswith(suffix[, start[, end]]),字符的开始和结束，end为字符串的长度
shsj = "today is Wednesday!"        #0-18，19个字符
print(shsj.endswith('!'))           #最后一个字符
print(shsj.endswith('!',0,len(shsj)))
print(shsj.endswith('is',0,8))

#tabsize -- 指定转换字符串中的 tab 符号 \t 转为空格的字符数。
dggd = 'zheshi\tyige\tzifuchaun'
print(dggd)
print(dggd.expandtabs())    #默认以8个字符为一组
print(dggd.expandtabs(1))   #以1个字符为一组
print(dggd.expandtabs(2))   #以2个字符为一组，zh/es/hi/  /yi/ge/  /zi/fu/ch/au/n
print(dggd.expandtabs(3))   #以3个字符为一组，zhe/shi/   /yig/e  /zif/uch/aun
print(dggd.expandtabs(4))   #以4个字符为一组，zhes/hi  /yige/    /zifu/chau/n
print(dggd.expandtabs(5))   #以5个字符为一组
print(dggd.expandtabs(6))   #以6个字符为一组
hgjg = dggd.expandtabs(6)
print(hgjg.find(' '))

#str.find(str, beg=0, end=len(string)),len()为字符串长度
"""
检测 str 是否包含在字符串中，如果指定范围 beg 和 end 
则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
"""
hfjk = "ni hao wo you yi ge mao shan"
jkjk = 'you'
print(len(hfjk))        #返回字符长度28个
print(hfjk.find(jkjk))  #0-10,返回起始的索引值

#index()和find()类似,如果包含子字符串返回开始的索引值，否则抛出异常。
hfjk = "ni hao wo you yi ge mao shan"
jkjk = 'hao'
print(hfjk.index(jkjk))
#str.isalnum() 方法检测字符串是否由字母和数字组成,如果没有其他字符，空格等返回True
jkjl = "2345qwerty????"     #包含其他符号“？”
dha = "6666weqe"
print(jkjl.isalnum())
print(dha.isalnum())

#str.isalpha(),如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。
kl = 'sld你好'
ko = "我有一个梦"
kj = "haha哈哈123"
print(kl.isalpha())
print(ko.isalpha())
print(kj.isalpha())

#str.isdigit(),字符串是否全为数字
hjj = 'nihao111'
dskf = '8956'
print(hjj.isdigit())
print(dskf.isdigit())

#str.islower()方法检测字符串是否由小写字母组成。
jidh = 'abcdef'
sjfi = 'Abcde'
print(jidh.islower())
print(sjfi.islower())

#isnumeric() 方法检测字符串是否只由数字组成，
#数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。指数类似²与分数类似½也属于数字。
"""
\ u 为unicode 码；
一般其后跟 4 个 16 进制数，因此，一般为 unicode-16
Python：字符串的decode和encode成员函数，可对其进行转换
"""

cbn = '一2三²\u0030'          #0030为Unicode字符‘0’
print(cbn.isnumeric())

hjh = "\u0030"          #unicode字符对照表，https://symbl.cc/cn/unicode-table/#basic-latin
print(hjh.encode())
print('\U0001F601')

#str.isspace() 方法检测字符串是否只由空白字符组成。
ncj = '    '
print(ncj.isspace())

#title(),将字符串进行标题化
#istitle()，如果字符串是标题化的(见 title())则返回 True，否则返回 False
sdj = 'my name is jarvis'
sdjj = sdj.title()
print(sdjj)
print(sdjj.istitle())

#str.isupper() 方法检测字符串中所有的字母是否都为大写。
saf = 'I am liuxingen'
saff = 'I AM LIUXINGEN'
print(saf.isupper())
print(saff.isupper())

#序列是一个统称，包括列表元组字符串等
#str.join(seq)方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#str:指定连接的字符，seq:要连接的序列
yut = '*'
yuut = ('l','i','u','x','i','n','g','e','n')        #创建一个元组
print(yut.join(yuut))

#str.ljust(width[, fillchar])方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。fillchar默认为空格。
#如果指定的长度小于原字符串的长度则返回原字符串。
#rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
asd = 'abcdef'
print(asd.ljust(10,'-'))
print(asd.rjust(10,'+'))
print(asd.ljust(4,'*'))


# str.lower()方法转换字符串中所有大写字符为小写。
sss = 'ABCD'
print(sss.lower())

#strip()方法用于移除字符串头尾指定的字符（默认为空格）或字符序列,该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#str.lstrip([chars]),chars --指定截取的字符,默认为空格。
#rstrip() 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。
jkl = '@@@@@the key information@@@'
print(jkl.lstrip('@'))
print(jkl.rstrip('@'))
print(jkl.strip('@'))

"""
str.maketrans(x[, y[, z]])
创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标
使用str.translate()方法将映射关系应用到字符串
translate()函数做的就是接收一个映射表，然后把字符串中含有的映射表的键全都换成映射的值。
"""
tuo = 'liuxingen'
str_relate = tuo.maketrans('aeiou','12345')   #代表一个映射关系
print(tuo.translate(str_relate))              #将映射关系应用于字符

#max(str)方法返回字符串中最大的字母，比较的是ascii码表中的一个值。
#min(str)方法返回字符串中最小的字母
print(max('ZSdfg'))         #在有大小写的字符串中返回的是小写字母的最大值。
print(max('ASDFGZ'))
print(max('xhshl'))

"""
str.replace(old, new[, max])
三个参数，old是需要替换的值，new是替换后的值，max是最多替换的次数
如果指定第三个参数max，则替换不超过max次。
"""

hkh = '我身体的每个朝向，\n都是你。\n我站着不动，\n世界上最大的风口，\n就是我的心脏。'
print(hkh.replace('你','远方'))
hk = '我身体的每个朝向，\n都是远方。\n我站着不动，\n世界上最大的风口，\n就是我的心脏。'
print(hk.replace('我','你',2))        #三个‘我’，只替换两次，最后一个‘我’不替换


"""
str.rindex(str, beg=0 end=len(string)),从右侧开始查找
rindex() 返回子字符串 str 在字符串中最后出现的位置，
如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
"""
hjds = 'Said I have been there'
print(len(hjds))                    #0-21，22个字符串
print(hjds.rindex('there',0,22))    ##左闭右开，不包含最后一个字符（最后一个是空字符）

#str.rfind(str, beg=0, end=len(string))，从右侧开始查找
#rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1
print(hjds.rfind('been',0,16))      #左闭右开，不包含最后一个字符

"""
str.split(str="", num=string.count(str))
split() 方法通过指定分隔符对字符串进行切片，该方法将字符串分割成子字符串并返回一个由这些子字符串组成的列表。
如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
split()方法特别适用于根据特定的分隔符将字符串拆分成多个部分。
"""
bju = 'if you are a dog'
print(bju.split())
print(bju.split(' ',2))     #只分隔两次

"""
splitlines() 按照行('\r', '\r\n', \n')分隔，
返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
\r ：将当前位置移到本行开头。又叫回车，对应键盘上的return键
\n：将当前位置移到下一行开头。又叫换行，newline。
"""
biu = "fang\rfunny\n\rmade\r\nmuddy\npi\rpee"
print(biu.splitlines(True))     #保留回车换行符

"""
str.startswith(substr, beg=0,end=len(string));
startswith() 方法用于检查字符串是否是以指定子字符串开头，
如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
"""
jiji = '无底深渊，前程万里'
print(jiji.startswith('里',8,9))

#swapcase() 方法用于对字符串的大小写字母进行转换，即将大写字母转换为小写字母，小写字母会转换为大写字母。
nji = 'YOU are my best FRIEND'
print(nji.swapcase())

#upper() 方法将字符串中的小写字母转为大写字母。
print(nji.upper())

#str.zfill(width)方法返回指定长度的字符串，原字符串右对齐，前面填充0。
lkj = 'this is string'
print(lkj.zfill(18))    #长度18个字符

#isdecimal()方法检查字符串是否只包含十进制字符。
bgt = '12345560x30'
rfv  ='111222333'
print(bgt.isdecimal())
print(rfv.isdecimal())




