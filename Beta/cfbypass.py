# CFBypass Beta v1.BETA 
# Coded on 6/9/2019
# Inspired by CloudSearch.cf
# Author = SmallDoink
# Date = 6/9/2019
# Version = v1.BETA 
import os 
import socket
print """
    __  _____  ____   __ __  ____   ____  _____ _____
   /  ]|     ||    \ |  |  ||    \ /    |/ ___// ___/
  /  / |   __||  o  )|  |  ||  o  )  o  (   \_(   \_ 
 /  /  |  |_  |     ||  ~  ||   _/|     |\__  |\__  |
/   \_ |   _] |  O  ||___, ||  |  |  _  |/  \ |/  \ |
\     ||  |   |     ||     ||  |  |  |  |\    |\    |
 \____||__|   |_____||____/ |__|  |__|__| \___| \___|

    CFBypass - CloudFlare Bypass - Version v1.BETA
                Author - SmallDoink#1102
""" 
i = raw_input("Website Name> ")
websitename = "i"
ip = socket.gethostbyaddr('ssh.'+i)
print "IP Behind Cloudflare - "+ip 
os.exit()
# END OF SCRIPT 
