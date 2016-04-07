#! /usr/bin/env python

import os
import sys
import json
import requests

url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify?version=2015-12-0'
filepath = '/home/tikeda/wtsnData/imgTower.jpg'
filename = os.path.basename(filepath)

res = requests.post(
    url, auth=('de62e230-71af-4c84-a5ea-11b213a16fba', 't0Cf7AcMnZjN'),
    files={
        'imgFile': (filename, open(filepath, 'rb')),
        }
    )

if res.status_code == requests.codes.ok:
    data = json.loads(res.text)
    for img in data['images']:
        print('{} - {}'.format(img['image'], img['image']))
        for label in img['scores']:
            print('    {:30}: {}'.format(label['classifier_id'], label['score']))

else:  # error
    print('stauts_code: {} (reason: {})'.format(res.status_code, res.reason))
    sys.exit(1)