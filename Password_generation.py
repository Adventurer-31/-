from random import choice
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
def Password_generation(l):
  A = ascii_lowercase
  B = ascii_uppercase
  C = punctuation
  D = digits
  s1 = 'abcdABCD'
  l1 = [A, B, C, D, A, B, C, D]
  dic1 = dict(zip(s1,  l1))
  s2 = ''
  for i in l[:-1]:
    s2 += dic1[i]
  l2 = list(s2)
  l3 = []
  for i in range(l[-1]):
    l3.append(choice(l2))
  return ''.join(l3)

if __name__ == '__main__':
  op1 = list(input('''请选择构成你需要的密码的元素：（可多选）
  A.小写字母
  B.大写字母
  C.标点符号
  D.数字
  '''))
  n = int(input('请输入一个代表密码长度的整数：'))
  op1.append(n)
  print(Password_generation(op1))
  input('请按任意键退出')