Skip to content

SHOOTER-MAKER

/

JuttBadshah

Public

Code

Issues

Pull requests

Actions

Projects

Wiki

Security

Insights

Create Juttbrand.py

 main

@SHOOTER-MAKER

SHOOTER-MAKER committed 5 days ago

1 parent e297fa5 commit 86f139f90e36fd360d57e308dabd911eab6d5086

Showing  with 33 additions and 0 deletions.

 33  

Juttbrand.py

@@ -0,0 +1,33 @@

#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

if not os.path.isfile('Jutt.so'):

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/Jutt.cpython-310.so > Jutt.so')

    os.system('clear')

if not os.path.isfile('brand.so'):

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/brand.cpython-310.so > brand.so')

    os.system('clear')

bit=platform.architecture()[0]

go = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/JuttBadshah/main/update.txt').text

if 'Juttbrand' in go:

    if bit == '64bit':

        from Jutt import reg

        reg()

    elif bit == '32bit':

        from brand import reg

        reg()

else:

    os.system('rm -rf Jutt.so brand.so')

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/Jutt.cpython-310.so > Jutt.so')

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/brand.cpython-310.so > brand.so')

    if bit == '64bit':

        from Jutt import reg

        reg()

    elif bit == '32bit':

        from brand import reg

        reg()

0 comments on commit 86f139f

Leave a comment

 You’re not receiving notifications from this thread.

© 2022 GitHub, Inc.

Terms

Privacy

Security

Status

Docs

Contact GitHub

Pricing

API

Training

Blog

About

