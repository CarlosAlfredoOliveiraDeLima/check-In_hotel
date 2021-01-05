import psycopg2
import consult_customer
import register_customer


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
    print("1: Consultar Cliente")
    print("2: Cadastrar Cliente")
    option = input("Digite uma opção: ")

    if option == '1':
        consult_customer.query_by_cpf(action_db)
    if option == '2':
        register_customer.customer_personal_data(action_db, connection_db)
    if option == '0':
        break

action_db.close()
connection_db.close()
