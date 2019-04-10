


import requests
import os
import string
import json
from bs4 import BeautifulSoup

url = 'https://www.ntnu.no/sok?p_p_id=ntnusearcheksternwebresultportlet_WAR_ntnusearchportlet_INSTANCE_9Y1EmaWDtjCa&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=regular-search-json&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1'

chars = string.ascii_letters
reduced_chars = chars[0:26]


finaldic = []

for c in reduced_chars:
	query = c

	for i in range(20):
		data = requests.get(url, allow_redirects=False, params={
			'query': c,
			'category': 'employees',
			'pageNo': i,
			'sortby': 'alpha'
			})

		print ('Reguesting names starting with letter %s and page %i ' % (c,i))
		
		soup = BeautifulSoup(data.text, 'html.parser')
		newdic = json.loads(str(soup.text))
		#print(newdic)
		employe = (newdic['searchResults'])
		for item in employe:
			print('-------------------------------------')
			print (item['firstName'], item['lastName'], item['cellPhone'])
			print('Username is %s', item['username'])

