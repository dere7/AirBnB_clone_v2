#!/usr/bin/python3
from fabric.api import local, cd, put, env, run, sudo, lcd
from datetime import datetime
from os import path

env.hosts = ['3.239.74.200', '3.238.233.55']


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
    archive_withoutext = path.splitext(path.basename(archive_path))[0]
    if (not path.exists(archive_path)):
        return False
    with cd('/tmp'):
        upload = put(archive_path, archive_withoutext + '.tgz')
    sudo('mkdir -p /data/web_static/releases/{}'.format(archive_withoutext))
    sudo('tar -xzf /tmp/{0}.tgz -C /data/web_static/releases/{0}/'.format(
         archive_withoutext))
    sudo('rm /tmp/{}.tgz'.format(archive_withoutext))
    sudo('mv /data/web_static/releases/{0}/web_static/* \
    /data/web_static/releases/{0}/'.format(archive_withoutext))
    sudo('rm -rf /data/web_static/releases/{}/web_static'.format(
        archive_withoutext))
    sudo('rm -rf /data/web_static/current')
    sudo('ln -s /data/web_static/releases/{} /data/web_static/current'.format(
        archive_withoutext))
    return upload.succeeded


def deploy():
    """created and destributes an archive to web server"""
    fpath = do_pack()
    if fpath is None:
        return False
    return do_deploy(fpath)


def do_clean(number=0):
    """deletes out-of-date archives"""
    with lcd('versions'):
        local('pwd')
        if number == 0:
            number = 1
        local("ls -tp | grep -v '/$' | tail -n +{}".format(number + 1) + " | xargs -I \{} rm -- \{}")
