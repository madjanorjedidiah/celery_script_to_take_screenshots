import pyautogui
import time
from datetime import datetime
from tasks import send_mail



def current_time():
	now = datetime.now()
	current_time = now.strftime('%H:%M:%S')
	return current_time


def take_screen_shot(func):
	myscreen = pyautogui.screenshot()
	return myscreen.save(f'{func}.png')


def wait_time(sec=None):
	if sec == None:
		sec = 2
	return time.sleep(sec)


start_time = '21:59:00'
end_time = '22:00:00'


while True:
	time_now = current_time()
	if time_now >= start_time:
		take_screen_shot(time_now)
		mail = send_mail.delay('dev1357mail@gmail.com', 'jmadjanor6@gmail.com', 'Trial Celery', 'Cureent Screenshots', time_now, f'{time_now}.png')
		mail.ready()
		mail.get()
		mail.get(propagate=False)
		mail.traceback
		wait_time()
		if end_time <= current_time():
			print('Time to end taking screenshots.')
			break
print('task ended')


