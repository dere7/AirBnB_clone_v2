#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive"""
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    fpath = 'versions/web_static_{}.tgz'.format(now)
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static'.format(fpath))
    if (result.succeeded):
        return fpath
