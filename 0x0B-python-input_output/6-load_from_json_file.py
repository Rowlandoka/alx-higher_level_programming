#!/usr/bin/bash/python3
"""loads object from a json file"""

import json


def load_from_json_file(filename):
    """ load json"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return(json.load(f))
