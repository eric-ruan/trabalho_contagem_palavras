# O arquivo txt é uma história gerada por uma IA:
```
Era uma vez um pássaro colorido que voava pelos céus de uma cidade ensolarada. Ele cantava alegremente enquanto voava, espalhando suas penas multicoloridas pelo ar. As pessoas olhavam maravilhadas para o pássaro e se perguntavam qual seria a sua espécie.

O pássaro sobrevoou prédios altos, parques verdes e rios sinuosos, sem nunca perder o ritmo de sua canção. Ele parecia livre como o vento, sem nenhum cuidado ou preocupação.

Mas, de repente, uma tempestade se aproximou. As nuvens escuras cobriram o céu e começaram a despejar uma chuva forte. O pássaro, que antes voava com tanta graça, agora lutava para se manter no ar. As suas penas se encharcaram e a sua canção se transformou em um triste piado.

Mas o pássaro não desistiu. Ele batalhou bravamente contra o vento e a chuva, até que finalmente, a tempestade passou. O sol voltou a brilhar, e o pássaro, exausto, pousou em um galho de árvore.

As pessoas que antes o observavam, agora se aproximaram para ver se ele estava bem. Eles ficaram impressionados com a beleza de suas penas, mesmo molhadas, e agradeceram por terem presenciado um espetáculo tão bonito.

O pássaro, com um último piado, voou novamente para o céu, deixando as pessoas maravilhadas com a sua coragem e determinação. E assim, a cidade ensolarada continuou a viver a sua vida, sabendo que, mesmo nos momentos difíceis, a beleza e a esperança sempre podem surgir.
```

## Explicação do código


### Primeiramente decidi dividir o código em funções para que ficasse visualmente mais bonito e fácil de entender.


## Começando o código:
- A primeira parte do código é ler o arquivo txt, para isso utilizei a função "carregar_arquivo". Ela utiliza o "with open(), foi passado também a opção 'r' de read e encoding='utf-8', para que assim o arquivo seja interpretado da forma correta. No final é retornado a leitura do texto.
```python
def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as texto:
        return texto.read()
```

- A próxima função é a de reescrever o texto removendo todos os caracteres, ou seja, deixando ele formatado, primeiro eu usei a função 'unidecode', que remove acentos, depois deixei o texto todo em maiusculo e removi os espaços de cada palavra. Após isso criei uma lista vazia e formatei cada palavra do texto removendo virgulas, pontos e outras coisas que pudessem interferir no resultado final.
```python
def reescrever_texto(texto):
    texto = unidecode(texto)
    texto = texto.upper().split()
    palavras = []
    for i in texto:
        i = i.translate(str.maketrans('', '', string.punctuation))
        palavras.append(i)
    return palavras
```

- A função de contagem de palavras é feita da seguinte maneira: crio um dicionário vazio, após isso crio um for para percorrer todo o texto, a lógica seguida é a seguinte, se a palavra da vez estiver dentro do dicionário, é adicionado 1 na frente dela, se não, adiciona a palavra e o 1. Após isso utilizo a função sorted com função lambda e reverse=True para ordenar do maior para o menor.
```python
def contar_palavras(palavras):
    contador = {}
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return sorted(contador.items(), key=lambda x: x[1], reverse=True)
```

- A consulta de palavra é feita através de um for com duas variáveis 'palavra' e 'ocorrencias', percorrendo todo o texto com a contagem das palavras. A lógica é a seguinte, se a palavra escolhida for igual a alguma palavra que está sendo passada no for, ela é exibida junto com a sua ocorrencia. Se não é pedido para escolher outra palavra.
```python
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
```

- A próxima função é a de exibir as palavras mais e menos frequentes, criei uma variável chamada palavra que recebe o primeiro indice de um for percorrendo as palavras ordenadas com seus indices. Após isso os prints exibem as mesmas.
```python
def exibir_palavras_frequentes(palavras_ordenadas):
    palavras = [p[0] for p in palavras_ordenadas]
    print(f"A palavra mais frequente é: {palavras[0]}, com {palavras_ordenadas[0][1]} ocorrências")
    print(f"A palavra menos frequente é: {palavras[-1]}, com {palavras_ordenadas[-1][1]} ocorrências")
```

- Para ficar visualmente melhor eu criei uma função printando as opções que podem ser escolhidas.
```python
def opcoes():
    print('Retirar os acentos[1]...')
    print('Contar as palavras[2]...')
    print('Escolher qual(is) palavra(s) deseja ver e quantas vezes aparece[3]...')
    print('Exibir as palavras com mais aparição e com menos aparição[4]...')
    print('Sair[0]...')
```

- Por ultimo eu chamei as funções em cada opção que o usuário fosse escolher.
```python
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
```

# Segue abaixo o código completo:
```python
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
```