from lmdeploy import pipeline,ChatTemplateConfig
from lmdeploy.vl import load_image
pipe = pipeline('/root/InternLM-813/L2/InternVL/InternVL2-2B',chat_template_config = ChatTemplateConfig(model_name="internvl2-internlm2"))

image = load_image('/root/InternLM-813/L2/InternVL/test.jpg')
response = pipe(('请你根据这张图片，讲一个脑洞大开的梗', image))
print(response.text)