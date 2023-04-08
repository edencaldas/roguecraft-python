class Servidor(object):
	def __init__(self, nome, ip, desc):
		self.nome = nome
		self.ip = ip
		self.desc = desc


	def informa(self):
		self.msg = """
			Informacoes do Servidor:
			Nome: {0}
			IP:{1}
			Desc:{2}
			""".format(self.nome, self.ip, self.desc)

		print (self.msg)

	def print_nome(self):
		print (self.nome)


xs01 = Servidor("xs01", "192.168.200.201", "Xenserver 01")
xs02 = Servidor("xs02", "192.168.200.202", "Xenserver 02")

print (xs01.nome)

xs01.informa()
xs02.informa()


mylist = []

mylist.append(xs01)
mylist.append(xs02)

xs01.nome = "xs99"

xs01.informa()

print (mylist[1].nome)
print (xs02.nome)