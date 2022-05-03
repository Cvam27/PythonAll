dictionary = {'george': '16', 'amber': '19'}
search_age = input("Provide age")

for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if age == search_age:
        # keys = dictionary.keys()
        print(name)
