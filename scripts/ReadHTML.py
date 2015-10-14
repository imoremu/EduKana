'''
Created on 14/10/2015

@author: Vivelo
'''

from requests import session

user = "admin"
password = "admin"

payload = {'name': user, 'pass': password, 'form_id': 'user_login'}

with session() as c:
    
    r = c.post('http://test.local.vivelogratis.com/?q=user', data=payload)
    
    response = c.get('http://test.local.vivelogratis.com/')

    print(response.text)

