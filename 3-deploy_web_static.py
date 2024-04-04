#!/usr/bin/python3
"""
   Fabric script that generates a .tgz archive from the contents
   of the web_static folder of your AirBnB Clone repo,
   using the function do_pack.
"""
from os.path import isdir, isfile
from fabric.api import local, put, env, local, run
from datetime import datetime

env.hosts = ['54.227.197.97', '54.237.28.128']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
    """function to archive the content of the web_static dir"""

    dt = datetime.utcnow()
    file = "versions/web_static{}{}{}{}{}{}.tgz".format(dt.year,
                                                        dt.month,
                                                        dt.day,
                                                        dt.hour,
                                                        dt.minute,
                                                        dt.second)

    if not isdir('versions'):
        if local('mkdir -p versions').failed:
            return None
    if local('tar -cvzf {} web_static'.format(file)).failed:
        return None
    return file


def do_deploy(archive_path):
    """function that distribute an archive to my web servers
    Args:
        archive_path (string): path of the archive to be deployed
    Returns:
        False if the file isn't exist or failure, otherwise True
    """

    if not isfile(archive_path):
        return False

    file = archive_path.split('/')[-1]
    filename = file.split('.')[0]

    if put(archive_path, '/tmp/{}'.format(file)).failed:
        return False

    if run('mkdir -p /data/web_static/releases/{}/'.format(filename)).failed:
        return False

    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file, filename)).failed:
        return False

    if run('rm /tmp/{}'.format(file)).failed:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(filename, filename)).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".format(filename)).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(filename)).failed:
        return False

    return True


def deploy():
    """function to deploy the content."""
    return do_deploy(do_pack())
