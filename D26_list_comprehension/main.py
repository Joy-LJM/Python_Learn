# python sequence: list, range, string, tuple
# new_list=[new_item for item in list]
# conditional list comprehension
# new_list=[new_item for item in list if test]
numbers=[1,2,3]
new_nums=[n+1 for n in numbers]
print(new_nums)

name ="Joy"
letters_list=[letter for letter in name]
print(letters_list)

range_list=[num*2 for num in range(1,5)]
print(range_list)

names=['Alex',"Beth","Caroline","Alexander"]
short_names=[name for name in names if len(name)<5]
print(short_names)
long_names=[name.upper() for name in names if len(name)>5]
print(long_names)
