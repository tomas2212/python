import optparse
import shlex
import ConfigParser

parser = optparse.OptionParser("%prog [options]") # 1st argument is usage, %prog is replaced with sys.argv[0]
parser.add_option(
    "-s", "--server",    # short and long option
    dest="server",       # not needed in this case, because default dest name is derived from long option
    type="string",     # "string" is default, other types: "int", "long", "choice", "float" and "complex"
    action="append",      # "store" is default, other actions: "store_true", "store_false" and "append"
    default=[], # set default value here, None is used otherwise
   
)

parser.add_option(
    "-p", "--port",    
    dest="port",       
    type="string",      
    
)

parser.add_option(
    "-t", "--timeout",    
    dest="timeout",       
    type="int",       
    
)

config = ConfigParser.SafeConfigParser()
config.read("config.ini")
sCfg = config.get("section","server")
pCfg = config.get("section","port")
tCfg =  config.get("section","timeout")

print sCfg, pCfg, tCfg

options, args = parser.parse_args()
c = ConfigParser()
for a in args:
   read(a)
options = vars(options)
sd = c.items("config.ini") # sd = set default
config = dict(sd)
config.update(options)

"""
f = file("config.ini","r").read()
lexer = shlex.split(f)
print lexer
"""
print options

