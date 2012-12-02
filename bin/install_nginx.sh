#!/bin/bash

cd /repository/deps/nginx/

export NGINX_PARAMS=$(cat ../conf/nginx_conf_args | xargs)
export LUAJIT_LIB= /usr/local/lib/lua/5.1/
export LUAJIT_INC=/usr/local/include/luajit-2.0

./configure $NGINX_PARAMS
make -j2
make install
