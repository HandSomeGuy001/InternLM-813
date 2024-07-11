#### 闯关任务 完成SSH连接与端口映射并运行`hello_world.py`

首先上结果图：
![](../../attachments/l0_hello_world.png)

##### 任务要求：
用SSH实现端口映射，在本地机上访问开发机运行的Web服务；

>什么是SSH？
>SSH，全称为 Secure Shell，是一种加密的网络协议，用于安全地访问远程计算机。它通常用于登录到服务器、执行远程命令、传输文件等。SSH 通过加密方式保护数据传输过程中的安全性，防止数据在传输过程中被窃听或篡改。
>关于SSH端口映射？
>SSH 本身并不直接支持端口映射，但是可以通过 SSH 隧道（也称为端口转发）来实现类似功能。SSH 隧道允许你将本地计算机上的端口转发到远程服务器上的端口，从而可以安全地访问远程服务器上的服务。

操作流程：
**本地机**运行：
```powershell
PS C:\Users\HndsGuy> ssh -p 44145 root@ssh.intern-ai.org.cn -CNg -L 7860:127.0.0.1:7860 -o StrictHostKeyChecking=no
```
创建一条SSH隧道，将发送到本地端口（7860）的流量转发到开发机上的127.0.0.1：7860端口；
**开发机**运行：
```shell
(base) root@intern-studio-50088800:~# python hello_world.py 
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
```

后在本地访问`127.0.0.1:7860`即可查看到网页！


