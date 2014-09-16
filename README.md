#YoAfter
=======

YoApp Service for 1hr/30min/15min reminders. Visit http://yoafter.appspot.com.

###Update 2: 9/15/2014
* Refactored Code
* includes two new Yo accounts, YOPOMODORO and YOPOMODORORESTART (http://pomodorotechnique.com/)
* Now forwards the link paramater.


## What is it?

Ever wanted a short reminder? With YoAfter you can remind yourself with a Yo with 3 reminders.


| Yo Username | Description          |
| ------------- | ----------- |
| YOAFTERANHOUR | Yo's you after an hour.|
| YOAFTER30MIN | Yo's you after 30 minutes. |
| YOAFTER15MIN  | Yo's you after 15 minutes. |


## Uses

* remember to take out the laundry once it's finished?
* as a kitchen timer?
* ...the possibilities are endless.

## How to use it?

Just send a Yo to any one of the accounts, Yoafter will reply back after the respective time interval.

## Tip

Make a shortcut on your homescreen (Android phones only!) for all these accounts for quick access to these reminders.


###Note:

* I've not included apikeys.py to prevent abuse of the system. The callbacks are also secret.
* The Yo Api is restricted to one yo per recipient per minute. You can't receive two 15 min reminders in the same minute.

