import psycopg2

login = input("Digite o usuário: ")
password = input("Digite a senha: ")

connection_db = psycopg2.connect(
    host="localhost",
    database="hotel_checkin_checkout",
    user=login,
    password=password
)

action_db = connection_db.cursor()

while True:
    print("1: Cadastrar Cliente")
    option = input("Digite uma opção: ")

    if option == '1':
        pass # register_client()
    if option == '0':
        break

connection_db.close()
