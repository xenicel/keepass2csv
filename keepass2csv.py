#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

try:
	filename = sys.argv[1]
except:
	print ('usage: ' + sys.argv[0] + ' filename')
	sys.exit(1)

tree = ET.parse(filename)

# The database level
elem = tree.getroot()
firstgroup = elem.getchildren()[1]

# Get group nodes
for i in firstgroup.findall('Group'):
	
	# Get entry nodes
	for j in i.findall('Entry'):
		title = ''
		url = ''
		username = ''
		password = ''
		notes = ''

		# Get string nodes
		for x in j.findall('String'):
			key = x.find('Key')
			if key.text == 'Title':
				title = x.find('Value').text
			if key.text == 'URL':
				url = x.find('Value').text
			if key.text == 'UserName':
				username = x.find('Value').text
			if key.text == 'Password':
				password = x.find('Value').text
			if key.text == 'Notes':
				notes = x.find('Value').text
				
		if not title: title = ''
		if not url: url = ''
		if not username: username = ''	
		if not password: password = ''
		if not notes: notes = ''	

		# Create a CSV file with rows in this format :
		# "title","url","username","password","notes"				
		print ('"' + title + '","' + url + '","' + username + '","' + password + '","' + notes.replace('\n', ' ### ') + '"')

