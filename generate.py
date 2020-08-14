def generate(user,lname,date):
    day = date[0]+date[1]
    month = date[2]+date[3]
    year = date[4]+date[5]+date[6]+date[7]
    
    l1 = user+day
    l2 = user+month
    l3 = user+year
    l4 = user+day+month
    l5 = user+date
    l6 = user+lname+day
    l7 = user+lname+month
    l8 = user+lname+year
    l9 = user+lname+day+month
    l10 = user+lname+date
    l11 = date

    the_wdl = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]

    return the_wdl
