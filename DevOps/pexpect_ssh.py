import pexpect
ssh = pexpect.spawn('ssh python_demo@192.168.1.48')
fout = file('sshlog.txt', 'w')
ssh.logfile = fout

ssh.expect("python_demo@192.168.1.48's password:")

ssh.sendline("123456")
ssh.expect('#')

ssh.sendline('ls ~')
