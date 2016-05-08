#!/usr/bin/env python
import os
from app import create_app , db
#from app.models import
from flask.ext.script import Manager,Shell
from flask.ext.migrate, MigrateCommand

if __name__ == '__name__':
    manager.run()