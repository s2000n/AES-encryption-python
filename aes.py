def hx1(v1):
    hex_v1 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
               'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    msg_len = len(v1)
    final = ''
    for i in range(0, msg_len):
        final = final + hex_v1[v1[i]]
    return final


def hx2(v1):
    bin_v1 = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
               '0100': '4', '0101': '5', '0110': '6', '0111': '7',
               '1000': '8', '1001': '9', '1010': 'a', '1011': 'b',
               '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
    msg_len = len(v1)
    lst = []
    final = ''
    count = 0
    i = 0
    while count != msg_len:
        lst = lst + [v1[count:count + 4]]
        final = final + bin_v1[lst[i]]
        i = i + 1
        count = count + 4

    return final


def substitution_box(rc):
    hex_v1 = {'0': '0', '1': '1', '2': '2', '3': '3',
               '4': '4', '5': '5', '6': '6', '7': '7',
               '8': '8', '9': '9', 'a': '10', 'b': '11',
               'c': '12', 'd': '13', 'e': '14', 'f': '15'}

    s_box = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
                      ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
                      ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
                      ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
                      ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
                      ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
                      ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
                      ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
                      ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
                      ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
                      ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
                      ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
                      ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
                      ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
                      ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
                      ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

    substitution = s_box[int(hex_v1[rc[0]])][int(hex_v1[rc[1]])]
    return substitution


def xor(left, right):
    final = ''
    l_len = len(left)
    for i in range(0, l_len):
        if left[i] == right[i]:
            final = final + '0'
        elif left[i] != right[i]:
            final = final + '1'
    return final


def col_to_row(v1):
    row = []
    for i in range(0, 4):
        col = []
        for j in range(0, 4):
            col = col + [v1[j][i]]
        row = row + [col]
        
    return row


def row_to_col(v1):
    col = []
    for i in range(0, 4):
        row = []
        for j in range(0, 4):
            row = row + [v1[j][i]]
        col = col + [row]
    return col

def substitute_byte(state):
    row = []
    for i in range(0, 4):
        col = []
        for j in range(0, 4):
            col = col + [substitution_box(state[i][j])]
        row = row + [col]
    return row

def shift_row(sub_bytes):
    state_array = []

    first = sub_bytes[0]
    state_array = state_array + [first]

    second = [sub_bytes[1][1]] + [sub_bytes[1][2]] + [sub_bytes[1][3]] + [sub_bytes[1][0]]
    state_array = state_array + [second]

    third = [sub_bytes[2][2]] + [sub_bytes[2][3]] + [sub_bytes[2][0]] + [sub_bytes[2][1]]
    state_array = state_array + [third]

    four = [sub_bytes[3][3]] + [sub_bytes[3][0]] + [sub_bytes[3][1]] + [sub_bytes[3][2]]
    state_array = state_array + [four]

    return state_array

def multiply_by_02(inp):
    bin_v1 = hx1(inp[0]) + hx1(inp[1])
    final = ''
    if bin_v1[0] == '1':

        bin_v1 = bin_v1[1:len(bin_v1)] + '0'

        final = xor(bin_v1, hx1('1b'))
    elif bin_v1[0] == '0':
        final = bin_v1[1:len(bin_v1)] + '0'

    return final

def multiply_by_03(inp):
    mix = multiply_by_02(inp)
    final = xor(mix, hx1(inp))

    return final

def row0(row):
    xor01 = xor(multiply_by_02(row[0]), multiply_by_03(row[1]))
    xor23 = xor(hx1(row[2]), hx1(row[3]))
    final_xor = xor(xor01, xor23)

    return hx2(final_xor)

def row1(row):
    xor01 = xor(hx1(row[0]), multiply_by_02(row[1]))
    xor23 = xor(multiply_by_03(row[2]), hx1(row[3]))
    final_xor = xor(xor01, xor23)

    return hx2(final_xor)

def row2(row):
    xor01 = xor(hx1(row[0]), hx1(row[1]))
    xor23 = xor(multiply_by_02(row[2]), multiply_by_03(row[3]))
    final_xor = xor(xor01, xor23)

    return hx2(final_xor)

def row3(row):
    xor01 = xor(multiply_by_03(row[0]), hx1(row[1]))
    xor23 = xor(multiply_by_02(row[3]), hx1(row[2]))
    final_xor = xor(xor01, xor23)

    return hx2(final_xor)


def mix_col(s_row):
    final_row = []
    for i in range(0, 4):
        tmp_row = [row0(s_row[i])] + [row1(s_row[i])] + [row2(s_row[i])] + [row3(s_row[i])]
        final_row = final_row + [tmp_row]

    return final_row


def key_expansion(s_key, rnd):
    keys = []
    

    for pos in range(0, 4):
        if pos == 0:
            first_col = []
            tmp = s_key[3]
            t_len = len(tmp)

            for i in range(1, t_len):
                first_col = first_col + [tmp[i]]
            first_col = first_col + [tmp[0]]
            col = []

            f_len = len(first_col)
            for i in range(0, f_len):
                col = col + [substitution_box(first_col[i])]

            tmp_key = []
            for i in range(0, 4):
                sub_key = xor(hx1(s_key[0][i]), hx1(rnd[i]))
                sub_key1 = xor(sub_key, hx1(col[i]))
                tmp_key = tmp_key + [str(hx2(sub_key1))]

            keys = keys + [tmp_key]

        elif pos > 0:
            first_col = []

            for i in range(0, 4):
                sub_key = xor(hx1(s_key[pos][i]), hx1(keys[pos - 1][i]))
                first_col = first_col + [str(hx2(sub_key))]

            keys = keys + [first_col]
 
    return keys


def add_round(plain_text, keys):
    row = []
    for i in range(0, 4):
        col = []
        for j in range(0, 4):
            tmp = xor(hx1(keys[i][j]), hx1(plain_text[i][j]))
            col = col + [hx2(tmp)]
        row = row + [col]

    return col_to_row(row)

def valid_block_size(msg):
    msg_len = len(msg)
    final = msg
    if msg_len > 32:
        print('\nNot a valid size block, Exceeding Block size!')
        final = final[0:32]
        print('\nafter pading: ', final,'\n')
        print('\n____________________________________________________________________________________________________________')
        return final
    elif msg_len % 32 != 0:
        print('\nNot a valid size block')
        for i in range(abs(32 - (msg_len % 32))):
            final = final + '0'
        print('\nafter pading: ', final,'\n')
        print('____________________________________________________________________________________________________________')
        return final
    else:
        print('\nvalid size block\n')
        print('\n____________________________________________________________________________________________________________')
    return msg


def key_and_text_to_matrix(key_string):
    arr = [['00' for _ in range(4)] for _ in range(4)]
    row = 0
    col = 0
    for i in range(0, len(key_string), 2):
        if row < 4 and col < 4:
            if len(key_string[i:i + 2]) == 1:
                arr[row][col] = key_string[i:i + 2] + '0'
            else:
                arr[row][col] = key_string[i:i + 2]
            col = col + 1
            if col > 3:
                row = row + 1
                col = 0
   
    return arr


rnd_const = [['01', '00', '00', '00'], ['02', '00', '00', '00'], ['04', '00', '00', '00'], ['08', '00', '00', '00'],
             ['10', '00', '00', '00'], ['20', '00', '00', '00'], ['40', '00', '00', '00'], ['80', '00', '00', '00'],
             ['1b', '00', '00', '00'], ['36', '00', '00', '00']]


def aes_encryption(plain_text, aes_key):
    add_round_key = add_round(plain_text, aes_key)
    sub_byte = substitute_byte(add_round_key)
    shift_rows = shift_row(sub_byte)
    mix_column = mix_col(row_to_col(shift_rows))
    add_round_key = add_round(mix_column, key_expansion(aes_key, rnd_const[0]))
    aes_key = key_expansion(aes_key, rnd_const[0])
    
    for i in range(1, 9):
        tmp_key = key_expansion(aes_key, rnd_const[i])
        aes_key = tmp_key
        print('\naes key',i,': ',str(aes_key).replace('[','').replace(']','').replace(',','').replace("'",''),'\n')
        sub_byte = substitute_byte(add_round_key)
        print('sub byte',i,': ',str(sub_byte).replace('[','').replace(']','').replace(',','').replace("'",''),'\n')
        shift_rows = shift_row(sub_byte)
        print('shift rows',i,': ',str(shift_rows).replace('[','').replace(']','').replace(',','').replace("'",''),'\n')
        mix_column = mix_col(row_to_col(shift_rows))
        print('mix column',i,': ',str(mix_column).replace('[','').replace(']','').replace(',','').replace("'",''),'\n')
        add_round_key = add_round(mix_column, aes_key)
        print('adding the round key',i,': ',str(add_round_key).replace('[','').replace(']','').replace(',','').replace("'",''),'\n')
        print('____________________________________________________________________________________________________________')
        
    sub_byte = substitute_byte(add_round_key)
    print('\nsub byte : ',str(sub_byte).replace('[','').replace(']','').replace(',','').replace("'",''))
    shift_rows = row_to_col(shift_row(sub_byte))
    print('\nshift rows : ',str(shift_rows).replace('[','').replace(']','').replace(',','').replace("'",''))
    tmp_key = key_expansion(aes_key, rnd_const[9])
    print('\nkey : ', str(tmp_key).replace('[','').replace(']','').replace(',','').replace("'",''))
    aes_key = tmp_key
    print('\naes key : ',str(aes_key).replace('[','').replace(']','').replace(',','').replace("'",''))
    add_round_key = add_round(shift_rows, aes_key)
    print('\nadding the round key :',str(add_round_key).replace('[','').replace(']','').replace(',','').replace("'",''),'\n')

    cipher = ''
    for row in range(0, len(add_round_key)):
        for col in range(0, 4):
            cipher = cipher + add_round_key[col][row]
    return cipher

while True:
    plaintext = input('\nEnter text: ')
    valid_pt_block = valid_block_size(plaintext.lower())
    plaintext_matrix = key_and_text_to_matrix(plaintext.lower())

    key = input('\nEnter key: ')
    valid_k_block = valid_block_size(key.lower())
    key_matrix = key_and_text_to_matrix(key.lower())

    cipher_text = aes_encryption(plaintext_matrix, key_matrix)
    print('____________________________________________________________________________________________________________')
    print('\nEncrypted Text: ', cipher_text)
    print('\n____________________________________________________________________________________________________________')
    x=input('\ndo you wnat encrypt again y/n: ')
    if x == 'n' and x=='no':
        break
    elif x != 'y' and x !='yes':
        print('\nWrong input...')
        break

