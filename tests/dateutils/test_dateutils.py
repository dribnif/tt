from unittest import TestCase
from tt.dateutils.dateutils import *
from tt.exceptz.exceptz import TIError
import mock

import pytz

test_timezone = "Europe/Berlin"


class TestDateutils(TestCase):

    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    def test_utc_to_local_cet_winter_time(self, mocked):
        mocked.return_value=pytz.timezone(test_timezone)
        test_time_as_datetime = parse_isotime("2018-02-01T18:00:00.000001Z")
        time_h_m = utc_to_local(test_time_as_datetime).strftime("%H:%M")
        self.assertEqual("19:00", time_h_m)

    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    def test_utc_to_local_cet_summer_time(self, mocked):
        mocked.return_value = pytz.timezone(test_timezone)
        test_time_as_datetime = parse_isotime("2018-06-01T18:00:00.000001Z")
        time_h_m = utc_to_local(test_time_as_datetime).strftime("%H:%M")
        self.assertEqual("20:00", time_h_m)

    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    def test_isotime_utc_to_local_cet_winter_time(self, mocked):
        mocked.return_value = pytz.timezone(test_timezone)
        isotime_local = isotime_utc_to_local("2018-02-01T17:00:00.000001Z")
        self.assertEqual("2018-02-01T18:00:00.000001+01:00", isotime_local.isoformat())

    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    def test_isotime_utc_to_local_cet_summer_time(self, mocked):
        mocked.return_value = pytz.timezone(test_timezone)
        isotime_local = isotime_utc_to_local("2018-06-01T17:00:00.000001Z")
        self.assertEqual("2018-06-01T19:00:00.000001+02:00", isotime_local.isoformat())

    def test_parse_isotime(self):
        now_really = datetime.now()
        isotime_now = now_really.isoformat()+"Z"
        isotime_parsed_from_string = parse_isotime(isotime_now)
        self.assertEqual(isotime_parsed_from_string, now_really)
        
    def test_parse_time_multiformat_colon_separated(self):
        time_parsed = parse_time_multiformat("20:15")
        self.assertEqual(20, time_parsed.hour)
        self.assertEqual(15, time_parsed.minute)

    def test_parse_time_multiformat_not_separated(self):
        time_parsed = parse_time_multiformat("2015")
        self.assertEqual(20, time_parsed.hour)
        self.assertEqual(15, time_parsed.minute)

    @mock.patch('tt.dateutils.dateutils.get_now')
    def test_parse_time_multiformat_with_now_string(self, mocked_datetime_now):
        mocked_datetime_now.return_value = datetime(2019, 3, 16, 20, 15)
        time_parsed = parse_time_multiformat("now")
        self.assertEqual(2019, time_parsed.year)
        self.assertEqual(3, time_parsed.month)
        self.assertEqual(16, time_parsed.day)
        self.assertEqual(20, time_parsed.hour)
        self.assertEqual(15, time_parsed.minute)

    def test_parse_time_multiformat_not_separated(self):
        self.assertRaises(TIError, parse_time_multiformat, "51n3p")

    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    @mock.patch('tt.dateutils.dateutils.get_current_day')
    def test_isotime_utc_to_local_cet_summer_time(self, mocked_current_day, mocked_timezone ):
        mocked_timezone.return_value = pytz.timezone(test_timezone)
        mocked_current_day.return_value = "2018-11-21"
        parsed_time=parse_time_h_m_to_iso("01:15")
        self.date_time_assertion_helper(parsed_time, 2018, 11, 21, 0, 15, 0, 1)
        
        
    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    @mock.patch('tt.dateutils.dateutils.get_current_day')
    def test_isotime_utc_to_local_cet_summer_time(self, mocked_current_day, mocked_timezone ):
        mocked_timezone.return_value = pytz.timezone(test_timezone)
        mocked_current_day.return_value = "2018-06-21"
        parsed_time=parse_time_h_m_to_iso("01:15")
        self.date_time_assertion_helper(parsed_time, 2018, 6, 20, 23, 15, 0, 1)
        
    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    @mock.patch('tt.dateutils.dateutils.get_current_day')
    def test_isotime_utc_to_local_cet_summer_time(self, mocked_current_day, mocked_timezone ):
        mocked_timezone.return_value = pytz.timezone(test_timezone)
        mocked_current_day.return_value = "2018-11-21"
        parsed_time=parse_time_h_m_to_iso("0115")
        self.date_time_assertion_helper(parsed_time, 2018, 11, 21, 0, 15, 0, 1)
        
        
    @mock.patch('tt.dateutils.dateutils.get_local_timezone')
    @mock.patch('tt.dateutils.dateutils.get_current_day')
    def test_isotime_utc_to_local_cet_summer_time(self, mocked_current_day, mocked_timezone ):
        mocked_timezone.return_value = pytz.timezone(test_timezone)
        mocked_current_day.return_value = "2018-06-21"
        parsed_time=parse_time_h_m_to_iso("0115")
        self.date_time_assertion_helper(parsed_time, 2018, 6, 20, 23, 15, 0, 1)
        
    def date_time_assertion_helper(self, parsed_time, year, month, day, hour, minute, second, microsecond):
        self.assertEqual(year,parsed_time.year)
        self.assertEqual(month,parsed_time.month)
        self.assertEqual(day,parsed_time.day)
        self.assertEqual(hour,parsed_time.hour)
        self.assertEqual(minute,parsed_time.minute)
        self.assertEqual(second,parsed_time.second)
        self.assertEqual(microsecond,parsed_time.microsecond)

