import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import pdfplumber

def ler_txt(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()

def ler_pdf(caminho):
    texto = ""
    with pdfplumber.open(caminho) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text() or ""
    return texto

def dividir_texto(texto, tamanho_chunk=500):
    chunks = []
    for i in range(0, len(texto), tamanho_chunk):
        chunks.append(texto[i:i + tamanho_chunk])
    return chunks

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def gerar_embedding(texto):
    return modelo.encode(texto)

def buscar_mais_relevante(pergunta, lista_textos, lista_embeddings):
    emb_pergunta = gerar_embedding(pergunta)
    melhor_indice = 0
    menor_distancia = float("inf")
    for i, emb in enumerate(lista_embeddings):
        distancia = cosine(emb_pergunta, emb)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_indice = i
    return lista_textos[melhor_indice], melhor_indice

def gerar_resposta_llm(pergunta, contexto):
    resposta = f"""
    Pergunta: {pergunta}
    Baseado no contexto:
    {contexto}
    Resposta:
    De acordo com as informacoes disponiveis, {contexto.lower()}
    """
    return resposta

def pipeline_rag(caminho_arquivo):
    print("Lendo documento...")
    if caminho_arquivo.endswith(".pdf"):
        texto = ler_pdf(caminho_arquivo)
    else:
        texto = ler_txt(caminho_arquivo)
    print("Documento carregado!")

    chunks = dividir_texto(texto, 500)
    print(f"\nTotal de chunks: {len(chunks)}")
    print("\nPrimeiro chunk:\n", chunks[0])
    print("\nUltimo chunk:\n", chunks[-1])

    print("\nGerando embeddings...")
    embeddings = [gerar_embedding(chunk) for chunk in chunks]
    print("Embeddings prontos!")

    pergunta = input("\nDigite sua pergunta: ")

    contexto, indice = buscar_mais_relevante(pergunta, chunks, embeddings)
    print(f"\n Chunk usado: {indice}")

    resposta = gerar_resposta_llm(pergunta, contexto)
    print("\nResposta final:")
    print(resposta)

if __name__ == "__main__":
    caminho = "C:/Users/Gamer/OneDrive/Desktop/Nova pasta/TPI-2026-1-master/TPI-2026-1-master/A3 - RAGs/regras_empresa.txt"
    pipeline_rag(caminho)