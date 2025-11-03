
'''Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.'''


def dec_to_bin(dec):
    '''Decimal to binary conversion'''

    binary = ''

    while dec > 0:
        binary += str(dec % 2)
        dec = dec // 2

    return binary[::-1]

def to_actet_conversion(num_seq):
    '''Conversion of num sequence into IPv4 actet'''

    empty_actet = '00000000'
    zero_counter = 0
    actet_val = 0

    if num_seq == empty_actet:
        return 0
    
    '''Remove extra zeros before main binary digit'''
    for e in num_seq:
        if e == '0':
            zero_counter += 1
        else:
            num_seq = num_seq[zero_counter:]
            break

    num_amount = len(num_seq)
    iteration = 1
    
    '''Conversion binary to decimal'''
    for e in range(num_amount):
        actet_val += int(num_seq[e]) * 2**(num_amount - iteration)
        iteration += 1

    return actet_val

def int32_to_ip(int32):
    '''General function of int32_to_ip'''
    binary = dec_to_bin(int32)
    actets = []
    bin_num_amount = len(binary)
    binary = '0' * (32 - bin_num_amount) + binary
    interval = 0
    
    '''Making 4 actets of IPv4'''
    for i in range(8, 33, 8):
        actets.append(binary[interval:i])
        interval += 8

    '''Conversion every actet into decimal'''
    for i in range(4):
        actets[i] = to_actet_conversion(actets[i])
        
    return '.'.join(str(x) for x in actets)
