#!/bin/bash
#JSON FILE
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
