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

   