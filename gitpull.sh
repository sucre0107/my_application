#!/usr/bin/env bash

echo -e "\033[34m--------------------拉取源码--------------------\033[0m"

git fetch --all

sleep 0.5

git reset --hard origin/main
