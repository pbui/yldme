#!/bin/sh

if [ -z "$1" ]; then
    URL=$(curl -s -X POST --data-binary @- https://yld.me/paste?raw=1)
else
    URL=$(curl -s -X POST --data-binary @- https://yld.me/paste?raw=1 < "$1")
fi

if [ -z "$URL" ]; then
    exit 1
fi

if [ -n "$WAYLAND_DISPLAY" ]; then
    printf $URL | wl-copy
else
    printf $URL | xclip
fi

if command -v notify-send > /dev/null; then
    notify-send --icon="cloud-upload" "Yld.Me Paste" "$URL"
fi
echo $URL
