from users import User

from admin import Admin, Privileges

james = Admin('james', 'moore', 'kit', 24, 'chemical engineering')

james.privileges.privileges = ['can delete post', 'can delete user', 'can edit profiles']

james.privileges.show_privileges()