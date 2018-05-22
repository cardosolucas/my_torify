# My Torify

Tor Iptables script is an anonymizer that sets up iptables and tor to route all services and traffic including DNS through the Tor network.

#### Dependencies:
tor
wxpython

#### Usage
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