mylist = []
mylist.append(1)
mylist.append("21-SE-043")
mylist.insert(1,"Ali")
# print(mylist)
# print(mylist[2])
# print(mylist[:2])
# print(mylist[-2:-1])
# mynumberslist = [5,3,21,111,23,45]
# print(mynumberslist.sort(reverse=False))
# fruits = ["Apple","Banana","Orange","Mangoe","Guava"]
# print("Printing fruits list in descending order")
# fruits.sort(reverse=True)
# print(fruits)
# print("Printing fruits list in reverse order")
# fruits.reverse()
# print(fruits)
# print("Counting Apple in the list")
# print(fruits.count("Apple"))
# print("Extending the fruit list with mylist")
# fruits.extend(mylist)
# print(fruits)
# print("Removing Apple from the list")
# fruits.remove("Apple")
# print(fruits)
# string = ("My","Name","Is","Ali")
# print(string)
# print(type(string))
# int = (1,2,3)
# print(int)
# print(type(int))
# int_tuple = (1,2,3,4,5)
# print(int_tuple)
# string_tuple = ('syed','ali','akbar','shah','gelani')
# print(string_tuple)
# float_tuple = (3.14, 1.618, 9.81, 2.718, 0.007)
# print(float_tuple)

int_tuple = (1,2,3,4,5)
string_tuple = ('syed','ali','akbar','shah','gelani')
concatenated_tuple = int_tuple + string_tuple
print("'syed' in concatenated tuple is appeard ",concatenated_tuple.count("syed"),"time")
print("Displaying the index of 'akbar' in the concatenated tuple:",concatenated_tuple.index("akbar"))
# print("Creating dictionary with integer keys and string values")
names_dict = {1:"Syed",2:"Ali",3:"Akbar",4:"Shah",5:"Gelani"}
# print(names_dict)
# print("Creating dictionary with float keys and string values")
gpa_dict = {3.6:"Asad Shah",2.99:"Aon Hashmi",2.4:"Basit Naeem"}
# print(gpa_dict)
# print("Creating dictionary with string keys and string values")
car_dict = {'Name':'Mercedz-Benz','Model':'X-600','Status':'Taxed'}
# print(car_dict)
# gpa_dict = {3.6:"Asad Shah",2.99:"Aon Hashmi",2.4:"Basit Naeem"}
# print("Sorting the dict keys")
# print(sorted(gpa_dict.items()))
# print("Sorting the dict values")
# print(sorted(gpa_dict.items(),key=lambda item: item[1]))
# gpa = {2.14,3.25,3.75,3.5,3.75}
# reg = {1,2,3,4,5}
# print(names)
# print("Observing! Set removes duplicate gpa")
# print(gpa)
# print(reg)

# names = {"Syed","Ali","Akbar","Shah"}
# print("Adding element in the set 'names'")
# names.add("Gelani")
# print(names)
# names.remove("Shah")
# print("Removing element in the set 'names'")
# print(names)
# print("Discarding element in the set 'names'")
# names.discard("syed")
# print(names)