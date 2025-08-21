class List(list):

    def __init__(self):
        self.list = []

    def append(self, list_object):
       print("hier1")
       self.list += list_object
       return self.list


list_class_obj = List()
list = ["bla", 1]
list2 = ["omg", 5]
print(list_class_obj)
list_class_obj.append(list)
print(list_class_obj.append(list))
print(list_class_obj)
print(list_class_obj.list)
list_class_obj.append(list2)
print(list_class_obj.list)
# print(list_class_obj)