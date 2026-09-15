import tiktoken

text = "Who is Pm of India ?"
tokenizer = tiktoken.encoding_for_model(model_name="gpt-4")

tokenIds = tokenizer.encode(text)

print(tokenIds)
//[15546, 374, 393, 76, 315, 6890, 949]

resultIds = [8971, 315, 6890, 374, 66904, 3696, 77, 64594, 1491, 72]

result = tokenizer.decode(res)