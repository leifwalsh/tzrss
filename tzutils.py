#!/usr/bin/python

from datetime import datetime
import pytz

from tzrss import settings

# Configuration variables:
LOCAL_TZ_NAME = settings.TIME_ZONE

local_tz = pytz.timezone(LOCAL_TZ_NAME)

_TIMEZONE_LIST = None

def tz_list():
  """Get a list of available timezone objects.  Caches the list after
  constructing the list in memory.
     
  Return:
    A list of timezone objects.
  """

  global _TIMEZONE_LIST

  if _TIMEZONE_LIST is None:
    _TIMEZONE_LIST = _get_timezone_list()
  return _TIMEZONE_LIST

def _get_timezone_list():
  """Private helper for tz_list()."""

  _tz_list = []
  for tz_name in pytz.common_timezones:
    try:
      tz = pytz.timezone(tz_name)
    except IOError, e:
      # timezone not available, just skip it
      pass
    else:
      _tz_list.append(tz)
  return _tz_list

_HR_TZ_LIST = None

def human_readable_tz_list():
  """List of the human-readable names of timezones."""

  global _HR_TZ_LIST

  if _HR_TZ_LIST is None:
    _HR_TZ_LIST = _get_human_readable_tz_list()

  return _HR_TZ_LIST

def _get_human_readable_tz_list():
  """Private helper for human_readable_tz_list."""

  return [tz.zone for tz in tz_list()]

def localize_dt(dt_obj, tz_name):
  """Localizes a datetime object to the given tz_name.

  Note: There are like a million ways to break this.  Make sure you don't pass
  something stupid.

  Args:
    dt_obj :: datetime.datetime
    tz_name :: str

  Returns:
    datetime.datetime (I think)
  """

  return pytz.timezone(tz_name).localize(dt_obj)

def convert_dt(dt_obj, tz_name):
  """Converts a localized datetime object to a new location.

  Note: You can break this one too.

  Args:
    dt_obj :: datetime.datetime
    tz_name :: str

  Returns:
    datetime.datetime
  """

  return dt_obj.astimezone(pytz.timezone(tz_name))

def get_timezones_for_hour(dt_obj, hour):
  """Takes a localized datetime object and finds the timezones in which the
  same global time had that hour (that is, dt_obj, converted to any of the
  timezones generated, will be between hour:00:00 and hour:59:59 for some day.

  Note:  This might have corner cases that fail silently.  Sometime in the
  future we may decide to study timekeeping theory and fix them, but it's good
  enough for now.

  Example:
    >>> eastern = pytz.timezone('US/Eastern')
    >>> pacific = pytz.timezone('US/Pacific')
    >>> now = datetime.datetime(2009, 1, 12, 17, 0, 0)
    >>> est_dt = eastern.localize(now)
    >>> pacific in [get_timezones_for_hour(est_dt, 2)]
    True

  Yields:
    Timezone objects.
  """

  for tz in tz_list():
    if dt_obj.astimezone(tz).hour == hour:
      yield tz
