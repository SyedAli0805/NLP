from transformers import TextGenerationPipeline, AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("imone/pangu_2_6B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("imone/pangu_2_6B", trust_remote_code=True)

text_generator = TextGenerationPipeline(model, tokenizer)
# greedy search
print(text_generator("中国和美国和日本和法国和加拿大和澳大利亚的首都分别是哪里？", max_length=50))

[{'generated_text': '中国和美国和日本和法国和加拿大和澳大利亚的首都分别是哪里？\n中国北京,美国华盛顿,日本东京,法国巴黎,加拿大多伦多,澳大利亚悉尼,新西兰奥克兰,澳大利亚墨尔本,新西兰奥克兰,'}]
