import requests

from navistar_socialnetwork.celery import celery_app


@celery_app.task(name="send_sms",
                 bind=True,
                 default_retry_delay=5,
                 max_retries=1,
                 acks_late=True)
def send_sms(self, phone, otp):
    phone_num = str(phone)
    url = 'here is the path to the provider API' + phone_num + ' and ' + otp
    # requests.get(url) # here is requests library method to send otp to user's phone
    print('= SENT SMS =', phone, otp, '===')  # this print to show otp in terminal
