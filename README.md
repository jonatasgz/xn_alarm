# XN Alarm

XN Alarm is a first incursion on using XN parameters to try and estimate risk of CLL

## Live version

The latest version of this app can be used at my [server](https://xnalarm.publica-me.com). 

No uploaded data is stored.

## Install instructions

You need to have docker installed and running in order to use this app.

1. Clone the repo:
```
$ git clone https://github.com/jonatasgz/xn_alarm.git
```

2. Go into root folder:
```
$ cd xn_alarm
```

3. Build the app:
```
$ docker build -t xn_alarm .
```

4. Run the app:
```
$ docker run -d --restart unless-stopped -p 7865:7860 xn_alarm
```

The app will bind port 7865 by default.

You can access it at localhost:7865 in your browser.

## How to use

Just input XN parameters on the left column. A conclusion will be drawn on the right column.

## Contributions

No contributions are accepted at the moment. This project is being developed by Haematology specialists.

## License
This software is licensed under GNU General Public License v3.0 - check the LICENSE file for details.


