def caesar(text, shift, encryption=True):
    # isinstance() 1st parameter: value to check, 2nd parameter: type to check against
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encryption:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

# 按照题目要求：定义带text和shift参数的函数
def encrypt(text, shift):
    # 加密，第三个参数默认True，也可以显式写上
    return caesar(text, shift)

def decrypt(text, shift):
    # 解密，第三个参数传False
    return caesar(text, shift, False)

# 测试调用
result_encrypt = encrypt('freeCodeCamp', 3)
result_decrypt = decrypt(result_encrypt, 3)

print("加密结果：", result_encrypt)
print("解密结果：", result_decrypt)