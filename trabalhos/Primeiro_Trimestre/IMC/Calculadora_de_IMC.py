import sqlite3

def calcular_imc(nome, peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.
    Retorna o IMC, status de peso e mensagem indicando o status de peso da pessoa.
    """

    if peso <= 0 or altura <= 0:
        return "Por favor, insira um valor válido para peso e altura.", None

    imc = peso / (altura ** 2)

    if imc < 18.5:
        status = "Abaixo do peso"
    elif imc < 25:
        status = "Peso normal"
    elif imc < 30:
        status = "Sobrepeso"
    elif imc < 35:
        status = "Obesidade grau I"
        perda_peso = peso * 0.20
    elif imc < 40:
        status = "Obesidade grau II"
        perda_peso = peso * 0.30
    else:
        status = "Obesidade grau III"
        perda_peso = peso * 0.40

    if imc >= 35:
        mensagem = f"Você está com {status}. Para voltar ao peso ideal, você precisa perder {perda_peso:.2f} quilos."
    else:
        mensagem = f"Seu IMC é {imc:.2f}. Você está {status}."

    return mensagem, imc

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('dados_usuarios.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, peso REAL, altura REAL, imc REAL)''')

while True:
    try:
        nome = input("Digite seu nome: ")
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))

        resultado, imc = calcular_imc(nome, peso, altura)
        if imc is not None:
            print(resultado)

            # Inserir os dados do usuário no banco de dados
            cursor.execute("INSERT INTO usuarios (nome, peso, altura, imc) VALUES (?, ?, ?, ?)", (nome, peso, altura, imc))
            conn.commit()

            break
        else:
            print(resultado)
    except ValueError:
        print("Por favor, insira um valor numérico para peso e altura.")

# Fechar a conexão com o banco de dados
conn.close()
