## CFBypass DNS Method v2.BETA 
# Coded 6/10/19
# Inspired by CloudSearch.cf
# Author = SmallDoink
# Date = 6/10/19
# Version = v2.BETA 
# Updated: Added DNS Method 
# Imports 
import os
import socket 
import dns.resolver
# End Imports 
# Start Setup
os.system('clear')
cfdns = dns.resolver.Resolver()
os.system('clear')
print """
    __  _____  ____   __ __  ____   ____  _____ _____
   /  ]|     ||    \ |  |  ||    \ /    |/ ___// ___/
  /  / |   __||  o  )|  |  ||  o  )  o  (   \_(   \_
 /  /  |  |_  |     ||  ~  ||   _/|     |\__  |\__  |
/   \_ |   _] |  O  ||___, ||  |  |  _  |/  \ |/  \ |
\     ||  |   |     ||     ||  |  |  |  |\    |\    |
 \____||__|   |_____||____/ |__|  |__|__| \___| \___|

    CFBypass - CloudFlare Bypass - Version v2.MAIN
                Author - SmallDoink#1102
                      Methods:
                    DNS      SSH 
"""
site = raw_input("Wesbite> ")
meth = raw_input("Method> ")
if meth == "dns":
    bpip = cfdns.query(site, "A")
    for rdata in bpip:
        print "IP Behind CloudFlare" + rdata
else:
    site = i 
    ip = socket.gethostbyname('ssh.'+i)
    print c.pink + "IP Behind Cloudflare - "+ip
