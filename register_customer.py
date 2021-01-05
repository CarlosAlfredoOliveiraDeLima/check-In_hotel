def customer_personal_data(action_db, connection_db):
    cpf = input('Digite o CPF: ')
    first_name = input('Digite o nome: ')
    name = input('Digite o sobrenome: ')
    sql = "insert into client_basic_data (cpf, client_first_name, client_name) values (%s, %s, %s)"
    action_db.execute(sql, (cpf, first_name, name))
    connection_db.commit()
    return
