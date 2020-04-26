file = open('./01_sample-text.txt')

print(file.read())
file.seek(0)
print('**********')
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
print('**********')
print(file.readlines())

file.close()