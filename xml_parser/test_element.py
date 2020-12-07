import  lxml.etree as ElementTree

if __name__ == '__main__':
    print("test element")
    content = '''
	<tag name="struct"> 
	    <value name="key" value="100">
		</value>
	</tag>
    
	'''
    tree = ElementTree.fromstring(content)
    for child in tree:
             if child.attrib:
                 print(dict(child.attrib))
             else:
                 print(child.text)
