import sqlite3

def criar_tabela_alunos(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            linguagens REAL,
            ciencias_humanas REAL,
            ciencias_natureza REAL,
            matematica REAL,
            redacao REAL,
            media REAL,
            status TEXT
        )
    ''')
    conexao.commit()

def salvar_aluno_no_banco(conexao, notas, media, status):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO alunos (linguagens, ciencias_humanas, ciencias_natureza, matematica, redacao, media, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (notas[0], notas[1], notas[2], notas[3], notas[4], media, status))
    conexao.commit()

def calcular_media_enem_e_salvar(notas, conexao):
    """
    Calcula a média final de um aluno no ENEM com base nas notas obtidas em cada área de conhecimento.
    Retorna a média final e uma mensagem indicando se o aluno foi aprovado ou reprovado.
    Salva os dados do aluno no banco de dados SQLite.
    """

    # Verifica se há notas fora do intervalo permitido (0 a 1000)
    for nota in notas:
        if nota < 0 or nota > 1000:
            return 0, "Alguma nota está fora do intervalo permitido (0 a 1000)"

    # Verifica se a nota da redação é maior que zero
    if notas[-1] == 0:
        status = "Reprovado"
    else:
        status = "Aprovado"

    # Calcula a média das notas
    media = sum(notas) / len(notas)

    # Salva os dados do aluno no banco de dados
    salvar_aluno_no_banco(conexao, notas, media, status)

    # Retorna a média final e a mensagem de status
    return media, status

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('alunos.db')

# Criar a tabela de alunos (ou verificar se já existe)
criar_tabela_alunos(conexao)

# Exemplo de uso:
areas_conhecimento = ["Linguagens", "Ciências Humanas", "Ciências da Natureza", "Matemática", "Redação"]
notas = []

for area in areas_conhecimento:
    nota = float(input(f"Digite a nota de {area}: "))
    while nota < 0 or nota > 1000:  # Validação da nota dentro do intervalo permitido
        print("Nota inválida. Digite uma nota entre 0 e 1000.")
        nota = float(input(f"Digite a nota de {area}: "))
    notas.append(nota)

media_final, status = calcular_media_enem_e_salvar(notas, conexao)
print(f"Sua média final no ENEM é: {media_final:.2f}")
print(f"Status: {status}")

# Fechar a conexão com o banco de dados
conexao.close()

