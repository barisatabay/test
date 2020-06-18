USE paramiko.SSHClient()

class hardware:
	def __init__(self)
		serial=""
		hostname=""
		type=""
		ip=""
	def fetch(ip,user,pass):
		conn()

host = "192.168.1.21"
port = 22
username = "baris"

## şifreyi nasıl gizlicez
password = "<bunu hashlemek gerek"

## komutları buraya girelim
## komutları dışardan girebiliriz
## menu'den sec, guncelle gibi
komutlar = {"sw_serial":"", "sw_hostname":"","srv_serial":"dmidecode -s system-serial-number","srv_hostname":"hostname"}
proxy_command1 = "vepc"
##  Çıktıyı dosyaya yazdıralım

switch_command1 = "hostname"
server_command1 = ""


## Eger hostname -- sw ise 

## Eger hostname  -- server ise



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(switch_command1)
lines = stdout.readlines()
print(lines)
OUTPUT