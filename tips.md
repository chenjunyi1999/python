在python中res.append(path),是将此path对象加入res,后续path改变时，res中的path也会变  
正确做法  
Python: **res.append(list(path))**  
JAVA: **res.append(new LinkedList(path))**  
C++: **res.push_back(path)**  
