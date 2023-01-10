Valor = float (input ('Digite o valor da compra: '))

Cupom = input('Digite o nome do cumpom: ')
 
Desconto = ( Valor * 0.15)

ValorFinal = (Valor - Desconto)

if Valor > 200:
   print (Desconto)    
   print (ValorFinal) 
else:
    print(Valor)
