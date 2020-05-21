# -*- coding:utf-8 -*-

import re

def to_string(strings):
    print('原数为',strings)
    tt_lst = strings.split(']')
    new_lst = ''
    for i in tt_lst:
        if not str(i[0]).isdigit():
            i='1'+i
        new_lst+=i
    # print(new_lst)
    tmp=''.join(new_lst)
    word_lst = re.findall(r'[a-zA-Z]+',tmp)
    num_lst = re.findall(r'\d+',tmp)
    fianlLst=''
    for word,num in zip(word_lst,num_lst):
        fianlLst+=word*int(num)
    print('最后的结果',fianlLst)

if __name__ == '__main__':
    s='f2[ab]4[c]d3[ee]g'
    to_string(s)