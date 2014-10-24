#!/usr/bin/python
from __future__ import print_function
import sys
try:
    import simplejson as json
except ImportError: 
    import json

#output file from ec2.py
EC2_DATA_FILE = "data.json"
OP_FILE = "ec2_hosts"
INV = {}

def main():
    """ Reads from EC2_DATA_FILE and writes to OP_FILE """
    try:
        with open(EC2_DATA_FILE) as fd:
            data = json.loads(fd.read())
    except IOError as e:
        print(e)
        sys.exit(1)

    #Read the hosts info.
    hosts = data["_meta"]["hostvars"]

    #Dump the info. into INV dict
    for k,v in hosts.iteritems():
        INV[v["ec2_tag_Env"]] = INV.get(v["ec2_tag_Env"],[])+[k]
  
    with open(OP_FILE,"w+") as op: 
        for env, ip_list in INV.iteritems():
            op.write('[{0}]\n{1}\n\n'.format(env, "\n".join(ip_list)))

if __name__ == "__main__":
    main()
