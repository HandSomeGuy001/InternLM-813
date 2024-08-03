# OpenCompass 评测 InternLM-1.8B 实践
这把没有参考教程，所以记录实现过程  
### 实现过程

首先安装OpenCompass
> 官方GitHub仓库的Installation
```bash
conda create --name opencompass python=3.10 pytorch torchvision pytorch-cuda -c nvidia -c pytorch -y
conda activate opencompass
git clone https://github.com/open-compass/opencompass opencompass
cd opencompass
pip install -e .
```

因为之前demo环境用的很好，所以本次还是在demo环境下进行复现，clone下仓库后直接安装 
```bash
(demo) root@intern-studio-50088800:~/InternLM-813/OpenCompass/opencompass pip install -e .
```

首先准备数据集  
```bash
(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass# mkdir data
(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass# cd data
(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass/data# wget https://github.com/open-compass/opencompass/releases/download/0.2.2.rc1/OpenCompassData-core-20240207.zip

(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass/data# unzip OpenCompassData-core-20240207.zip 
```
如果开发机太慢，可以在自己的设备上下好这个数据集，然后上传到开发机解压

解压后的文件是**data文件夹**，需要将其移动到opencompass目录，或者直接在opencompass目录下解压（     

为避免出现错误
```bash
Error: mkl-service + Intel(R) MKL: MKL_THREADING_LAYER=INTEL is incompatible with libgomp.so.1 library.
```
请运行  
```bash
(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass# export MKL_THREADING_LAYER=GNU
(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass# export MKL_SERVICE_FORCE_INTEL=1
```

根据[QuickStart文档](https://opencompass.readthedocs.io/zh-cn/latest/get_started/quick_start.html)，
有两个配置比较重要  
一个是模型model，一个是评测数据集dataset,将这两个配置写入配置文件中，使用run.py脚本进行调用即可。  
**注意** 配置文件要放在configs文件夹下   
[配置文件](./intern_1_8_mmlu.py)
运行
```bash
(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass# python run.py configs/eval_intern_1_8_mmlu.py 
```
