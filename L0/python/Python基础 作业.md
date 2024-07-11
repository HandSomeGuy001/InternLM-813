在Vscode中，可通过在代码文件中加入断点的方式对程序进行调试，如下图所示：  
Python Debug界面:
![[attachments/python_debug_button.png]]  
此处对比进行标点符号去除前后的字符串  
![[attachments/l0_python_before_remove.png]]

可看到运行标点符号去除后，字符串变量中没有标点符号  
![[attachments/l0_python_after_remove.png]]

最后附上运行结果 ：
```bash
(base) root@intern-studio-50088800:~# python wordcount.py 
{'got': 2, 'thi': 1, 'panda': 1, 'pluh': 1, 'toy': 1, 'for': 3, 'my': 1, 'daughter': 1, 'birthday': 1, 'who': 1, 'love': 1, 'it': 8, 'and': 3, 'take': 1, 'everywhere': 1, 'oft': 1, 'uper': 1, 'cute': 1, 'face': 1, 'ha': 1, 'a': 3, 'friendly': 1, 'look': 1, 'bit': 1, 'mall': 1, 'what': 1, 'i': 4, 'paid': 1, 'though': 1, 'think': 1, 'there': 1, 'might': 1, 'be': 1, 'other': 1, 'option': 1, 'that': 1, 'are': 1, 'bigger': 1, 'the': 1, 'ame': 1, 'price': 1, 'arrived': 1, 'day': 1, 'earlier': 1, 'than': 1, 'expected': 1, 'o': 1, 'to': 2, 'play': 1, 'with': 1, 'myelf': 1, 'before': 1, 'gave': 1, 'her': 1}

```
