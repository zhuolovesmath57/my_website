file_name = "/Users/zhangzhuo/Downloads/untitled.md"

with open(file_name, "r") as f:
    s = f.read()
    s.replace("\\", "\\newline")
    print(s)
    
