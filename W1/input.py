def question():
    return input("What is your answer? \n\t")

# 核心逻辑：先把多个空格压缩成一个，再首字母大写
answer = question()

# 步骤1：把连续多个空格替换成单个空格
import re  # 用正则表达式处理更稳妥
clean_answer = re.sub(r'\s+', ' ', answer).strip()  # strip() 去掉首尾多余空格

# 步骤2：首字母大写（Title Case）
final_answer = clean_answer.title()

print(f'hello, {final_answer}!')

def question_2():
    return input("What is your answer? \n\t")

answer = question_2().title().replace(" ", "")
print(f'hello, {answer}!')
