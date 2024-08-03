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
日志，推理结果，见 opencompass/outputs/default/\$YOUR_RUN_TIME\$  
[推理结果example](./lukaemon_mmlu_college_biology.json)
***
跑这个要好久（  
经过一夜的推理，还是有很多任务没有跑完，受不了，直接Ctrl+C  
后运行命令
```bash
(demo) (base) root@intern-studio-50088800:~/InternLM-813/L1/OpenCompass/opencompass# python run.py configs/eval_intern_1_8_mmlu.py -m eval -r /root/InternLM-813/L1/OpenCompass/opencompass/outputs/default/20240803_222642
```
依据现有推理结果进行推理，-m 设置model为eval验证模式，-r设置依赖工作路径  
[推理结果](./summary_20240804_064917.txt)
```bash\
dataset                                            version    metric    mode    internllm-1.8b
-------------------------------------------------  ---------  --------  ------  ----------------
lukaemon_mmlu_college_biology                      caec7d     accuracy  gen     50.69
lukaemon_mmlu_college_chemistry                    520aa6     accuracy  gen     32.00
lukaemon_mmlu_college_computer_science             99c216     accuracy  gen     43.00
lukaemon_mmlu_college_mathematics                  678751     accuracy  gen     33.00
lukaemon_mmlu_college_physics                      4f382c     accuracy  gen     27.45
lukaemon_mmlu_electrical_engineering               770ce3     accuracy  gen     44.14
lukaemon_mmlu_astronomy                            d3ee01     accuracy  gen     48.68
lukaemon_mmlu_anatomy                              72183b     accuracy  gen     44.44
lukaemon_mmlu_abstract_algebra                     2db373     accuracy  gen     31.00
lukaemon_mmlu_machine_learning                     0283bb     accuracy  gen     32.14
lukaemon_mmlu_clinical_knowledge                   cb3218     accuracy  gen     48.68
lukaemon_mmlu_global_facts                         ab07b6     accuracy  gen     22.00
lukaemon_mmlu_management                           80876d     accuracy  gen     64.08
lukaemon_mmlu_nutrition                            4543bd     accuracy  gen     45.42
lukaemon_mmlu_marketing                            7394e3     accuracy  gen     64.96
lukaemon_mmlu_professional_accounting              444b7f     accuracy  gen     34.40
lukaemon_mmlu_high_school_geography                0780e6     accuracy  gen     55.05
lukaemon_mmlu_international_law                    cf3179     accuracy  gen     52.89

```

