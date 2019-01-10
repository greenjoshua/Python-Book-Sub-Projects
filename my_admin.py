from admin import User, Admin, Privileges

josh = Admin('joshua', 'green', 'nathaniel', 25, 'ols')
josh.privileges.privileges = ['can reset passwords',
    'can moderate discussions',
    'can suspend accounts',]

josh.privileges.show_privileges()
