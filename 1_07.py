#! /usr/bin/python2
#coding=utf-8
#python2

str1 = 'attack at dawn'

def str2bin(str1):
	return ''.join([('{0:b}'.format(i)).zfill(8) for i in bytearray(str1)])

print(str2bin(str1))

hex_str = '09e1c5f70a65ac519458e7e53f36'

def hex2bin(hex_str):
	return ''.join([bin(int(char,16))[2:].zfill(4) for char in hex_str])
#int(char,16)将16进制字符串转变为10进制
#.zfill返回指定长度的字符串

print(hex2bin(hex_str))

#XOR
bin1 = str2bin(str1)
bin2 = hex2bin(hex_str)

def char_xor(c1,c2):
	if c1 == c2:
		return '0'
	else:
		return '1'

#result = ''.join([char_xor(str3[i],str4[i]) for i in range(0,len(str3)) ])

bin3 = ''

for i in range(0,len(bin1)):
	num1 = char_xor(bin1[i],bin2[i])
	bin3 = bin3 + num1

print(bin3)

str2 = 'attack at dusk'

bin4 = str2bin(str2)

bin5 = ''

for j in range(0,len(bin3)):
	num2 = char_xor(bin3[j],bin4[j])
	bin5 = bin5 + num2

print(bin5)

#二进制转为十六进制
def bin2hex(bin5):
	result = ''

	max_len = 4

	for k in range(0,len(bin5) // max_len):
		split = bin5[k*max_len:(k+1)*max_len]
		num3 = int(split,2)
		hex_str1 = hex(num3)[2:]
		result = result + hex_str1

	return result
	
print(bin2hex(bin5))
