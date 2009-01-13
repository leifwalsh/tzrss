# Create your views here.

from datetime import datetime

from django.shortcuts import render_to_response

from tzrss import tzutils

def index(request):
  hr_tz_list = tzutils.human_readable_tz_list()
  # django is fucking stupid
  now = tzutils.localize_dt(datetime.now(), 'UTC').astimezone(tzutils.local_tz)
  default_dict = {'dt_now': now,
                  'local_tz_name': tzutils.LOCAL_TZ_NAME,
                  'hours': range(24),
                  'hr_tz_list': hr_tz_list}

  if request.method == 'POST':
    hour = int(request.POST['hour'])
    tz_name = request.POST['tz_name']

    dt_obj = tzutils.localize_dt(datetime.today().replace(hour=hour), tz_name)
    morning_tz_list = list(tzutils.get_timezones_for_hour(dt_obj, 8))

    default_dict.update({'dt_now': dt_obj,
                         'local_tz_name': tz_name,
                         'morning_tz_list': morning_tz_list})
    return render_to_response('index.html', default_dict)
  else:
    return render_to_response('index.html', default_dict)