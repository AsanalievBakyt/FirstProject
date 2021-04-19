# criminals = ['johny', 'sparrow', 'harry', 'potter', 'jcvd', 'selena']
# name = input()
#
# if name not in criminals:
#     criminals.append(name)
# print(criminals)

user_info = [[],[]]

while True:
    username = input()
    if username == '1':
        break
    password = input()
    check_password = input()

    if password == check_password:
        user_info[0].append(username)
        user_info[1].append(password)
    print(user_info)