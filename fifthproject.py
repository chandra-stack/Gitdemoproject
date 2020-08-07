try:
    file=open('chandru.txt')
    print(file.readlines())
except FileNotFoundError:
    print("file not found and try giving some other file")

