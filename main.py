def count_chars():
    s = input("请输入一行字符：")
    letters = digits = spaces = others = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1
            
    print(f"英文字符：{letters} 个")
    print(f"数字：{digits} 个")
    print(f"空格：{spaces} 个")
    print(f"其他字符：{others} 个")

if __name__ == "__main__":
    count_chars()
