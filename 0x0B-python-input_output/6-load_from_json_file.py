#!/usr/bin/python3
"""module doc"""
import json


def load_from_json_file(filename):
    """func doc"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
