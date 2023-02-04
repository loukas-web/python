import xml.etree.ElementTree as ET

file = '/home/loukas/Downloads/gokuthelegend.wordpress.com-2023-01-31-19_25_23-29sgknitilhqubo1pqmqys4thesckljo/text' \
       '.txt'
xml_file = '/home/loukas/Downloads/gokuthelegend.wordpress.com-2023-01-31-19_25_23-29sgknitilhqubo1pqmqys4thesckljo' \
           '/gokuthelegend.wordpress.com-2023-01-31-19_25_17/site.wordpress.2023-01-31.000.xml'

mytree = ET.parse(xml_file)
myroot = mytree.getroot()
print(myroot)

xlm = []
for item in myroot[0]:
    for x in item:
        if 'encoded' in str(x.tag):
            text = str(x.text)
            print(text)
            xlm.append(text)

with open(file, 'w') as a:
    a.writelines(xlm)
