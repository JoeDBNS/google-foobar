# While Foobar site was under maintenance in early 2019 I ran this checker to alert me once it was back up.

import urllib.request, time

# string to find if site is down for maintenance
find_if_down = 'foobar is currently down for extended maintenance'
page_request = find_if_down

# while the site is found to be down, read content of site request and check whether find_if_down is found.
while find_if_down in page_request:
    x = urllib.request.urlopen('https://foobar.withgoogle.com')
    page_request = str(x.read())
    print('Down\t:(\t', time.time(), end='\r')

input('Up\t:)\thttps://foobar.withgoogle.com')