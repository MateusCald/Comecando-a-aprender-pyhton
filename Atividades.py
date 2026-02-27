#ATIVIDADES PARA FIXCAÇÃO DE IF, ELIF, ELSE

1#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
macas = int(input('Digite a quantidade de maças vendidas: '))
bananas = int(input('Digite a quantidade de bananas vendidas: '))

if macas > bananas:
    print ('Foram vendidas mais macas do que bananas')
elif macas < bananas:
    print ('Foram vendidas mais bananas do que macas')
else:
    print ('Foram vendidas a mesma quantidade das frutas')

2#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
atividade_a = int(input('Informe a quantidade de dia(s) que utilizou para resolver a atividade A: '))
atividade_b = int(input('Informe a quantidade de dia(s) que utilizou para resolver a atividade B: '))
atividade_c = int(input('Informe a quantidade de dia(s) que utilizou para resolver a atividade C: '))

if (atividade_a > 0 and atividade_a > 0 and atividade_c > 0):
    total_de_dias = atividade_a + atividade_b + atividade_c
    print (f'Foi utilizado um total de {total_de_dias} dias para finalizar as três atividades.')
else:
    print ('Erro: Não utilize valores negativos')

3#Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura = int(input('Digite a temperatura atual: '))

if temperatura <= 25:
    print (f'A temperatura é de {temperatura}, está dentro do limite permitido')
else:
    print (f'Alerta! A temperatura é de {temperatura}, esta acima do limite permitido')

4#O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura '))

IMC = peso / altura ** 2

if IMC < 18.5:
    print (f'Seu IMC é {IMC:.2f}, está abaixo do peso')
elif IMC < 25:
    print (f'Seu IMC é {IMC:.2f}, está dentro do peso')
else:
    print (f'Seu IMC é: {IMC:.2f}, está acima do peso')

5#Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
despesa_mensal = float(input('Digite a despesa total do mês: '))

if despesa_mensal > 3000:
    print ('Atenção! Você ultrapassou o limite do orçamento')
else:
    print ('O valor da despesa se encontra dentro do limite estipulado')

6#O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado. 
horario_atual = int(input('Digite o horário atual (formato de 24 horas): '))

if 8 <= horario_atual <= 18:
    print ('Acesso permitido.')
else:
    print ('Acesso negado!')

7#Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
#Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
#Média < 5: Reprovado
primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))
terceira_nota = float(input('Digite sua terceira nota: '))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print (f'Sua média é {media:.1f}, Aprovado')
elif 5 <= media < 7:
    print (f'Sua média é {media:.1f}. Recuperação')
else:
    print (f'Sua média é {media:.1f}, Reprovado')

#8Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
#Até 100 km: R$ 10,00
#Entre 100 km e 200 km: R$ 20,00
#Acima de 200 km: R$ 30,00
distancia = float(input('Digite a distância percorrida: '))

if distancia <= 100:
    print (f'A distância foi de {distancia:.3f} KM, valor do pedágio é: R$ 10,00')
elif 100 < distancia <= 200:
    print (f'A distância foi de {distancia:.3f} KM, valor do pedágio é: R$ 20,00')
else:
    print (f'A distancia foi de {distancia:.3f} KM, o valor do pedágio é: R$ 30,00')

9#Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print (f'O número {numero}, é par')
else:
    print (f'O número {numero}, é impar')

10#Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
#O valor da renda mensal precisa ser maior que R$ 2.000,00.
#O valor da parcela não pode ultrapassar 30% da renda.
#Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.
renda = float(input('Digite o valor da sua renda mensal: '))
parcela = float(input('Digete o valor da parcela desejada: '))

if renda > 2000 and parcela <= 0.3 * renda:
    print ('Empréstimo aprovado')
elif renda <= 2000:
    print ('Empréstimo negado: Renda insuficiente')
else:
    print ('Empréstimo negado: Parcela acima de 30% do valor da renda')

11#Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.
clientes = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

for cliente in clientes:
    print (cliente)

12#Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" 5 vezes
for i in range (5):
    print ('Bem-vindo ao Buscante')

13#Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
valores = [10, 20, 30, 40, 50]

soma = 0 

for valor in valores:
    soma += valor

print (f'A soma total das receitas é: {soma}')

14#Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".
projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

for projeto in projetos:
    if projetos is None:
        print ('Projeto ausente')
    else:
        print (projeto)

15#Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.
livros = ['1984', 'Dom Casmurro', 'O Pequeno Príncipe', 'O Hobbit', 'Orgulho e Preconceito']

for livro in livros:
    if livro == 'O Hobbit':
        print (f'Livro encontrado: {livro}')
        break

16#Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
estoque_livros = 5

while estoque_livros > 0:
    estoque_livros -= 1
    print (f'Venda realizada! Estoque restante: {estoque_livros}')
print ('Estoque esgotado')

17#Crie um programa que utilize um laço for para exibir as seguintes mensagens:
#Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
#Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
#Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".

for segundos in range (10, 0, -1):
    if segundos % 2 == 0:
        print (f'Falta apenas {segundos} segundos - Não perca essa oportunidade!')
    else:
        print (f'A contagem continua: {segundos} segundos restantes.')
print ('Aproveite a promoção agora!')

18#Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato: "Livro disponível: ".
livros = [
    {'nome': '1984', 'estoque': 5},
    {'nome': 'Dom Casmurro', 'estoque': 0},
    {'nome': 'O Pequeno Príncipe', 'estoque': 3},
    {'nome': 'O Hobbit', 'estoque': 0},
    {'nome': 'Orgulho e Preconceito', 'estoque': 2}
]  

for livro in livros:
    if livro ['estoque'] == 0:
        continue
print (f'Livro disponivel: {livro['nome']}')    

19#João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:
#O nome de usuário deve ter pelo menos 5 caracteres.
#A senha deve ter pelo menos 8 caracteres.
#João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

while True:
    usuario = input('Digite o nome de seu usuário: ')
    senha = input('Digite sua senha: ')

    if len (usuario) < 5:
        print ('O nome do usuário deve conter ao menos 5 carateres')
        continue
    if len (senha) < 8:
        print ('A senha deve conter ao menos 8 caracteres')
        continue
    print ('Cadastro realizado com sucesso!')
    break
