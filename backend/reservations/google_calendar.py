from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from .models import Reservation
from backend.rooms.models import Room
import django.utils.timezone as timezone

SCOPES = ['https://www.googleapis.com/auth/calendar']
class Calendar:
    def __init__(self):
        creds = None
        print("jestem w kalendarzu")
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                path = os.path.dirname(os.path.realpath(__file__))
                flow = InstalledAppFlow.from_client_secrets_file(
                    path + '/credentials.json', SCOPES)
                creds = flow.run_local_server()
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.creds = creds
        self.service = build('calendar', 'v3', credentials=creds)
        self.calendars = ['']
    def addEvent(self, summary, start_date, end_date, description):
        event = {
          'summary': summary,
          'location': 'CZIiT',
          'description': description,
          'start': {
            'dateTime': start_date,
            'timeZone': 'Europe/Warsaw',
          },
          'end': {
            'dateTime': end_date,
            'timeZone': 'Europe/Warsaw',
          },
          'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
          ],
          'attendees': [
          ],
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60},
              {'method': 'popup', 'minutes': 10},
            ],
          },
        }
        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print("===========================================", event)
        print('Event created: %s' % (event.get('htmlLink')))
        return event['id']

    def deleteEvent(self,eventId):
        deleted = self.service.events().delete(calendarId='primary', eventId=eventId).execute()
        print('-------------?', deleted)

    def insertNewCalendar(self, summary):
        print("build new calendar")
        calendar = {
          'summary': summary,
          'timeZone': 'Europe/Warsaw'
        }

        created_calendar = self.service.calendars().insert(body=calendar).execute()
        self.calendars.append(created_calendar)
        calendar_list = self.service.calendarList().list(pageToken=None).execute()
        for calendar_list_entry in calendar_list['items']:
          print(calendar_list_entry['summary'])


def getAvailableTime():
  now = timezone.now()
  week_later = now + datetime.timedelta(days=7)
  availability = dict()
  for room in Room.objects.all():
    available_periods = list()
    start_period = now
    print(room)
    for reservation in Reservation.objects.filter(room=room, start_reservation__gte=now).order_by('start_reservation'):
      print(reservation)
      if reservation.end_reservation > week_later:
        available_periods.append({'start_availability':start_period, 'end_availability': reservation.start_reservation})
        break
      if reservation.start_reservation > week_later:
        available_periods.append({'start_availability':start_period, 'end_availability': week_later})
        break
      available_periods.append({'start_availability':start_period, 'end_availability': reservation.start_reservation})
      start_period = reservation.end_reservation
    availability[room.name] = available_periods

  print(availability)
  return availability

