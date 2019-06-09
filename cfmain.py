## CFBypass Beta v1.MAIN
# Coded on 6/9/2019
# Inspired by CloudSearch.cf
# Author = SmallDoink
# Date = 6/9/2019
# Version = v1.MAIN
# Imports
import os
import socket

# END Imports
print """
    __  _____  ____   __ __  ____   ____  _____ _____
   /  ]|     ||    \ |  |  ||    \ /    |/ ___// ___/
  /  / |   __||  o  )|  |  ||  o  )  o  (   \_(   \_
 /  /  |  |_  |     ||  ~  ||   _/|     |\__  |\__  |
/   \_ |   _] |  O  ||___, ||  |  |  _  |/  \ |/  \ |
\     ||  |   |     ||     ||  |  |  |  |\    |\    |
 \____||__|   |_____||____/ |__|  |__|__| \___| \___|

    CFBypass - CloudFlare Bypass - Version v1.MAIN
                Author - SmallDoink#1102
"""
i = raw_input("Website Name> ")
v = raw_input("Verbosity> ")
if v == 1:
    websitename = "i"
    ip = socket.gethostbyaddr('ssh.'+i)
    print "IP Behind Cloudflare - "+ip
    os.quit()
    # END OF VERBOSITY 1
elif v == 0:
    websitename = "i"
    ip = socket.gethostbyaddr('ssh.'+i)
    print "IP Behind Cloudflare - "+ip
    os.quit()
    # END OF VERBOSITY 0
else:
    websitename = "i"
    ip = socket.gethostbyname('ssh.'+i)
    print "Hostname and IP behind Cloudflare - "+ip
    os.quit()
    # END OF VERBOSITY 2

