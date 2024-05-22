import gpsd
import time

while True:
  gpsd.connect()
  time.sleep(0.5)

  try:
    d = gpsd.get_current_as_dict()
    print(d)
  except NoFixError:
    print("No fix. Sleep...")
    continue
