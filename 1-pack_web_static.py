#!/usr/bin/python3
"""
   Fabric script that generates a .tgz archive from the contents 
   of the web_static folder of your AirBnB Clone repo, 
   using the function do_pack.
"""


def do_pack():
    """function to archive the content of the web_static dir"""
    from os.path import isdir
    from fabric.api import local
    from datetime import datetime

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
