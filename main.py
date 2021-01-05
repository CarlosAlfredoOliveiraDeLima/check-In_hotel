import psycopg2


def register_client():
    cpf = input('Digite o CPF: ')
    first_name = input('Digite o nome: ')
    name = input('Digite o sobrenome: ')
    sql = "insert into client_basic_data (cpf, client_first_name, client_name) values (%s, %s, %s)"
    action_db.execute(sql, (cpf, first_name, name))
    connection_db.commit()


def consult_client():
    cpf = input("Digite o CPF: ")
    # cpf = input('Digite o CPF: ')
    # action_db.execute("select client_first_name, client_name from client_basic_data where cpf = %s", cpf)
    # datas = action_db.fetchall()
    # print(f'Nome do cliente: {datas[0]} {datas[1]}')
    sql = "select * from client_basic_data where cpf = %s"
    action_db.execute(sql, (cpf,))
    datas = action_db.fetchall()
    for r in datas:
        print(f'Nome do cliente: {r[2]} {r[3]} CPF: {r[1]}')


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
    print("2: Consultar Cliente")
    option = input("Digite uma opção: ")

    if option == '1':
        register_client()
    if option == '2':
        consult_client()
    if option == '0':
        break

action_db.close()
connection_db.close()
