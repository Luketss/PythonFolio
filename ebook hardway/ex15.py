from sys import argv # importa o argv

script, filename = argv # unpack de dois valores 

txt = open(filename) #recebe o filename do aquivo que contem os dados externos e abre

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open (file_again)

print txt_again.read()
txt.close()
txt_again.close()
