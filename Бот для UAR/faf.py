import amino

print('Введите email')
email = input("Ваша почта:")
print("Ведите пароль")
password = input("Пароль:")


client=amino.Client()
client.login(email=email, password=password)

for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
    print(name, id)