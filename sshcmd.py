import threading
import paramiko
import subprocess

def ssh_command(ip, user, password, command):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username = user, password = passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ss_session.exec_command(command)
		print ssh_Session.recv(1024)
	return 

ss_command('10.0.2.15', 'guava', 'box', 'id')