#!/usr/bin/python3

"""File to instance a FileStorage and call reload method"""

from models import base_model
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
