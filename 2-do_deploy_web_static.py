#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import env, put, run
from os.path import exists

<<<<<<< HEAD
env.hosts = ["54.209.26.141", "18.215.182.32"]
env.user = "ubuntu"
env.key = "~/.ssh/id_rsa"
=======
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['54.164.125.6', '3.95.216.87']
>>>>>>> e53ddc400784148de62dde8d5ef114793def52d4


def do_deploy(archive_path):
    """Function to distribute an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        path_name = "/data/web_static/releases/" + name
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(path_name))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, path_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(path_name, path_name))
        run("rm -rf {}/web_static".format(path_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(path_name))
        return True
    except Exception:
        return False

# Run the script like this:
# $ fab -f 2-do_deploy_web_static.py
# do_deploy:archive_path=versions/file_name.tgz