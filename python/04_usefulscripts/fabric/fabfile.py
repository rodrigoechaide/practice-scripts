import datetime
from os import path, environ

from fabric.api import env, cd, task, local, settings
from fabric.operations import run, sudo, put, open_shell, get
from fabric.context_managers import (
    cd,
    lcd,
    remote_tunnel,
    shell_env,
    )
from fabric.contrib.files import append, exists
from fabric.colors import green, yellow, red
from fabric.utils import abort
from fabtools import service, require, files
#from asc_fabric.docker import (
#    push_local_registry,
#    start_local_registry,
#    stop_local_registry,
#    create_local_registry,
#    destroy_local_registry,
#    show_images
#    )

import asc_fabric.docker


@task
def create_local_registry():
    asc_fabric.docker.create_local_registry()

@task
def start_local_registry():
    asc_fabric.docker.start_local_registry()

@task
def stop_local_registry():
    asc_fabric.docker.stop_local_registry()

@task
def destroy_local_registry():
    asc_fabric.docker.destroy_local_registry()