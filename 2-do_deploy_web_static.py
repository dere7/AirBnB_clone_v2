#!/usr/bin/python3
from fabric.api import local, cd, put, env, run
from datetime import datetime
from os import path


def do_pack():
    """generates a .tgz archive"""
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    fpath = 'versions/web_static_{}.tgz'.format(now)
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static'.format(fpath))
    if (result.succeeded):
        return fpath


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    env.hosts = ['3.239.74.200', '3.238.233.55']
    if (not path.exists(archive_path)):
        return False
    with cd('/tmp'):
        upload = put(archive_path, archive_path)
    archive_withoutext = path.splitext(path.basename(archive_path))[0]
    run('mkdir -p /data/web_static/releases/{}'.format(archive_withoutext))
    run('tar -xzf /tmp/{0}.tgz -C /data/web_static/releases/{0}/'.format(
         archive_withoutext))
    run('rm /tmp/{}.tgz'.format(archive_withoutext))
    run('mv /data/web_static/releases/{0}/web_static/* /data/web_static/\
        releases/{0}/'.format(archive_withoutext))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(
        archive_withoutext))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        archive_withoutext))
    return upload.succeeded
