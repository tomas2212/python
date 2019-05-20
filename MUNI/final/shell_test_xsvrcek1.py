import unittest
from shell import Shell
from commands.quit import quit
 
"""test interface"""

class TestInterface(object):
    def __init__(self, input):
        self.input = input
        self.output = []

    def read(self):
        return self.input.pop(0)

    def write(self, msg):
        self.output.append(msg)


class ShellTest(unittest.TestCase):
    def test_process(self):
        i = TestInterface([])
        s = Shell(i)

        self.assertEqual(s.process('some text'), 'some text')

    def test_shell(self):
        i = TestInterface(['some text', 'quit'])
        s = Shell(i)
        s.add_command('quit', quit)
        s.run()
        self.assertEquals(i.output, ['some text'])
         
if __name__ == '__main__':
    unittest.main()
