#!/usr/bin/python3
"""Importing model"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
