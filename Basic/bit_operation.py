pwd = input('请输入密码： ')
print('原密码： ',pwd)
key = input('请输入密钥：')
password = int(pwd) ^ int(key)
print('原密码加密后：',password)
print('原密码解密后：',password ^ int(key))
number = 32
print('左移一位',number<<1)
print('右移一位',number>>1)
