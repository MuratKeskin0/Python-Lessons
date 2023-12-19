number = int(input('number: '))
isPrime=True
if number==1:
    print('1 is not Prime number')


for i in range(2,number):
    if(number%i==0):
        isPrime=False
        break

if isPrime:
    print('Prime number')
else:
    print('is not Prime number')
