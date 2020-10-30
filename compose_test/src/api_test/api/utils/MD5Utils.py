# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

import hashlib


def encryption(s: str):
    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    m = hashlib.md5()
    b = s.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()

    print('MD5加密前为 ：' + s)
    print('MD5加密后为 ：' + str_md5)

    # # 另一种写法：b‘’前缀代表的就是bytes
    # str_md5 = hashlib.md5(str).hexdigest()
    # print('MD5加密后为 ：' + str_md5)


if __name__ == '__main__':
    encryption("this is a md5 test.")
