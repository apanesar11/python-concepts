with open('./01_sample-text.txt') as file:
    text =  file.readlines()
    print(text)

with open('./01_sample-text.txt', mode='a') as file:
    text = file.write("Hello, it's me!")
    print(text)

with open('./02_sample-text.txt', mode='a') as file:
    text = file.write("This is a new file generated during runtime!")
    print(text)

with open('./03_sample-text.txt', mode='w') as file:
    text = file.write("This is another file generated during runtime!")
    print(text)