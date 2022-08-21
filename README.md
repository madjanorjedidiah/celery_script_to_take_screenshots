## celery_script_to_take_screenshots

This is a script to schedule screenshots and send email of taken screenshots.


## Purpose

Exploring celery and pygui.


## Prerequisites

- Install celery
- Install Rabbitmq
- Install pygui


## Run
- Edit the screen_capture.py by inputing the emails (sender, receiver), text, subject.
- You can also set a wait time (sleep) for the job. It defaultly waits for 2 seconds.
- Set the start time and end time for the script.
- Finally, paste this in the shell "celery -A tasks worker --loglevel=INFO"


Now your script should be running.

