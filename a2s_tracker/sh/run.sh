#!/bin/bash
printenv | grep "SERVERADDR" >> /etc/environment
printenv | grep "WEBHOOKURL" >> /etc/environment
printenv | grep "CUSTOMMSG" >> /etc/environment
python3 /py/start.py >> /dev/stdout
/bin/bash