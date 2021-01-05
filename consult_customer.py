def query_by_cpf(action_db):
    cpf = input("Digite o CPF: ")
    sql = "select * from client_basic_data where cpf = %s"
    action_db.execute(sql, (cpf,))
    datas = action_db.fetchall()
    for r in datas:
        print(f'Nome do cliente: {r[2]} {r[3]} CPF: {r[1]}')
    return
