1. 检查字符串中或list中是否有某个字符：

   ```python
    x in string
    x in list
   ```

2. 检查字符串中或list中不含某个字符：

   ```python
    x not in string
   ```

3. 取反keyword: not (而不是js中的!)

4. 函数keyword parameter：

   ```python
   greet(name="Mini",msg="Hello")
   ```

5. 保留两位小数点：

   ```python
   "{:.2f}".format(num); round(num, 2)
   ```

6. condition list comprehension:

   ```python
    new_list=[new_item for item in list if test]
   ```

7. dictionary comprehension: 

   ```python
   new_dict={key:value for item in list}
   new_dict={new_key:new_value for (key,value) in dict.items() if test}
   ```


8. in windows for PyCharm using Powershell checking environement variables:

   ```
   dir Env:
   ```


9. create virtual env to isolate dependency conflict between projects

   ```
   python -m venv venv
   # 激活环境 (Mac/Linux)即可通过pip install -r requirements.txt命令安装txt里的依赖和指定版本
   source venv/bin/activate
   
   # 激活环境 (Windows PowerShell)
   venv\Scripts\activate
   ```
10. reverse array
```python
a = [10, 20, 30, 40, 50]
for item in reversed(a):
   print(item)

a = [1, 2, 3, 4, 5]
for item in a[::-1]:
   print(item)
   
s = "Python"
for i in range(len(s) - 1, 0, -1):
   print(s[i])

```
   