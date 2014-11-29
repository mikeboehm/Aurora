

Add the following to /etc/rc.local before 'exit 0'
```
rabbitmqctl start_app
python /home/pi/code/aurora-web/server.py &
python /home/pi/code/Aurora/aurora_exec.py &
```

```
sudo pip install requests
sudo gem install lifx-http
```

Add to your .bashrc file
```
export RACK_ENV=production
```