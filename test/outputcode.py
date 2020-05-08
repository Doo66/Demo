# 验证码输出
# 验证码结构:大小写字母+数字

import random

def generate_code(code_len = 4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_charts = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos= len(all_charts) - 1
    code = ''
    for index in range(code_len):
        index = random.randint(0, last_pos)
        code += all_charts[index]
    return code
if __name__  == '__main__':
    print(generate_code(4))
else:
    print("error.")