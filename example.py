import argparx
b = True
parser = argparx.ArgParserX()

parser.take_args() #take args from sys.argv[1:]
parser.program_def("prints number") #definition of the program
x = parser.object_arg("-x", helparg="print number") #single letter argument example
y = parser.object_arg("--yiks", helparg="for how many cycles") #many-letters argument example
f = parser.object_arg("-f", helparg="flag", flag=1) #flag example
parser.help_arg() #init help of the program

if bool(y) == True:
    for i in range(0,int(y)):
        print x
        if f:
            print "hihi"
elif bool(y) == False:
    print x
    if f:
        print "hihi"

print "Done. x was {}, y was {}, f was {}".format(str(x), str(y), str(f))
