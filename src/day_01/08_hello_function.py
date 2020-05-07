"""
Пример программы для работы с функциями

Сделать
- функцию hello, которая выводит текст приветствия клиенту
"""


class ChatMembers(list):
    pass

    def append(self, name):
        list.append(self, name)
        print(f"Hello, {name}!")

    def pop(self, __index: int = ...):
        print(f"Goodbye, {list.pop(self, __index)}!")

    def remove(self, name):
        list.remove(self, name)
        print(f"Goodbye, {name}!")


names = ChatMembers()
b = ['John', 'David', 'Kate', 'Alex']
for i in b:
    names.append(i)

names.pop(-1)

names.remove("David")
b.remove("David")



def user_hello(user):
    print(f"Привет, {user}")


clients = ['John', 'David', 'Kate', 'Alex']

for user in clients:
    user_hello(user)

new_user = "Artur"

clients.append(new_user)
user_hello(new_user)
