import math
from Simples.op import soma, multiplicacao, divisao, subtracao
from Avancado.eq import bashkara, rq, rc, ptc, callog

print('''
                                                                                                                                                                                                                             
  ,----..               ,--,                             ,--,                  ___                              
 /   /   \            ,--.'|                           ,--.'|                ,--.'|_                            
|   :     :           |  | :                      ,--, |  | :                |  | :,'   ,---.    __  ,-.        
.   |  ;. /           :  : '                    ,'_ /| :  : '                :  : ' :  '   ,'\ ,' ,'/ /|        
.   ; /--`   ,--.--.  |  ' |      ,---.    .--. |  | : |  ' |     ,--.--.  .;__,'  /  /   /   |'  | |' |        
;   | ;     /       \ '  | |     /     \ ,'_ /| :  . | '  | |    /       \ |  |   |  .   ; ,. :|  |   ,'        
|   : |    .--.  .-. ||  | :    /    / ' |  ' | |  . . |  | :   .--.  .-. |:__,'| :  '   | |: :'  :  /          
.   | '___  \__\/: . .'  : |__ .    ' /  |  | ' |  | | '  : |__  \__\/: . .  '  : |__'   | .; :|  | '           
'   ; : .'| ," .--.; ||  | '.'|'   ; :__ :  | : ;  ; | |  | '.'| ," .--.; |  |  | '.'|   :    |;  : |           
'   | '/  :/  /  ,.  |;  :    ;'   | '.'|'  :  `--'   \;  :    ;/  /  ,.  |  ;  :    ;\   \  / |  , ;           
|   :    /;  :   .'   \  ,   / |   :    ::  ,      .-./|  ,   /;  :   .'   \ |  ,   /  `----'   ---'            
 \   \ .' |  ,     .-./---`-'   \   \  /  `--`----'     ---`-' |  ,     .-./  ---`-'                            
  `---`    `--`---'              `----'                         `--`---'                                        
                                                                                                                
''')

while True:
    print('\n♥ 1 - Sum\n♥ 2 - Subtract\n♥ 3 - Multiply\n♥ 4 - Divide\n♥ 5 - Root\n♥ 6 - Power\n♥ 7 - Bashkara \n♥ 8 - Logarithm\n♥ 0 - Quit')

    op = input('\nChoose an option: ')
    if op == '0':
     print('\nSee u next time!! :( ')
     break

    if op in ['1', '2', '3', '4']:
        a = float(input('First value: '))
        b = float(input('Second value: '))

        if op == '1':
            print('\nA The result is: ', soma(a, b))
        elif op == '2':
            print('\nA The result is: ', subtracao(a, b))
        elif op == '3':
            print('\nA The result is: ', multiplicacao(a, b))
        elif op == '4':
            print('\nA The result is: ', divisao(a, b))

    elif op =='5':
        raiz = input ('\nSquare or cubic root? ')
        if raiz == 'square':
            r1 = input('\nType a value: ')
            print('\nThe square root of {} is: {:.3f}'.format(r1, rq(float(r1))))

        elif raiz == 'cubic':
            r2 = input ('\nType a value: ')
            print('\nThe cubic root of {} is: {:.3f}'.format(r2, rc(float(r2))))


    elif op == '6':
        base = float(input('\nWhat is the base value? '))
        expoente = float(input('\nWhat is the exponent value? '))
        print('\nThe value of the base is {} and the exponent is {}, so the result is {}'.format(base, expoente, ptc(base, expoente)))


    elif op == '7':
        a = int(input('\nType the first value: '))
        b = int(input('\nType the second value: '))
        c = int(input('\nNow the third value: '))

        resultado = bashkara(a, b ,c)
        print('\n{}'.format(resultado))

    elif op == '8':
        num = float(input('\nType the value: '))
        base = float(input('\nType the base: '))
        print("\nThe logarithm result is: ", callog(num, base))
    else:
        print('\nNot a valid operation!! ')
