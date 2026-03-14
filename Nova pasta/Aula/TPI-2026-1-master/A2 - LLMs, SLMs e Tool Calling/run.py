import os
import json
from dotenv import load_dotenv
from groq import Groq

from tools import (
    somar,
    multiplicar,
    subtrair,
    dividir,
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    buscar_produto
)

load_dotenv()

client = Groq()

tools = [

    {
        "type": "function",
        "function": {
            "name": "soma",
            "description": "Soma dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "multiplicar",
            "description": "Multiplica dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "subtracao",
            "description": "Subtrai dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "divisao",
            "description": "Divide dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "celsius_para_fahrenheit",
            "description": "Converter Celsius para Fahrenheit",
            "parameters": {
                "type": "object",
                "properties": {
                    "c": {"type": "number"}
                },
                "required": ["c"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "fahrenheit_para_celsius",
            "description": "Converter Fahrenheit para Celsius",
            "parameters": {
                "type": "object",
                "properties": {
                    "f": {"type": "number"}
                },
                "required": ["f"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Busca o preço de um produto",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome_produto": {
                        "type": "string",
                        "description": "Nome do produto"
                    }
                },
                "required": ["nome_produto"]
            }
        }
    }

]


def perguntar(pergunta: str):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Você escolhe qual função usar."},
            {"role": "user", "content": pergunta}
        ],
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message

    if message.tool_calls:

        tool_call = message.tool_calls[0]

        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        #print("Função chamada:", tool_name)
        #print("Argumentos:", args)

        if tool_name == "soma":
            print("Resultado:", somar(args["a"], args["b"]))

        elif tool_name == "multiplicar":
            print("Resultado:", multiplicar(args["a"], args["b"]))

        elif tool_name == "subtracao":
            print("Resultado:", subtrair(args["a"], args["b"]))

        elif tool_name == "divisao":
            print("Resultado:", dividir(args["a"], args["b"]))

        elif tool_name == "celsius_para_fahrenheit":
            resultado = celsius_para_fahrenheit(args["c"])
            print(f"Resultado: {resultado:.2f}°F")

        elif tool_name == "fahrenheit_para_celsius":
            resultado = fahrenheit_para_celsius(args["f"])
            print(f"Resultado: {resultado:.2f}°C")

        elif tool_name == "buscar_produto":
            print(buscar_produto(args["nome_produto"]))


while True:

    pergunta = input("\nDigite sua pergunta (ou 'sair'): ")

    if pergunta.lower() == "sair":
        break

    perguntar(pergunta)