from mmengine.config import read_base

with read_base():
    # choose a list of datasets
    from .datasets.mmlu.mmlu_gen import mmlu_datasets
    # output the results in a choosen format
    from .summarizers.groups.mmlu import mmlu_summary_groups
    # choose a model of interest

from opencompass.models import HuggingFaceCausalLM
datasets=[*mmlu_datasets]
# summarizer=mmlu_summary_groups
models = [
    dict(
        type=HuggingFaceCausalLM,
        # 以下参数为 HuggingFaceCausalLM 的初始化参数
        path='/root/InternLM-813/L1/xtuner/Shanghai_AI_Laboratory/internlm2-chat-1_8b',
        tokenizer_path='/root/InternLM-813/L1/xtuner/Shanghai_AI_Laboratory/internlm2-chat-1_8b',
        # tokenizer_kwargs=dict(padding_side='left', truncation_side='left'),
        max_seq_len=2048,
        # 以下参数为各类模型都必须设定的参数，非 HuggingFaceCausalLM 的初始化参数
        abbr='internllm-1.8b',            # 模型简称，用于结果展示
        max_out_len=100,            # 最长生成 token 数
        batch_size=16,              # 批次大小
        run_cfg=dict(num_gpus=1),   # 运行配置，用于指定资源需求
        model_kwargs={"trust_remote_code":True,"device_map":'auto'},
        tokenizer_kwargs={"trust_remote_code":True}
    )
]

# summarizer = dict(
#     dataset_abbrs=[
#         ['mmlu', 'naive_average']
#     ],
#     summary_groups=sum(
#         [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
# ) 
    