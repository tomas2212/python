class Interface(object): # contains read() and write()
    """Represents Interface for IO read and write."""

    def read(self):
        return raw_input()
        
    def write(self, data):
        print data



class Shell(object):

	COMMDICT = {}

	def __init__(self, inst):
		self.inst = inst

	def add_command(self, word, function):
		self.COMMDICT[word] = function

	def parse(self, text):
		command, arg = text.split(' ')
		if command in self.COMMDICT:
			return self.COMMDICT[command](arg)
		return text

	def run(self):
		while True:
			input = self.inst.read()
			if not input:
				break
			result = self.parse(input)
			self.inst.write(result)