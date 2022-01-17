length_dict = int(input("Enter the length of Dictionary:"))
class_list = {}
for i in range(length_dict):
    Key = input("Enter Key")
    Value = input("value")

    class_list[Key] = Value


reversed_dictionary = {value : key for (key, value) in class_list.items()}

print(reversed_dictionary)
    







