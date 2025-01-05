from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

# Define your query
query = """ Summarize the following text in 50 words or less: Artificial Intelligence (AI) 
has revolutionized numerous industries, from healthcare to finance, by enabling advanced data 
analysis and decision-making capabilities. However, ethical concerns, such as bias in 
algorithms and potential misuse, remain significant challenges. Future developments in 
AI aim to address these concerns while expanding AI’s role in enhancing human productivity 
and creativity. """

# Tokenize the query
inputs = tokenizer.encode(query, return_tensors="pt")

# Generate the response
outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Response:", response)
