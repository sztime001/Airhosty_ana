# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:01:51 2018

@author: Sofei
"""

import requests
import sys


URL = 'https://www.airgms.com/app/chat.html?v=61025#1059399'

#def main():
    # Start a session so we can have persistant cookies
session = requests.session()
    
     # This is the form data that the page sends when logging in
#    login_data = {
#        'login-email': 'airlineproperty@gmail.com',
#        'login-password': 'allenapril!',
#        'login-inputs': 'submit',
#    }

    # Authenticate
#    r = session.post(URL, data=login_data)

    # Try accessing a page that requires you to be logged in
r = session.get(URL)

#if __name__ == '__main__':
#    main()