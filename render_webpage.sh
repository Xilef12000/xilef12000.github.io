#!/bin/sh
# run: "sh render_webpage.sh"
# run: "sh render_webpage.sh -f" for fast render

fast=false
web_server=true

echo_help() {
  echo "HELP:"
  echo "use -f for fast render mode"
  echo "use -n if you dont wnat to start the test server to see results"
}

while getopts 'fnh?' flag; do
  case "${flag}" in
    f) fast=true ;;
    n) web_server=false ;;
    *) echo_help
       exit 1 ;;
  esac
done

echo "\e[1;35m Preparing dir ... \e[0m"
rm -r -f $(pwd)/docs/
mkdir -p $(pwd)/docs/
cp $(pwd)/CNAME $(pwd)/docs/CNAME
echo "\e[1;35m Starting node Server ... \e[0m"
fuser -k 3000/tcp
node . > log_node.log &
cp $(pwd)/CNAME $(pwd)/docs/CNAME
echo "\e[1;35m Starting static render ... \e[0m"
if $fast ; then
    echo "\e[1;32m Using fast mode \e[0m"
    /bin/python3 $(pwd)/save-webpage.py -c render-conf.json -f > log_save-webpage.log
else
    echo "\e[1;32m This might take a while, ingore the errors ... \e[0m"
    /bin/python3 $(pwd)/save-webpage.py -c render-conf.json > log_save-webpage.log
fi
echo "\e[1;35m cleaning up ... \e[0m"
fuser -k 3000/tcp
if $web_server ; then
    echo "\e[1;35m Starting HTTP.Server on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ... \e[0m"
    /bin/python3 $(pwd)/webserver.py > log_webserver.log
fi