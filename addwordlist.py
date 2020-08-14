from generate import generate

file = open(f'addwl.txt')
info = file.read()
file.close()
user = ''
name = ''
lname = ''
date = ''
if '-' in info:
    option = info.find('-')
    for i in range(0,option):
        user += info[i]

if '/' in info:
    option2 = info.find('/')
    for i in range(option+1,option2):
        name += info[i]

if '//' in info:
    option3 = info.find('//')
    for i in range(option2+1,option3):
        lname += info[i]

if '///' in info:
    option4 = info.find('///')
    for i in range(option3+2,option4):
        date += info[i]


file = open(f'wordlists/{user}.txt','w')
lista = [name,date]
the_wdl = generate(name,lname,date)
for i in the_wdl:
    file.write(f'{i}\n')
