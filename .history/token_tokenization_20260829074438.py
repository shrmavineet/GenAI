import tiktoken

text = "Who is Pm of India ?"
tokenizer = tiktoken.encoding_for_model(model_name="gpt-4")

tokenIds = tokenizer.encode(text)

print(tokenIds)
//[20600, 382, 398, 76, 328, 8405, 1423]