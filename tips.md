1.在类函数中写self.xxx = yyy 这个变量就是类实例的属性，不是类的属性。没有self就是这个方法的临时变量
```python
class Test(object):
    def __init__(self):
        self.a=1
        b=2
```
\>\>\>test = Test()  
\>\>\>test.a   输出1  
\>\>\>test.b   报错,无该属性  


2. 在python中res.append(path),是将此path对象加入res,后续path改变时，res中的path也会变正确做法  
Python: **res.append(list(path))**  
JAVA: **res.append(new LinkedList(path))**  
C++: **res.push_back(path)**  
