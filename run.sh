sleep 5

TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`
echo "$TIMESTAMP - program was run " >> /home/calvinhathcock/Documents/College/UNCC/canvas_to_notion/logs/shell_logs/log.txt

cd ~/Documents/College/UNCC/canvas_to_notion

source .venv/bin/activate

.venv/bin/python3 canvas_to_notion.py

bash
