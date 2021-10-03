cz=[0,1,2,3,4,5,6,7,8,9]
C=[['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001'],
    ['0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100', '1100', '1101'],
    ['0000', '0001', '0010', '0011', '0100', '1011', '1100', '1101', '1110', '1111'],
    ['0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100'],
    ['0110000 ', '0110001', '0110010', '0110011', '0110100', '0110101', '0110110', '0110111', '0111000', '0111001']]
a=input('Introduceti codul in care vor fi scrise cifrele:')
if a=='Direct':
    print('In codul Direct:', C[0])
elif a=='Gray':
    print('In codul Gray:', C[1])
elif a=='Aiken':
    print('In codul Aiken:', C[2])
elif a=='Exces 3':
    print('In codul Exces 3:', C[3])
elif a=='ASCII':
    print('In codul ASCII:', C[4])
else:
    print('Nu exista astfel de cod')