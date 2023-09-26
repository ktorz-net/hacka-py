import sys

class Option :
    def __init__(self, name, letter="", default=False, help="" ):
        self._name= name
        self._letter= letter
        self._default= default
        self._value= self._default
        self._help= help

    # set:
    def setOn(self, aThing):
        if type( self._default ) is int :
            self.value= int(aThing)
        elif type( self._default ) is float :
            self.value= float(aThing)
        else :
            self._value= aThing

    # test:
    def needArgument(self) :
        return not type( self._default ) is bool
    
    # String:
    def help(self):
        s= "\t"
        if self._letter != "" :
            s+= f"-{self._letter}, "
        s+= f"--{self._name}\n"
        return s + f"\t\t{self._help} (default: {self._default})"
    
    def __str__(self) :
        s= f"-{self._letter}"
        if s == "-" :
            s= f"--{self._name}"
        if self.needArgument() :
            s+= f" {self._value}"
        return s

class Command :
    # Constructor:
    def __init__(self, name, options=[], help=""):
        self._cmd= name
        self._options= { o._name:o for o in options }
        self._arguments= []
        self._help= help
        self._ready= False
        self._log= ""
    
    # Accessor:
    def name(self):
        return self._name
    
    def options(self):
        return [ self._options[m] for m in self._options ]
    
    def option(self, name):
        return self._options[name]._value
    
    def arguments(self):
        return self._arguments

    def ready(self):
        return self._ready
    
    def log(self):
        return self._log

    def optionShort(self):
        dico= {}
        for opName in self._options :
            if self._options[opName]._letter != "" :
                dico[ self._options[opName]._letter ]= opName
        return dico

    # interpret a command line (typically sys.argv):
    def process(self, commandLine ):
        self._ready= False
        self._log= ""
        self._arguments= []
        dico= self.optionShort()
        cmd= commandLine.pop(0)
        if self._cmd != cmd :
            self._log= f"> {cmd} is not the expected command !!!"
            return self._ready
        
        while len(commandLine) != 0 :
            isOption= False
            option= -1
            element= commandLine.pop(0)
            if element[:2] == '--' :
                if not element[2:] in self._options :
                    self._log= f"> {element[2:]} is not an option !!!"
                    return self._ready
                isOption= True
                option= self._options[element[2:]]
            elif element[:1] == '-' :
                for op in element[1:] :
                    if not op in dico :
                        self._log= f"> -{op} is not an option !!!"
                        return self._ready
                for op in element[1:len(element)-1] :
                    if self._options[ dico[op] ].needArgument() :
                        self._log= f"> {dico[op]} option require an argument !!!"
                        return self._ready
                    self._options[ dico[op] ]._value= True
                isOption= True
                option= self._options[ dico[ element[-1] ] ]

            if isOption :
                if option.needArgument() :
                    if len(commandLine) == 0 or commandLine[0][0] == "-" :
                        self._log= f"> {option._name} option require an argument !!!"
                        return self._ready
                    option.setOn( commandLine.pop(0) )
                else :
                    option._value= True
            else :
                self._arguments.append( element )
        self._ready= True
        return self._ready

    # String:
    def help(self) :
        h= f"command: {self._cmd} [OPTIONS] [ARGUMENTS]\n\n\t{self._help}\n\nOPTIONS:\n"
        for op in self.options() :
            h+= op.help()
            h+= "\n\n"
        return h

    def __str__(self) :
        cmdLine= [self._cmd]
        for op in self.options() :
            if op.needArgument() or op._value :
                cmdLine.append( str(op) )
        cmdLine+= self._arguments
        return " ".join( cmdLine )

# Old...

def serverFromCmd():
    if len(sys.argv) > 1 :
        url= sys.argv[1]
        if ':' in url :
            url= url.split(":")
            host= url[0]
            port= int(url[1])
        else :
            host= url
            port= 1400
    else :
        host= 'localhost'
        port= 1400
    return host, port

class StartCmd():
    def __init__( self, gameName, modeLst, options= {}, parameters= {} ) :
        self.cmd= "."
        self.gameName= gameName
        self.modeLst= modeLst + ["help"]
        self.mode= modeLst[0]
        self.prmDsc= parameters
        self.parameters= { p:self.prmDsc[p][1] for p in self.prmDsc }
        self.optDsc= options
        self.options= { p:False for p in self.optDsc }
        self.interpret()

    # Accessor:
    def option(self, o):
        return self.options[o]
    
    def parameter(self, p):
        return self.parameters[p]

    def interpret(self):
        shArgs= sys.argv
        self.cmd= shArgs.pop(0)
        while len(shArgs) != 0 :
            v= shArgs.pop(0)
            if v[0] == '-' :
                if not self.interpretParam(v, shArgs ) :
                    print( "/!\\ invalid parameters ")
                    self.mode= "help"
            elif v in self.modeLst :
                if self.mode != "help" :
                   self.mode= v
            else :
                print( "/!\\ unknown mode "+ v )
                self.mode= "help"
        if self.mode == "help" :
            print( self.help() )

    def interpretParam( self, params, shArgs ):
        ok= True
        for p in params[1:-1] :
            if p in self.optDsc :
                self.options[p]= True
            else :
                ok= False

        p= params[-1]
        if p in self.prmDsc :
            self.parameters[p]= shArgs.pop(0)
        elif p in self.optDsc :
            self.options[p]= True
        else :
            ok= False

        return ok

    # print:
    def __str__(self):
        s= f"{self.cmd} {self.gameName} (mode: {self.mode}"
        for op in self.options :
            if self.options[op] :
                s+= ", "+ self.optDsc[op][0]
        for pa in self.parameters :
            s+= f", {self.prmDsc[pa][0]}: {self.parameters[pa]}" 
        return s+")"

    def help(self):
        help= f"{self.gameName} {self.cmd} command : {self.cmd} [options/parameters] mode OR `{self.cmd} help` (to get this help)"
        help+= f"\n  Example: python3 {self.cmd} {self.modeLst[0]}"
        help+= f"\n  Modes: [{ ', '. join(self.modeLst) }]"
        help+= "\n  Options:"
        for op in self.optDsc :
            help += f"\n     -{op} : {self.optDsc[op][0]}"
        help+= "\n  Parameters:"
        for p in self.prmDsc :
            help += f"\n     -{p} : {self.prmDsc[p][0]} (default: {self.prmDsc[p][1]})"
        return help
