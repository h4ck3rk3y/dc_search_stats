import os
from angular_flask import app

import copy, datetime, sys, time
from pydc_client import pydc_client

import logging


def runserver():
    os.system("sudo twistd -l access.log -n web --port 80 --wsgi  angular_flask.app")

if __name__ == '__main__':

    config_data = { "mode":True, "name":"NWA", "host":"172.17.23.44","nick":"BigTip","pass":"banana","desc":"","email":"","sharesize":53687091200,"localhost":"172.17.14.98"}
    c = pydc_client().configure(config_data).link({"mainchat":sys.stderr.write,"debug":[sys.stdout.write,open("debug.txt","w").write,None][2] }).connect("0/1/0");
    c._config["overwrite"] = True
    time.sleep(3); # Wait for the connection to established and session to be verified. # c.cli();
    c.connect('1')

    runserver()
