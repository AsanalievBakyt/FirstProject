data = [
    {'text':'oh hi duuuude how r uy??check this 1xbet'},
    {'text':'Dear Harry Potter, i am Frodo Baggins i represent 1xbet company.Best bet service'},
    {'text':'wooooh yoow harry look at my jackpot 100000000$ at 1xbet service'},
    {'text':'Harry , today i saw the man who looks like Hawkeye from Avengers on 100% and he dont use 1xbet service'},
]
final_mail = 'Hello Harry, my name is Maksim, Im still waiting for the letter from Hogwarts'


spam_word = ''
q_spam = 0
database = []

for mail in data:
    str = mail['text'].lower().split()
    database.extend(str)
print(database)
for word in database:
    quantity = database.count(word)
    if quantity > q_spam:
        q_spam = quantity
        spam_word = word

if spam_word in final_mail.lower():
    print('mail is not ok')
else:
    print('mail is ok')
