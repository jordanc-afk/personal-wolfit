from datetime import timedelta
from datetime import datetime
from app.helpers import less_than_day
from app.helpers import pretty_date
import pytest

def test_just_now_pretty_helper():
	assert(less_than_day(4)) == "just now"


def test_seconds_ago_pretty_helper():
	assert(less_than_day(14)) == "14 seconds ago"


def test_minutes_ago_pretty_helper():
	assert(less_than_day(240)) == "4 minutes ago"


def test_an_hour_ago_pretty_helper():
	assert(less_than_day(7100)) == "an hour ago"


def test_hours_ago_pretty_helper():
	assert(less_than_day(14400)) == "4 hours ago"


def test_days_ago():
	assert(pretty_date(datetime.now() - timedelta(days=4))) == "4 days ago"


def test_weeks_ago():
	assert(pretty_date(datetime.now() - timedelta(weeks=4))) == "4 weeks ago"


def test_months_ago():
	assert(pretty_date(datetime.now() - timedelta(weeks=18))) == "4 months ago"


def test_years_ago():
	assert(pretty_date(datetime.now() - timedelta(weeks=210))) == "4 years ago"
