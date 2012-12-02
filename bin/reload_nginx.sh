#!/bin/bash
kill -9 $(ps aux | grep nginx | awk '{ print $2 }' | head -n 5 | xargs)
nginx
