import hackapy.command as cmd

def test_commandClasses():
    anOption= cmd.Option("option")
    aCommand= cmd.Command("command")
    
    assert( type(anOption) is cmd.Option )
    assert( type(aCommand) is cmd.Command )

def test_option():
    anOption= cmd.Option("option")
    test = ("\t--option\n"
            "\t\t (default: False)")
    
    print( f">\n{anOption.help()}\nvs\n{test}" )
    assert( str(anOption.help()) == test )

def test_optionFeed():
    anOption= cmd.Option( "number", "n", 2, "number of games (an integer)" )
    test = ("\t-n, --number\n"
            "\t\tnumber of games (an integer) (default: 2)")
    
    print( f">\n{anOption.help()}\nvs\n{test}" )
    assert( str(anOption.help()) == test )
        
def test_commandProcess():
    aCommand= cmd.Command(
        "commandName",
        options= [
            cmd.Option( "number", "n", 2, "number of games (an integer)" ),
            cmd.Option( "port", default=1400 ),
            cmd.Option( "test", "t" ),
            cmd.Option( "server", "s", "localhost" )
        ]
    )
    
    assert( aCommand.process( commandLine= ['Bob'] ) == False )
    assert( aCommand.ready() == False )
    assert( aCommand.log() == "> Bob is not the expected command !!!" )

    assert( aCommand.process( ['commandName'] ) == True )
    assert( aCommand.ready() == True )
    assert( aCommand.log() == "" )

    assert( aCommand.process( commandLine= ['commandName', "--Bob"] ) == False )
    assert( aCommand.ready() == False )
    assert( aCommand.log() == "> Bob is not an option !!!" )

    assert( aCommand.optionShort() == { "n":"number", "t": "test", "s":"server" } )

    assert( aCommand.process( commandLine= ['commandName', "-b"] ) == False )
    assert( aCommand.ready() == False )
    assert( aCommand.log() == "> -b is not an option !!!" )

    assert( aCommand.process( commandLine= ['commandName', "-bs"] ) == False )
    assert( aCommand.ready() == False )
    assert( aCommand.log() == "> -b is not an option !!!" )

    assert( aCommand.process( commandLine= ['commandName', "-sn"] ) == False )
    assert( aCommand.ready() == False )
    assert( aCommand.log() == "> server option require an argument !!!" )

    assert( aCommand.process( commandLine= ['commandName', "-ts", "localhost"] ) == True )
    assert( aCommand.ready() == True )
    assert( aCommand.log() == "" )

    assert( aCommand.process( commandLine= ['commandName', "-ts" ] ) == False )
    assert( aCommand.ready() == False )
    assert( aCommand.log() == "> server option require an argument !!!" )

    assert( aCommand.process( commandLine= ['commandName', "--server" ] ) == False )
    assert( aCommand.ready() == False )
    assert( aCommand.log() == "> server option require an argument !!!" )

    assert( aCommand.process( commandLine= ['commandName', "Hello", "--server", "localhost", "World"] ) == True )
    assert( aCommand.ready() == True )
    assert( aCommand.arguments() == ["Hello", "World"] )
    assert( aCommand.log() == "" )

    print( aCommand )
    assert( str(aCommand) == "commandName -n 2 --port 1400 -t -s localhost Hello World" )

    assert( aCommand.option("number") == 2 )
    assert( aCommand.option("port") == 1400 )
    assert( aCommand.option("test") == True )
    assert( aCommand.option("server") == "localhost" )

def test_commandHelp():
    aCommand= cmd.Command(
        "commandName",
        [
            cmd.Option( "number", "n", 2, "number of games (an integer)" ),
            cmd.Option( "port", default=1400 ),
            cmd.Option( "test", "t" ),
            cmd.Option( "server", "s", "localhost" )
        ],
        "A Command Test"
    )

    test= ( "command: commandName [OPTIONS] [ARGUMENTS]\n"
            "\n"
            "\tA Command Test\n"
            "\n"
            "OPTIONS:\n"
            "\t-n, --number\n"
            "\t\tnumber of games (an integer) (default: 2)\n"
            "\n"
            "\t--port\n"
            "\t\t (default: 1400)\n"
            "\n"
            "\t-t, --test\n"
            "\t\t (default: False)\n"
            "\n"
            "\t-s, --server\n"
            "\t\t (default: localhost)\n"
            "\n" )

    print( f"{aCommand.help()}\nvs\n{test}" )

    for l1, l2 in zip( aCommand.help().split("\n"), test.split("\n") ) :
        assert( l1 == l2 )
    
def test_start_server():
    pass
