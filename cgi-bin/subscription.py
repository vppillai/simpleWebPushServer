#!/usr/bin/python

import sys, json
from pywebpush import webpush

publicVapidKey = 'BJsj8xtpUqT2WfcFSYvabvf7F-sdMRuzi4jSvFJkzBWwD9r3OdF8yDaxo6wY-9k4t9_cSdlUtbBTZKPaFqsVlkw'
privateVapidKey = 'rHzgZzYeDMSUMqXyxwX9v-GZf1zyxGlLacqUj2Z6GDc'

sub_info = json.load(sys.stdin)
with open('sub.info', 'w') as outfile:
    json.dump(sub_info, outfile)

print ('Status: 200\r\n\r\n')

webpush(sub_info,
        json.dumps({"title":"test notification title","body":"test notification body"}),
        privateVapidKey,
        vapid_claims={"sub": "mailto:vysakhpillai@gmail.com"})