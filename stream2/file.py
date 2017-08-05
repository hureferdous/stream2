fw = open('sample.text', 'w')
fw.write('This is a text file \n')
fw.write('My name is Hure \n')
fw.close()

fr = open('sample.text','r')
text = fr.read()
print(text)
fr.close()