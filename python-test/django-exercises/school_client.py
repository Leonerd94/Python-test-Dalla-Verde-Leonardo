import requests
import sys
import json
import argparse

# Dalla Verde Leonardo

HOST = 'localhost:8000'

def enroll_stud(fname, lname):
    resp = requests.post(
        'http://{}/home'.format(HOST),
        json.dumps({'fname':fname, 'lname':lname}))

    if resp.status_code == 200:
        print 'OK'
    else: 
        print 'Errore'

def search_stud(student):
    resp = requests.get(
        'http://{}/home'.format(HOST))
    content = json.loads(resp.content)
    for stud in content:
        if(stud['fname'] == student or stud['lname'] == student):
            print stud['fname'] + ' ' + stud['lname'] + ' enrolled on ' + stud['dt'] + '\n'




parser = argparse.ArgumentParser('school client')
parser.add_argument('command')
parser.add_argument('--fname')
parser.add_argument('--lname')
parser.add_argument('--student')
args = parser.parse_args()

if args.command == 'enroll':
    enroll_stud(args.fname, args.lname)
elif args.command == 'search':
    search_stud(args.student)
else:
    print 'Errore'

HOTS = 'localhost:8000'

