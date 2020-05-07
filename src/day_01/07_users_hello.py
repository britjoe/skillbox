"""
Пример программы для работы с циклами

Данные
- список клиентов чата ['John', 'David', 'Kate', 'Alex']

Сделать
- написать цикл для приветствия каждого клиента
- сообщение имеет вид "Hello, ИМЯ"
"""
names = ['John', 'David', 'Kate', 'Alex']
for i in names:
    print(f"Hello, {i}")
clients = ['John', 'David', 'Kate', 'Alex']

for user in clients:
    print(f"Привет, {user}")

clients.append("Artur")
