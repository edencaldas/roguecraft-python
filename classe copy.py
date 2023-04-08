class Servidor(object):
	def __init__(self, nome, ip, desc):
		self.nome = nome
		self.ip = ip
		self.desc = desc

xs01 = Servidor("xs01", "192.168.200.201", "Xenserver 01")

print(xs01.nome)

