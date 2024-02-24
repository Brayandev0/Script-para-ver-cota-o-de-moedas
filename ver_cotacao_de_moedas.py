# Criador         : Brayan vieira 
# função          : Verifica a cotação de moedas   
# versão          : 1.0
# data da criação : 19/2/2024
#
import requests
#--------------------------------------------------------------------------------------
#                                   Variaveis padrões
barras = 15 * "-"
sucesso = 201,202,200
MENU = " \n Insira qual moeda você quer ver a cotação \n \n Moedas disponiveis : \n \n [D] Dolar   | [ER] Euro \n \n [B] Bitcoin | [ET] ethereum  \n\n [All] todas | [BOL] bolivar venezuelano \n\n \n insira : "
#--------------------------------------------------------------------------------------
#                                 Definindo a moeda escolhida 
tipo_de_moeda = input(MENU).lower()
#--------------------------------------------------------------------------------------
#                               Definindo o menu de escolha 
match tipo_de_moeda:
    case "d":
        moeda_requisitada = "USD-BRL"
    case "er":
        moeda_requisitada = "EUR-BRL"
    case "b":
        moeda_requisitada = "BTC-BRL"
    case "et":
        moeda_requisitada = "ETH-BRL"
    case "bol":
          moeda_requisitada = "VEF-BRL"
    case "all":
        moeda_requisitada = "USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL"
    case _:
          print("\n você inseriu algo invalido \n ")
          exit()
#--------------------------------------------------------------------------------------
#                               Requisição + tratamento de erro 
API = f"https://economia.awesomeapi.com.br/last/{moeda_requisitada}"
try:
    total = requests.get(API)
except ConnectionError:
     print(" \n O servidor de consulta esta com erro, tente novamente mais tarde \n ")
#--------------------------------------------------------------------------------------
#                           Verificando o codigo de status da requisição 
codigo_status = total.status_code
if codigo_status == 200 or codigo_status == 201:
    dados = total.json()
#--------------------------------------------------------------------------------------
#                                          Realizando um for pelos dados recebidos
    for indice , valor_moeda in dados.items():
            print(barras)
            print(f"\n codigo da moeda :{ valor_moeda["code"]}")
            print(f"\n nome da moeda : {valor_moeda["name"]}")
            print(f"\n Alta : 1 {valor_moeda["code"]} vale  {valor_moeda["high"]} R$")
            print(f"\n baixa : 1 {valor_moeda["code"]} vale {valor_moeda["low"]} R$")
            print(f"\n Data e horario da consulta : {valor_moeda["create_date"]} \n")
            print(barras)
#--------------------------------------------------------------------------------------
#                                   Erro de comunicação 
else: 
     print(" \n Houve um erro de comunicação com o servidor, tente novamente mais tarde \n ")
