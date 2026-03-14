import sqlite3
produtos = {
    "notebook": 4500,
    "mouse": 80,
    "teclado": 150
}


def somar(a: int, b: int):
    return a + b


def multiplicar(a: int, b: int):
    return a * b


def subtrair(a: int, b: int):
    return a - b


def dividir(a: int, b: int):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def celsius_para_fahrenheit(c: float):
    return (c * 9/5) + 32


def fahrenheit_para_celsius(f: float):
    return (f - 32) * 5/9


def buscar_produto(nome_produto: str):

    nome_produto = nome_produto.lower()

    if nome_produto in produtos:
        return f"O preço do {nome_produto} é R${produtos[nome_produto]}"
    else:
        return "Produto não encontrado"
    
def buscar_produto(nome_produto: str):

    nome_produto = nome_produto.lower()

    if nome_produto in produtos:
        return f"O preço do {nome_produto} é R${produtos[nome_produto]}"
    else:
        return "Produto não encontrado"
    
    import sqlite3



produtos = {
    "notebook": 4500,
    "mouse": 80,
    "teclado": 150
}

estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 8
}

def buscar_produto(nome_produto: str):
    nome_produto = nome_produto.lower()

    if nome_produto in produtos:
        return f"O preço do {nome_produto} é R${produtos[nome_produto]}"
    else:
        return "Produto não encontrado"
    
eventos = []

def criar_evento(titulo: str, data: str):
    eventos.append({
        "titulo": titulo,
        "data": data
    })
    return f"Evento '{titulo}' criado para {data}"


def listar_eventos():
    if not eventos:
        return "Nenhum evento na agenda"

    lista = []
    for evento in eventos:
        lista.append(f"{evento['titulo']} - {evento['data']}")

    return "\n".join(lista)



clima = {
    "sao paulo": "24°C e nublado",
    "bauru": "30°C e ensolarado",
    "curitiba": "18°C e chuvoso"
}

def buscar_clima(cidade: str):
    cidade = cidade.lower()

    if cidade in clima:
        return f"O clima em {cidade} está {clima[cidade]}"
    else:
        return "Cidade não encontrada"



def buscar_produto_db(nome_produto: str):

    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT preco FROM produtos WHERE nome = ?",
        (nome_produto,)
    )

    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        return f"O preço do {nome_produto} é R${resultado[0]}"
    else:
        return "Produto não encontrado no banco"



def buscar_clientes_por_cidade(cidade: str):

    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nome FROM clientes WHERE cidade = ?",
        (cidade,)
    )

    resultados = cursor.fetchall()

    conn.close()

    if resultados:
        nomes = [r[0] for r in resultados]
        return "Clientes: " + ", ".join(nomes)
    else:
        return "Nenhum cliente encontrado"




def buscar_pedidos_cliente(nome: str):

    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT produto, valor FROM pedidos WHERE cliente = ?",
        (nome,)
    )

    resultados = cursor.fetchall()

    conn.close()

    if resultados:
        lista = []
        for produto, valor in resultados:
            lista.append(f"{produto} - R${valor}")

        return "\n".join(lista)

    return "Nenhum pedido encontrado"


def valor_total_cliente(nome: str):

    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT SUM(valor) FROM pedidos WHERE cliente = ?",
        (nome,)
    )

    total = cursor.fetchone()[0]

    conn.close()

    if total:
        return f"Valor total das compras: R${total}"
    else:
        return "Nenhum pedido encontrado"