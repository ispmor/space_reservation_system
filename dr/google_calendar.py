from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

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


