
import smtplib
import logging

# Enable debug output
logging.basicConfig(level=logging.DEBUG)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.set_debuglevel(1)  # Enable debug output for more detailed logs
    server.login('inuenike@gmail.com', 'ooxy amwg zmky txgt')
    print('SMTP connection successful')
    server.quit()
except Exception as e:
    print(f'Error: {e}')
