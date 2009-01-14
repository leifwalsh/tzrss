# Create your views here.

from datetime import datetime

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

from tzrss import tzutils

def index(request):
  hr_tz_list = tzutils.human_readable_tz_list()
  now = tzutils.local_tz.localize(datetime.now())
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

def convert(request):
  if request.method != 'POST':
    raise Http404('use POST')

  hour = int(request.POST['hour'])
  last_tz_name = request.POST['last_tz_name']
  new_tz_name = request.POST['new_tz_name']

  dt_obj = tzutils.localize_dt(datetime.today().replace(hour=hour), last_tz_name)
  new_hour = tzutils.convert_dt(dt_obj, new_tz_name).hour

  return HttpResponse('%s' % new_hour)
