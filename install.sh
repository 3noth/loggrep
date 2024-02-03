#!/bin/bash

SCRIPT_NAME=$1
PYTHON_SCRIPT_PATH=$(pwd)/src/loggrep.py
WRAPPER_SCRIPT=/usr/local/bin/loggrep

chmod +x "$PYTHON_SCRIPT_PATH"
 
echo "#!/bin/bash" > $WRAPPER_SCRIPT
echo "$PYTHON_SCRIPT_PATH \"\$@\"" >> $WRAPPER_SCRIPT

chmod +x $WRAPPER_SCRIPT

echo "Finish!"




