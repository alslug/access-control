#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Display status-lights on mote.',fromfile_prefix_chars='@')
mutually_exclusive = parser.add_mutually_exclusive_group(required=True)
mutually_exclusive.add_argument('--gpio',       help='GPIO pin for relay-pulse. Positive for posive pulse, negative for egative for negative pulse')
parser.add_argument('--heartbeat-url',          help='URL of heartbeat'                                                                 )
parser.add_argument('--heartbeat-timeout',      help='Interval of heartbeat (default 100s)',    default=100                             )
parser.add_argument('--salt',                   help='Salt for calculating key-hash',   default='Dette er det meget hemmelige SALT'     )
parser.add_argument('url',                      help='URL of key-validator',            type=str                                        )
args = parser.parse_args()      #'@/etc/heartbeat-display.conf')

print "============================="
print args
print "============================="

import signal
#print 10
import sys
#print 11
import time
#print 12
import readline
#print 13
import hashlib
#print 14
import requests
#print 15
if args.gpio:
        args.gpio = int(args.gpio)
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(args.gpio, GPIO.OUT)

def heartbeat_handler(signum, frame):
#       print 1111
#       print ('\nOperation timed out.')
#       exit (99)
#       print 2222
        if args.heartbeat_url:
                print "Heartbeat called"
                response = requests.get(args.heartbeat_url)
#       print 3333
        signal.alarm(int(args.heartbeat_timeout))
#       print 4444

def encrypt_string(hash_string):
        sha_signature = hashlib.sha512(hash_string.encode()).hexdigest()
        return sha_signature

status = 0

while status == 0:
        print 20

        signal.signal(signal.SIGALRM, heartbeat_handler)
        heartbeat_handler(0,0)

        print 21
        try:
        #       print 30
                s = ""
        #       print 31
                s = input ()
        #       print 32
        #       print ('You entered', s)
        #       print 33
                salt = 
                hash = encrypt_string(encrypt_string(str(s) + "!" + args.salt) + "!" + str(salt))
        #       print 34
        #       print ("< " + hash)
                print 35
                response = requests.get(args.url + "?hash=" + hash + "&salt=" + salt)
                print 36
                if response.text == "UNLOCK":
                        print "* UNLOCK THE DOOR!!!!!!"
                        if args.gpio:
                                print "* PULL MAGNET"
                                GPIO.output(args.gpio, GPIO.HIGH)
                                time.sleep(1)
                                print "* RELEASE MAGNET"
                                GPIO.output(args.gpio, GPIO.LOW)
                else:
                        print ("> " + str(response))
                        print ("* " + response.text)
        #       print 39
        except KeyboardInterrupt:
                print ('\nKeyboardInterrupt detected.' )
                status = 98
        except SystemExit:
                print ('SystemExit detected.' )
                #status = 97
        except NameError:
                print ('NameError detected.' )
                #status = 96
        except ValueError:
                print ('ValueError detected.' )
                #status = 96
        except SyntaxError:
                print ('SyntaxError detected.' )
                #status = 96
        except:
                print ('\nException detected: ', str(sys.exc_info()[0]) )
                #status = 90

print 16
signal.alarm(0)          # Disable the alarm.
print 17
GPIO.cleanup()
exit (status)
