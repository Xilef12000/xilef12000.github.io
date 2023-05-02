#!/bin/sh
# run: "sh render_webpage.sh"
# run: "sh render_webpage.sh -f" for fast render

fast=false
web_server=true

echo_help() {
  echo "HELP:"
  echo "use -f for fast render mode"
  echo "use -w to run without running test web server at the end"
  echo "use -n start only the node server in the background"
  echo "use -c to stop the node server running in the background"
}

node_server() {
  cleanup
  echo "\e[1;35mStarting node.js Server in background on 0.0.0.0 port 3000 (http://0.0.0.0:3000/) ... \e[0m"
  node . > log_node.log &
}
cleanup() {
  echo "\e[1;35mcleaning up open ports ... \e[0m"
  fuser -k 3000/tcp
  fuser -k 8000/tcp
}

while getopts 'fwnch?' flag; do
  case "${flag}" in
    f) fast=true ;;
    w) web_server=false ;;
    n) node_server
       exit 0 ;;
    c) cleanup
       exit 0 ;;
    *) echo_help
       exit 1 ;;
  esac
done

echo "\e[1;35mPreparing dir ... \e[0m"
rm -r -f $(pwd)/docs/
mkdir -p $(pwd)/docs/
cp $(pwd)/CNAME $(pwd)/docs/CNAME
node_server
cp $(pwd)/CNAME $(pwd)/docs/CNAME
echo "\e[1;35mStarting static render ... \e[0m"
if $fast ; then
    echo "\e[1;32mUsing fast mode \e[0m"
    /bin/python3 $(pwd)/save-webpage.py -c render-conf.json -f > log_save-webpage.log
else
    echo "\e[1;32mThis might take a while, ingore the errors ... \e[0m"
    /bin/python3 $(pwd)/save-webpage.py -c render-conf.json > log_save-webpage.log
fi
cleanup
if $web_server ; then
    echo "\e[1;35mStarting HTTP.Server on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ... \e[0m"
    /bin/python3 $(pwd)/webserver.py > log_webserver.log
fi