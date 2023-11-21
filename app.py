import sqlite3 as lite

#Criando conexão
con = lite.connect('dados.db')

#Criando a tabela se não existir
with con:
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarefa TEXT
        )
    ''')

#Função para exibir a lista de tarefas
def exibir_tarefas():
    with con:
        cur = con.cursor()
        cur.execute('SELECT tarefa FROM tarefas')
        tarefas = cur.fetchall()
    if not tarefas:
        print("Nenhuma tarefa.")
    else:
        for i, (tarefa,) in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

#Função para adicionar uma tarefa à lista
def adicionar_tarefa(nova_tarefa):
    with con:
        cur = con.cursor()
        cur.execute('INSERT INTO tarefas (tarefa) VALUES (?)', (nova_tarefa,))
    print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")

# Função para remover uma tarefa da lista
def remover_tarefa(numero_tarefa):
    with con:
        cur = con.cursor()
        cur.execute('SELECT tarefa FROM tarefas')
        tarefas = cur.fetchall()

        if not tarefas:
            print("Nenhuma tarefa para remover.")
        elif 1 <= numero_tarefa <= len(tarefas):
            tarefa_removida = tarefas[numero_tarefa - 1][0]
            cur.execute('DELETE FROM tarefas WHERE id = (SELECT id FROM tarefas LIMIT 1 OFFSET ?)', (numero_tarefa - 1,))
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")


#Menu de opções
while True:
    print("\nEscolha uma opção:")
    print("1. Exibir Tarefas")
    print("2. Adicionar Tarefa")
    print("3. Remover Tarefa")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        exibir_tarefas()
    elif escolha == "2":
        nova_tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefa(nova_tarefa)
    elif escolha == "3":
        numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
        remover_tarefa(numero_tarefa)
    elif escolha == "4":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
