block_size = 1
with open("1A.BIN","rb") as f1,open("2A.BIN",'rb') as f2,open("3A.BIN","rb") as f3,\
	open('1B.BIN',"rb") as f1b,open ("1C.BIN","rb") as f1c:
	while True:
		a = f1.read(block_size)
		if not(a):
			break
		a = int().from_bytes(a, byteorder='big', signed=False)
		a2 = int().from_bytes(f1b.read(block_size), byteorder='big', signed=False)
		a3 = int().from_bytes(f1c.read(block_size), byteorder='big', signed=False)
		b = int().from_bytes(f2.read(block_size), byteorder='big', signed=False)
		c = int().from_bytes(f3.read(block_size), byteorder='big', signed=False)
		if (c-b == b-a and c!=b and a==a2 and a==a3):
			print("{seg:x}:{off:x}".format(off = f1.tell()&0xffff,seg=0x477+(f1.tell()>>20))) 
			print(a,b,c)



