#!/usr/bin/python

import markdown
import sys
import codecs

if len(sys.argv) != 4:
    print 'Usage: {} template.html content.md output.html'.format(sys.argv[0])
    print 'Given: {}'.format(str(sys.argv));
    exit(1);

with open (sys.argv[1], "r") as myfile:
    template=myfile.read()
    
with codecs.open (sys.argv[2], "r", "UTF-8") as myfile:
    content=myfile.read()

markdown = markdown.markdown(content)
processed = template.replace('%%content%%', markdown);

with codecs.open (sys.argv[3], "w", 'UTF-8') as myfile:
    myfile.write(processed)

