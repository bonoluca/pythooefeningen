f = open("test_teskstbestand_maken.txt","w")
f.write("dit is regel 1 ")
f.write("dit is regel 2 ")
f.close()

f= open("test_teskstbestand_maken.txt","a")
f.write("dit is regel 3 ")
f.write("dit is regel 4 ")
f.close()

f=open("test_teskstbestand_maken.txt","r")
inhoud = f.read()
print(inhoud)

f.close()

