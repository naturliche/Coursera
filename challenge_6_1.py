#! /usr/bin/python3
#coding=utf-8

import base64

#如何解密base64加密的文件
def decodeb64(f_org):
	f_now=open(f_org,'r') #以只读方式打开文件
	content=f_now.read()  #从文件读取所有
	content1=base64.b64decode((content))
	with open(f_org,'wb+') as f_now:  #以二进制格式打开一个文件用于读写
		f_now.write(content1)
		#f_org.close(content)  error: AttributeError: 'str' object has no attribute 'close'

if __name__ == '__main__':
	f_org='E:/crypto0x/crypto_challenge/1_6/TestFile_Challenge06_CSIS463_1.txt'
	deci(f_org)

#bin函数所转换的二进制不符合要求
def binary(n):
	return '{0:08b}'.format(n)

#两个二进制数异或如何算出1的个数
def hammingDistance(s1,s2):
	d=0
	for c1,c2 in zip(s1,s2):
		if c1!=c2:
			b1=binary(c1)
			b2=binary(c2)
			while b1 or b2:
				e1=b1&1     #移位操作
				e2=b2&1
				d+=e1^e2
				b1>>=1  
				b2>>=1
	return d
	
#算出hammingDistance后，把密文分段
def