#!/bin/sh
set -e
EMACSCLIENT=/Applications/Emacs.app/Contents/MacOS/bin/emacsclient
exec $EMACSCLIENT -n -a ~/bin/emacsc "$@"
