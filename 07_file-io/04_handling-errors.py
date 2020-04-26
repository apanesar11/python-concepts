try:
    with open('04_non-existent.txt', mode='r') as file:
        text = file.readlines()
        print(text)
except (ImportError, FileNotFoundError) as e:
    print(e)