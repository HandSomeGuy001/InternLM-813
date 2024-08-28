accumulative_counts = 2
batch_size = 12
betas = (
    0.9,
    0.999,
)
custom_hooks = [
    dict(
        tokenizer=dict(
            pretrained_model_name_or_path=
            '/root/InternLM-813/L2/InternVL/InternVL2-2B',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.engine.hooks.DatasetInfoHook'),
]
data_path = '/root/InternLM-813/L2/InternVL/CLoT_cn_2000/ex_cn.json'
data_root = '/root/InternLM-813/L2/InternVL/CLoT_cn_2000/'
dataloader_num_workers = 4
default_hooks = dict(
    checkpoint=dict(
        by_epoch=False,
        interval=1000,
        max_keep_ckpts=1,
        save_optimizer=False,
        type='mmengine.hooks.CheckpointHook'),
    logger=dict(
        interval=10,
        log_metric_by_epoch=False,
        type='mmengine.hooks.LoggerHook'),
    param_scheduler=dict(type='mmengine.hooks.ParamSchedulerHook'),
    sampler_seed=dict(type='mmengine.hooks.DistSamplerSeedHook'),
    timer=dict(type='mmengine.hooks.IterTimerHook'))
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
image_folder = '/root/InternLM-813/L2/InternVL/CLoT_cn_2000/'
launcher = 'none'
llava_dataset = dict(
    data_paths='/root/InternLM-813/L2/InternVL/CLoT_cn_2000/ex_cn.json',
    image_folders='/root/InternLM-813/L2/InternVL/CLoT_cn_2000/',
    max_length=8192,
    model_path='/root/InternLM-813/L2/InternVL/InternVL2-2B',
    template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
    type='xtuner.dataset.InternVL_V1_5_Dataset')
load_from = None
log_level = 'INFO'
log_processor = dict(by_epoch=False)
lr = 1e-05
max_epochs = 8
max_length = 8192
max_norm = 1
model = dict(
    freeze_llm=True,
    freeze_visual_encoder=True,
    llm_lora=dict(
        lora_alpha=256,
        lora_dropout=0.05,
        r=128,
        target_modules=None,
        task_type='CAUSAL_LM',
        type='peft.LoraConfig'),
    model_path='/root/InternLM-813/L2/InternVL/InternVL2-2B',
    quantization_llm=True,
    quantization_vit=False,
    type='xtuner.model.InternVL_V1_5')
optim_type = 'torch.optim.AdamW'
optim_wrapper = dict(
    optimizer=dict(lr=1.0, type='DAdaptAdam'), type='DeepSpeedOptimWrapper')
path = '/root/InternLM-813/L2/InternVL/InternVL2-2B'
prompt_template = 'xtuner.utils.PROMPT_TEMPLATE.internlm2_chat'
randomness = dict(deterministic=False, seed=None)
resume = False
runner_type = 'FlexibleRunner'
save_steps = 1000
save_total_limit = 1
strategy = dict(
    config=dict(
        bf16=dict(enabled=True),
        fp16=dict(enabled=False, initial_scale_power=16),
        gradient_accumulation_steps='auto',
        gradient_clipping='auto',
        train_micro_batch_size_per_gpu='auto',
        zero_allow_untested_optimizer=True,
        zero_force_ds_cpu_optimizer=False,
        zero_optimization=dict(overlap_comm=True, stage=2)),
    exclude_frozen_parameters=True,
    gradient_accumulation_steps=1,
    gradient_clipping=1.0,
    sequence_parallel_size=1,
    train_micro_batch_size_per_gpu=12,
    type='xtuner.engine.DeepSpeedStrategy')
tokenizer = dict(
    pretrained_model_name_or_path='/root/InternLM-813/L2/InternVL/InternVL2-2B',
    trust_remote_code=True,
    type='transformers.AutoTokenizer.from_pretrained')
train_cfg = dict(max_epochs=8, type='xtuner.engine.runner.TrainLoop')
train_dataloader = dict(
    batch_size=12,
    collate_fn=dict(type='xtuner.dataset.collate_fns.default_collate_fn'),
    dataset=dict(
        data_paths='/root/InternLM-813/L2/InternVL/CLoT_cn_2000/ex_cn.json',
        image_folders='/root/InternLM-813/L2/InternVL/CLoT_cn_2000/',
        max_length=8192,
        model_path='/root/InternLM-813/L2/InternVL/InternVL2-2B',
        template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
        type='xtuner.dataset.InternVL_V1_5_Dataset'),
    num_workers=4,
    sampler=dict(
        length_property='modality_length',
        per_device_batch_size=24,
        type='xtuner.dataset.samplers.LengthGroupedSampler'))
visualizer = None
warmup_ratio = 0.03
weight_decay = 0.05
work_dir = './work_dir/diy_config'
