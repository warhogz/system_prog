#Из исходного текстового файла (Dostoevsky.txt) была поставлена цель выбрать блок информации за 1857
#год и поместить его в новый текстовый файл.

import re
data = re.compile(r'1857')
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    sss = file.read()
    bbb = re.findall(data, sss)
print(bbb)
with open('new_file.txt', 'w', encoding='utf-8') as f_in:
    f_in.write(str(bbb[0]))

enter = re.compile(r'\n')

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    lst = re.split(enter, text)
    print(lst)
fst = lst.index('1857 год')
scd = lst.index('1860–1866 гг.')
with open('new_file.txt', 'a', encoding='utf-8') as f_in:
        print(lst)
        for i in lst:
            if i == '1857 год':
                for j in lst[fst+1:scd]:
                    if j!='1860–1866 гг.':
                            f_in.write(f'\n{j}')