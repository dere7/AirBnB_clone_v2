#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """generates a .tgz archive"""
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    fpath = f'versions/web_static_{now}.tgz'
    local('mkdir -p versions/')
    result = local(f'tar -cvzf {fpath} web_static')
    if (result.succeeded):
        return fpath
