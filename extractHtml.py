import json
import codecs

inputFile = open("elec_file2.json",'r')
jsonArr = json.load(inputFile)
count =3
for jsonObj in jsonArr:
    outputfile = codecs.open(str(count)+'.html','w','utf-8')
    outputfile.write(jsonObj['_source']['raw_text'])
    outputfile.close()
    count = count + 1