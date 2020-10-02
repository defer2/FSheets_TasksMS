#!/bin/zsh
app="tasks"
docker build -t ${app} .
docker run -p 5011:5011 \
  --name=${app} \
  -v $PWD:/app ${app}