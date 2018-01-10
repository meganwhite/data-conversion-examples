with open('myfile.txt') as f:
    myfile_text = f.read()

myfile_text_plus_hello = myfile_text + ". Hello from fileo.py!!"

with open('testwrite.txt', 'w') as f:
    f.write(myfile_text_plus_hello)