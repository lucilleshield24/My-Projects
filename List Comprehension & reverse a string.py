me = {
            'firstname' : 'matthew',
            'lastname' : 'shield',
            'age' : 15
            }
bestsister = {
            'firstname' : 'luci',
            'lastname' : 'shield',
            'age' : 12
            }
oksister = {
            'firstname' : 'helena',
            'lastname' : 'shield',
            'age' : 21
            }
father = {
            'firstname' : 'alan',
            'lastname' : 'shield',
            'age' : 79
            }
mother = {
            'firstname' : 'hong',
            'lastname' : 'tang',
            'age' : 98}
d = [me, bestsister, oksister, father, mother]
# write list comprehension, given d, producing list of everyone's ages
ages = [x['age'] for x in d]
# reverse a string --> create new string, append -x to it
def reverse(my_string):
    new_string = ""
    for x in my_string:
        new_string = x + new_string
    return new_string

#write list comp, given d, produce first names but backwards
names_first = [reverse(x['firstname']) for x in d]
print(names_first)

