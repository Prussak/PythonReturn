idade = int (
    input (
        "Digite a Idade da pessoa: ")
           )

if idade >= 18:
    print ("Maior de idade")
else:
    print("menor de idade")
    
 #
notaA = float(input('Digite sua primeira nota: '))

notaB = float(input('Digite sua segunda nota: '))

# Calcular media
mediafinal = (notaA + notaB) / 2

# verificação

if mediafinal >= 7.0:
    print('A Média %.1f - Aprovado' % mediafinal)

else:
    print('A Média: %.1f - Reprovado' % mediafinal)
    
#####################################################    
#Sequencias de Escapes
# \n	Insere uma quebra de linha.
# \t	Insere tabulação horizontal.
# \v	Insere tabulação vertical.
# \r	Equivalente ao efeito da tecla Enter.
# \’	Aspas simples.
# \”	Aspas duplas.
# \\	Insere uma barra invertida (backslash).
# \a	Chamado de ASC bell ou beep do sistema. Se houver suporte, aciona um bipe.
# \b	Aciona o backspace, ou seja, apaga o caractere anterior.
# \f	Insere uma quebra de página.
# \u	Insere um caractere UNICODE. Deve acompanhar um código com 4 números.
###################################################
#Máscaras
# %d ou %i	Int (inteiro)	Exibe um valor inteiro.
# %f	Float ou double	Exibe um valor decimal.
# %ld	Long Int	Exibe um número inteiro longo.
# %e ou %E	Float e double	Exibe um número exponencial (número científico).
# %c	Char (caractere)	Exibe um caractere.
# %o	Int	Exibe um número inteiro em formato octal.
# %x ou %X	Int	Exibe um número inteiro no formato hexadecimal.
# %s	Char	Exibe uma cadeia de caracteres (string).
# %r	Boolean	Exibe true ou false (verdadeiro ou falso).
###################################################
Valor = float (input ('Digite o valor da compra: '))

Cupom = input('Digite o nome do cumpom: ')
 
Desconto = ( Valor * 0.15)

ValorFinal = (Valor - Desconto)

if Valor > 200:
   print (Desconto)    
   print (ValorFinal) 
else:
    print(Valor)
    
######################################################
#EstruturaSimples.py
A = imput ("Informe um valor para a váriavel A")
B = input ("Informe um valor para a váviavel B")

if (A>B):
    aux = A;
    A=B;
    B=aux;
    
print("O valor da variável A agora é : ", A);
print("O valor da variável B agora é : ", B);
    
##########################################################
#elif
idade = int (
    input (
        "Digite a Idade da pessoa: ")
           )

if idade >= 18:
    print ("Maior de idade")
    
elif idade >16:
    print("Infanto juvenil")
    
else:
    print("menor de idade") 
    
#############################################################
#Estrutura de repetição
for n in range(10):
    print(n)
    
#do 1 ao 10:
for n in range(1, 11):
    print(n)  

#decrescente
for n in range(10, 0, -1):
    print(n)
    
#while
x = 1
while x<=15:
    print(x);
    x=x+1    
#Media de Valores
qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
        soma = soma + valor
        qtd = qtd + 1
        #Enquanto o valor for positivo ele pede para digitar
        valor = float(input("Digite um valor: "))

#Caso digite um valor negativo, o laço encerra        
media = soma / qtd
print("\n Total da Soma: ", soma)
print("\n quantidade de valores digitados: ", qtd)
print("\n Media dos valores: ", media)    

#Fuções

def lernotas():
    n = float(input('Digite uma nota: '))
    return n


def resultado(n1, n2):
    media = (n1+n2) / 2
    print("nota 1: ", n1)
    print("nota 2: ", n2)
    print("media: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
resultado(a,b)


#Outras funções
#Gravar.py
arquivo =  open('arqText.txt', 'W')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#leitura do arquivo de texto

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()

#r	Abre o arquivo somente para leitura.O arquivo deve já existir.
#r+	Abre o arquivo para leitura e escrita. O arquivo deve já existir. A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.
#w	Abre o arquivo somente para escrita, no início do arquivo.Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.
#w+	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.a	Abre o arquivo para escrita no final do arquivo.Não apaga o conteúdo preexistente.
#a+	Abre o arquivo para escrita no final do arquivo e leitura.

     
        