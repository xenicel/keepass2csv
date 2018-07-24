#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

try:
	filename = sys.argv[1]
except:
	print ('usage: ' + sys.argv[0] + ' filename')
	sys.exit(1)

outputdict = {}

tree = ET.parse(filename)

# The database level
elem = tree.getroot()
firstgroup = elem.getchildren()[1]

# title, website, username, password, comment

# get individual groups
for i in firstgroup.findall('Group'):
	# level2 = i.find('Title').text
	# Get individual entries
	for j in i.findall('Entry'):
		title = ''
		url = ''
		username = ''
		password = ''
		notes = ''
	
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
		print ('"' + title + '","' + url + '","' + username + '","' + password + '","' + notes.replace('\n', ' ### ') + '"')

