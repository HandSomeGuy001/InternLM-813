import json
import matplotlib.pyplot as plt
# 打开并读取JSON文件
loss_dadap = []
with open('/root/InternLM-813/L2/InternVL/work_dir/diy_config/20240827_085434/vis_data/20240827_085434.json', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)  # 此时 line 是一个单独的 JSON 对象
        # 执行你需要的操作，例如获取 'lr' 字段
        loss = data.get('loss', None)
        print('loss的值是：', loss)
        loss_dadap.append(loss)
plt.figure()
plt.plot(loss_dadap,label='Dadap')
loss_adam=[]
with open('/root/InternLM-813/L2/InternVL/work_dir/internvl_qlora_ft/20240827_063210/vis_data/20240827_063210.json', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)  # 此时 line 是一个单独的 JSON 对象
        # 执行你需要的操作，例如获取 'lr' 字段
        loss = data.get('loss', None)
        print('loss的值是：', loss)
        loss_adam.append(loss)

plt.plot(loss_adam,label='Adam')

plt.title('Loss Curve')
plt.xlabel('Iterations /10')
plt.ylabel('Loss')
plt.legend()
plt.savefig("./Dadap_loss.jpg")