#1. What will be output of following program
dict = {(3,4,8):4,(5,6,7):3}
print('1 output',dict[5,6,7])

#2.  Get keys[“name”, “age”] from dictionary and create new dictionary
# and delete both keys from Dictionary
animaldict = {
  "name": "Dog",
  "age":5,
  "Weight": 4,
  "Country": "US",
  "City":"California"
   
}
new_dict = {key:animaldict[key] for key in ['name','age']}
print('2 output',new_dict)


new_animaldict = {key:animaldict[key] for key in animaldict.keys()-['name','age']}
print(new_animaldict)

#3.
dictlang = {'c#': 6, 'GO': 89, 'Python': 4,'Rust':10}
print(sorted(dictlang))
for _ in sorted(dictlang):
    print ('3 output', dictlang[_])

dictlang['Python3'] = dictlang.pop('Python')
print(dictlang)

if 'GO' in dictlang:
    del dictlang['GO']

print('Dict after deleting GO', dictlang)
print('min value Key', min(dictlang, key = dictlang.get))
print('max value Key', max(dictlang, key = dictlang.get))
