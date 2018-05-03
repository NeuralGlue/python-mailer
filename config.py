"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

from datetime import datetime

# file settings
LOG_FILENAME = '/tmp/pymailer.log'
CSV_RETRY_FILENAME = '/tmp/pymailer.csv'
STATS_FILE = '/tmp/pymailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# smtp settings
SMTP_HOST = 'mail.example.com'
SMTP_PORT = '587'

# the address and name the email comes from
FROM_NAME = 'Test User'
FROM_EMAIL = 'from@example.com'
AUTH_USER="username"
PASSWORD="password"

# test recipients list
TEST_RECIPIENTS = [
    {'name': 'test', 'email': 'test@example.com'},
]
