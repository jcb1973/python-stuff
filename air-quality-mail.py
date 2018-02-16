import urllib.request
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USER = "anon@anon.com"
GMAIL_PASS = "topsecret"
RECIPIENTS = ["myfriend1@gmail.com", "myfriend2@gmail.com"]
PM25_MAX = 25
API_KEY = 'very-top-secret'

req = urllib.request.Request('https://airapi.airly.eu/v1/mapPoint/measurements?latitude=49.97031&longitude=20.42504')
req.add_header('Accept', 'application/json')
req.add_header('apikey', API_KEY)

response = urllib.request.urlopen(req)
the_page = response.read()
JSON_object = json.loads(the_page.decode('utf-8'))

pm25_level =  (JSON_object["currentMeasurements"]["pm25"])

if pm25_level <= 11:
    level_str = "Low 1"
    color = "#66FF99"
elif 11 <= pm25_level <= 23:
    level_str = "Low 2"
    color = "#00FF00"
elif 23 <= pm25_level <= 35:
    level_str = "Low 3"
    color = "#00cc00"
elif 35 <= pm25_level <= 41:
    level_str = "Moderate 1"
    color = "#FFFF00"
elif 41 <= pm25_level <= 47:
    level_str = "Moderate 2"
    color = "#FFCC00"
elif 47 <= pm25_level <= 53:
    level_str = "Moderate 3"
    color = "#FF9900"
elif 53 <= pm25_level <= 58:
    level_str = "High 1"
    color = "#FF3366"
elif 58 <= pm25_level <= 64:
    level_str = "High 2"
    color = "#FF0000"
elif 64 <= pm25_level <= 70:
    level_str = "High 3"
    color = "#990000"
else:
    level_str = "Very High"
    color = "#CC00FF"

percentage = pm25_level / PM25_MAX * 100
percentage_str = '{0:.1f}'.format(percentage)
body = "Air quality level is currently '" +level_str+ "', which is " + percentage_str + "% of maximum level (PM 2.5)."

me = GMAIL_USER
you = RECIPIENTS

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Air quality currently " + percentage_str + "% of norm"
msg['From'] = me
msg['To'] = ", ".join(you)

# Create the body of the message (a plain-text and an HTML version).
text = body
html = """\
<html>
  <head></head>
  <body>
  <table border=”0″ cellpadding=”0″ cellspacing=”0″ width=”600″>
  <td bgcolor="%s">
    <p>Hi! This is John's automated mail to tell you the current air quality in Bochnia.<br>
       %s<br>
    </p>
    </td>
    </table>
  </body>
</html>
""" % (color, body)

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()
mail.login(GMAIL_USER, GMAIL_PASS)
mail.sendmail(me, you, msg.as_string())
mail.quit()
