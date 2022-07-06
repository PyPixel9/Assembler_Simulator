import sys
decode = {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'FLAGS': 7}


def getcode(o):
    if o == 'add':
        return '10000'
    elif o == 'sub':
        return '10001'
    elif o == 'movI':
        return '10010'
    elif o == 'movR':
        return '10011'
    elif o == 'ld':
        return '10100'
    elif o == 'st':
        return '10101'
    elif o == 'mul':
        return '10110'
    elif o == 'divi':
        return '10111'
    elif o == 'rs':
        return '11000'
    elif o == 'ls':
        return '11001'
    elif o == 'xor':
        return '11010'
    elif o == 'or':
        return '11011'
    elif o == 'and':
        return '11100'
    elif o == 'not':
        return '11101'
    elif o == 'cmp':
        return '11110'
    elif o == 'jmp':
        return '11111'
    elif o == 'jlt':
        return '01100'
    elif o == 'jgt':
        return '01101'
    elif o == 'je':
        return '01111'
    elif o == 'hlt':
        return '01010'


def A(opcode, reg1, reg2, reg3):
    a = list(getcode(opcode))
    x1 = list(f'{decode.get(reg1):03b}')
    x2 = list(f'{decode.get(reg2):03b}')
    x3 = list(f'{decode.get(reg3):03b}')

    a = a + ['0', '0']
    a = a + x1
    a = a + x2
    a = a + x3
    print(''.join(a))


def B(opcode, reg1, imm):
    a = list(getcode(opcode))
    x1 = list(str(f'{decode.get(reg1):03b}'))
    imm = list(f'{int(imm):08b}')
    a = a + x1
    a = a + imm
    print(''.join(a))


def C(opcode, reg1, reg2):
    a = list(str(getcode(opcode)))
    x1 = list(f'{decode.get(reg1):03b}')
    x2 = list(f'{decode.get(reg2):03b}')
    a = a + ['0', '0', '0', '0', '0']
    a = a + x1
    a = a + x2
    print(''.join(a))


def D(opcode, reg1, addr):
    a = list(str(getcode(opcode)))
    x1 = list(f'{decode.get(reg1):03b}')
    addr = list(f'{addr:08b}')
    a = a + x1
    a = a + addr
    print(''.join(a))


def E(opcode, addr):
    a = list(str(getcode(opcode)))
    addr = list(f'{addr:08b}')
    a = a + ['0', '0', '0']
    a = a + addr
    print(''.join(a))


def F(opcode):
    a = list(str(getcode(opcode)))
    a = a + ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    print(''.join(a))
