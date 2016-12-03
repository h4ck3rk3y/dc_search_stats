# Converts nicks to IPS in log.csv
with open('ips.csv', 'r') as ips:
	nick_dic = {}
	for line in ips:
		data = line.split(',')
		nick_dic[data[0]] = data[1]
	with open('log.csv', 'r') as logfile:
		with open('output.csv', 'w') as output:
			for line in logfile:
				if 'Hub:' in line:
					last_comma=line.rfind(',')+5
					nick = line[last_comma:line.rfind(':')]
					if nick in nick_dic:
						output.write(line.replace('Hub:%s'%(nick), nick_dic[nick].strip()))
					else:
						output.write(line)
				else:
					output.write(line)

