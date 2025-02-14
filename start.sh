if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Kanhaiya960/Safari-Filter-Bot.modified.git /Safari-Filter-Bot.modified
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Safari-Filter-Bot.modified
fi
cd /Safari-Filter-Bot.modified
pip3 install -U -r requirements.txt
echo "Starting Safari-Filter-Bot.modified...."
python3 bot.py
