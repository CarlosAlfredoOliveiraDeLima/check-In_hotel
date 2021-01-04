import psycopg2


def register_client():
    cpf = input('Digite o CPF: ')
    first_name = input('Digite o nome: ')
    name = input('Digite o sobrenome: ')
    action_db.execute("insert into client_basic_data (cpf, client_first_name, client_name) values (%s, %s, %s)",
                      (cpf, first_name, name))
    connection_db.commit()


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
        register_client()
    if option == '0':
        break

connection_db.close()
