#!/usr/bin/env python3

import os
import os.path
import subprocess
import sys
import time
import hashlib

if os.path.exists('node_modules'):
    print("Remove node_modules before running")
    sys.exit(2)

if not os.path.exists('input-planet.osm.pbf'):
    print("Place planet file to be processed in input-planet.osm.pbf")
    sys.exit(2)

tic = time.time()
args = [
    'docker',
    'run',
    '-it',
    '--rm',
    '-w',
    '/wkd',
    '-v',
    f'{os.getcwd()}:/wkd',
    'stefda/osmium-tool',
    'osmium',
    'tags-filter',
    'input-planet.osm.pbf',
    '-R',
    'name,brand,operator,network',
    '--overwrite',
    '-o',
    'filtered.osm.pbf',
]
print(f'Running docker command: {" ".join(args)}')
subprocess.run(args, check=True)
toc = time.time()
print(f'Took {toc-tic}s')

tic = time.time()
args = [
    'docker',
    'run',
    '-it',
    '--rm',
    '-w',
    '/wkd',
    '-v',
    f'{os.getcwd()}:/wkd',
    'node:10',
    'bash',
    '-c',
    'npm install && node collect_osm.js filtered.osm.pbf',
]
print(f'Running docker command: {" ".join(args)}')
subprocess.run(args, check=True)
toc = time.time()
print(f'Took {toc-tic}s')

print(f'Calculating hash of input-planet.osm.pbf')
tic = time.time()
 
md5_hash = hashlib.md5()
with open("input-planet.osm.pbf","rb") as fd:
    # Read and update hash in chunks of 4K
    for byte_block in iter(lambda: fd.read(4096),b""):
        md5_hash.update(byte_block)
hash = md5_hash.hexdigest()
toc = time.time()
print(f'Got: {hash} Took {toc-tic}s')
with open("last_run.md5", "w") as fd:
    fd.write(hash + '\n')