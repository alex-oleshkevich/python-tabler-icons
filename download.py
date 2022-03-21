#!/usr/bin/env python
import glob
import json
import os
import pathlib
import urllib.request
import zipfile

this_dir = pathlib.Path(__file__).parent
workdir = this_dir / '_workdir'

sock = urllib.request.urlopen('https://api.github.com/repos/tabler/tabler-icons/releases')
releases = json.loads(sock.read())
latest_release = [release for release in releases if release['draft'] is False and release['prerelease'] is False][0]
version = latest_release['tag_name'].lstrip('v')
zipball = latest_release['zipball_url']

# dowload archive
os.makedirs(workdir, exist_ok=True)
urllib.request.urlretrieve(zipball, workdir / 'sources.zip')
with zipfile.ZipFile(workdir / 'sources.zip') as zip_ref:
    zip_ref.extractall(workdir)

files = glob.glob(os.path.join(workdir, 'tabler-*', 'icons', '*.svg'))
with zipfile.ZipFile(this_dir / 'tabler_icons' / 'archive.zip', 'w') as out_ref:
    for file in files:
        out_ref.write(file, os.path.basename(file), zipfile.ZIP_DEFLATED, compresslevel=9)
