#!/usr/bin/python

import sys, json
from pywebpush import webpush

publicVapidKey = 'BJsj8xtpUqT2WfcFSYvabvf7F-sdMRuzi4jSvFJkzBWwD9r3OdF8yDaxo6wY-9k4t9_cSdlUtbBTZKPaFqsVlkw'
privateVapidKey = 'rHzgZzYeDMSUMqXyxwX9v-GZf1zyxGlLacqUj2Z6GDc'

 
with open('..\sub.info') as f:
  sub_info = json.load(f)

webpush(sub_info,
        json.dumps({"title":"test notification title","body":"test notification body"}),
        privateVapidKey,
        vapid_claims={"sub": "mailto:vysakhpillai@gmail.com"})