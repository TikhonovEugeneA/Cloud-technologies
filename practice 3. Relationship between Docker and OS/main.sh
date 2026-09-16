echo "-------------------"
socat TCP4-LISTEN:8080,reuseaddr,fork SYSTEM:'sh handler.sh'