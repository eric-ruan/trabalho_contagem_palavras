#Crie um programa em Python que receba um texto (proveniente de um arquivo TXT) e realize as seguintes atividades:
from unidecode import unidecode
import string

# Carregue o arquivo
def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as texto:
        return texto.read()

# Retire os acentos e exiba o texto reescrito. opção[1]
def reescrever_texto(texto):
    texto = unidecode(texto)
    texto = texto.upper().split()
    palavras = []
    for i in texto:
        i = i.translate(str.maketrans('', '', string.punctuation))
        palavras.append(i)
    return palavras

# Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente). opção[2]
def contar_palavras(palavras):
    contador = {}
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return sorted(contador.items(), key=lambda x: x[1], reverse=True)

# Permita ao usuário saber qual(is) palavra(s) que ele deseja e quantas aparições de cada uma. opção[3]
def consultar_palavra(palavras_ordenadas):
    while True:
        print("Digite uma palavra para consultar se tem no texto e quantas vezes aparece...")
        print("Ou digite SAIR para terminar...")
        palavra_escolhida = input(str()).upper().strip()
        if palavra_escolhida == 'SAIR':
            break
        palavra_encontrada = False
        for palavra, ocorrencias in palavras_ordenadas:
            if palavra_escolhida == palavra:
                print(f"A palavra escolhida foi: {palavra} e ela aparece {ocorrencias} vezes")
                palavra_encontrada = True
                break
        if not palavra_encontrada:
            print('Palavra não encontrada no texto, tente novamente...')

# Exibir a com mais aparição e a com menos aparição. opção[4]
def exibir_palavras_frequentes(palavras_ordenadas):
    palavras = [p[0] for p in palavras_ordenadas]
    print(f"A palavra mais frequente é: {palavras[0]}, com {palavras_ordenadas[0][1]} ocorrências")
    print(f"A palavra menos frequente é: {palavras[-1]}, com {palavras_ordenadas[-1][1]} ocorrências")

# OPÇÕES
def opcoes():
    print('Retirar os acentos[1]...')
    print('Contar as palavras[2]...')
    print('Escolher qual(is) palavra(s) deseja ver e quantas vezes aparece[3]...')
    print('Exibir as palavras com mais aparição e com menos aparição[4]...')
    print('Sair[0]...')

texto = carregar_arquivo('historia.txt')
opcoes()

while True:
    palavras = reescrever_texto(texto)
    palavras_ordenadas = contar_palavras(palavras)
    
    opcao = input(str('Digite a opção escolhida: '))
    if opcao == '1':
        print(palavras)
    elif opcao == '2':
        print(palavras_ordenadas)
    elif opcao == '3':
        consultar_palavra(palavras_ordenadas)
    elif opcao == '4':
        exibir_palavras_frequentes(palavras_ordenadas)
    elif opcao == '0':
        print('Obrigado por utilizar o sistema...')
        break
    else:
        print('Escolha uma opção correta...')
