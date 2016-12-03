#!/bin/bash
until killall -9 python; python sheriffbot.py; do
    echo "'sheriffbot.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done