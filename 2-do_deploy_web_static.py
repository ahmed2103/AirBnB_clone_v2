#!/usr/bin/python3
"""
    Fabric script that distributes an archive to my web servers
"""


def do_deploy(archive_path):
    """function that distribute an archive to my web servers
    Args:
        archive_path (string): path of the archive to be deployed
    Returns:
        False if the file isn't exist or failure, otherwise True
    """

    from os.path import isfile
    from fabric.api import env, run, put


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
