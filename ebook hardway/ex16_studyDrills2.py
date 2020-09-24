from sys import argv

script, filename = argv

txt = open(filename)

print "This is the file you ask me to read %r." % filename
print txt.read()

txt.close()
