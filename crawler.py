# /usr/bin/env python
import requests
import os
import argparse
import subprocess
def arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("-u","--url",dest="url",help="Urls to request")
    options=parser.parse_args()
    if not options.url:
        parser.error("Please specify the url")
    return(options)


def make_request(url):



         with open("wordlist.txt" , "r") as wordlist_file:
             for line in wordlist_file:
                  line_c=line.strip()

                  try:
                      session = requests.Session()
                      session.trust_env = False
                      os.environ['NO_PROXY'] = url
                      get_response = session.get("http://" + line_c + "." + url)
                      if get_response:
                           print("[+] Possible subdomain:" + "http://" + line_c + "." + url)
                           print(get_response.status_code)
                  except:
                      pass




options=arguments()
make_request(options.url)
