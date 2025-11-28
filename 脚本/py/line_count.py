# 如果是小文件，可以用 f.readlines()；
# 如果是大日志文件，我更倾向于用 for line in f: 循环来计数，这样更省内存。


with open('word.txt', 'r') as f:
    line_count = len(f.readlines())
print(line_count)



line_count = 0
with open("word.txt",'r') as f:
    for line in f:
        line_count += 1
print(line_count)
# 迭代文件对象：一次只读一行到内存。
