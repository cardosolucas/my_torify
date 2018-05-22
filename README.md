# My Torify

My Torify is a TrayIcon GUI to [toriptables2](https://github.com/ruped24/tor_ip_switcher)

#### Dependencies:
* tor
* wxpython

#### Usage (run as superuser)
```python
tray.py
```
#### To test:
* [What is my IP address](http://whatismyipaddress.com)
* [Check Tor Project](https://check.torproject.org)
* [Witch proxy checker](http://witch.valdikss.org.ru)
* [IP leak test](http://www.doileak.com/)
* [DNS leak test](http://dnsleaktest.com)
* [Test my IPv6](http://testmyipv6.com/)
* [What every Browser knows about you](http://webkay.robinlinus.com/)


#### To manually change IP w/o reload:
##### Refresh Check Tor Project webpage
```bash
sudo kill -HUP $(pidof tor)
```