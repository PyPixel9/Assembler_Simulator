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


cmd = sys.stdin.read().split('\n')
cmd = [x.split() for x in cmd if x != '\n' and x != '']
if len(cmd) > 256:
    print("Compilation Error: Memory Overflow!")
    exit()
ops_A = ['add', 'sub', 'mul', 'xor', 'or', 'and']
ops_B = ['mov', 'ls', 'rs']
ops_C = ['mov', 'div', 'not', 'cmp']
ops_D = ['ld', 'st']
ops_E = ['jmp', 'jlt', 'jgt', 'je']
ops_F = ['hlt']
regs = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R0']
variables = {}
var_count = 0
labels = {}
no_cmds = len(cmd)
e_count = 0

if not cmd:
    exit()

for w in range(len(cmd)):
    i = cmd[w]
    if ':' in i[0]:
        labels[i[0][:-1]] = w
        i.pop(0)

if ['hlt'] not in cmd:
    e_count += 1
    print('Syntax Error: hlt instruction is not present in the file.')

if cmd[-1] != ['hlt'] and ['hlt'] in cmd:
    e_count += 1
    print('Syntax Error: hlt instruction is not found at the EOF')

if cmd.count(['hlt']) > 1:
    e_count += 1
    print('Syntax Error: There are more than 1 hlt instructions in the file.')

while cmd != [] and cmd[0][0] == 'var':
    variables[cmd[0][1]] = var_count
    cmd.pop(0)
    var_count += 1

for i in variables.keys():
    variables[i] += no_cmds-var_count

for w in range(len(cmd)):
    i = cmd[w]
    if 'var' in i:
        e_count += 1
        print('Syntax Error: Invalid variable declaration in line %d' % (w + var_count + 1))
        continue
    if ':' in ''.join(i):
        e_count += 1
        print('Syntax Error: Invalid label declaration in line %d' % (w + var_count + 1))
        continue
    if 'FLAGS' in i:
        if i[0] != 'mov':
            e_count += 1
            print('Syntax Error: Invalid use of Flag registers in line %d' % (w + var_count + 1))
            continue
        if i[2] != 'FLAGS':
            e_count += 1
            print('Syntax Error: Invalid use of Flag registers in line %d' % (w + var_count + 1))
            continue

    try:
        if i[0] not in ops_A + ops_B + ops_C + ops_D + ops_E + ops_F:
            e_count += 1
            print('Syntax Error: Invalid instruction in line %d' % (w + var_count + 1))
            continue
    except IndexError:
        e_count += 1
        print('Syntax Error: Incorrect use of syntax in line %d' % (w + var_count + 1))
        continue

    if i[0] == 'mov':
        try:
            if i[1] not in regs:
                e_count += 1
                print('Syntax Error: Invalid use of registers in line %d' % (w + var_count + 1))
                continue
            if '$' in i[2] and '.' in i[2]:
                e_count += 1
                print('Syntax Error: Invalid literal value in line %d' % (w + var_count + 1))
                continue
            if '$' in i[2] and (0 > int(i[2][1:]) or int(i[2][1:]) > 255):
                e_count += 1
                print('Syntax Error: Invalid literal value in line %d' % (w + var_count + 1))
                continue
            if '$' not in i[2] and i[2] not in (regs + ['FLAGS']):
                e_count += 1
                print('Syntax Error: Invalid use of registers in line %d' % (w + var_count + 1))
                continue
        except IndexError:
            e_count += 1
            print("Syntax Error: Incorrect use of syntax at line %d" % (w + var_count + 1))
            continue

    else:
        if i[0] in ops_A:
            try:
                if i[1] not in regs or i[2] not in regs or i[3] not in regs:
                    e_count += 1
                    print('Syntax Error: Invalid use of registers in line %d' % (w + var_count + 1))
                    continue
            except IndexError:
                print('General Syntax Error: Invalid use of syntax in line %d' % (w + var_count + 1))
                continue
        if i[0] in ops_C:
            if i[1] not in regs or i[2] not in regs:
                e_count += 1
                print('Syntax Error: Invalid use of registers in line %d' % (w + var_count + 1))
                continue

        if i[0] in ops_B:
            try:
                if i[1] not in regs:
                    e_count += 1
                    print('Syntax Error: Invalid use of registers in line %d' % (w + var_count + 1))
                    continue
                if '$' in i[2] and '.' in i[2]:
                    e_count += 1
                    print('Syntax Error: Invalid literal value in line %d' % (w + var_count + 1))
                    continue
                if '$' in i[2] and (0 > int(i[2][1:]) or int(i[2][1:]) > 255):
                    e_count += 1
                    print('Syntax Error: Invalid literal value in line %d' % (w + var_count + 1))
                    continue
                if '$' not in i[2]:
                    e_count += 1
                    print("Syntax Error: '$' sign must be used before a literal value in line %d" % (w + var_count + 1))
                    continue
            except IndexError:
                e_count += 1
                print("Syntax Error: Incorrect use of syntax at line %d" % (w + var_count + 1))
                continue
    if i[0] in ops_D:
        try:
            if i[1] not in regs:
                e_count += 1
                print('Syntax Error: Invalid use of registers in line %d' % (w + var_count + 1))
                continue
            if i[2] not in variables:
                e_count += 1
                print("Syntax Error: Use of undefined variable '%s' in line %d" % (i[2], (w + var_count + 1)))
                continue
        except IndexError:
            e_count += 1
            print("Syntax Error: Incorrect use of syntax at line %d" % (w + var_count + 1))
            continue
    if i[0] in ops_E:
        try:
            if i[1] not in labels:
                e_count += 1
                print("Syntax Error: Use of undefined label '%s' in line %d" % (i[1], (w + var_count + 1)))
                continue
        except IndexError:
            e_count += 1
            print("Syntax Error: Incorrect use of syntax at line %d" % (w + var_count + 1))
            continue

