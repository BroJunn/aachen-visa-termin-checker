from utils import Checker
import time
import boto3
from datetime import datetime
from config import *
root_url = "https://termine.staedteregion-aachen.de/auslaenderamt/"



if __name__ == "__main__":
    

    client = boto3.client(
        "sns",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=REGION_NAME
    )


    while True:
        checker = Checker()
        res = []

        checker.init_url_root(root_url)
        checker.click_to_verlaengen(idx_group=1)
        no_appointment = checker.check_if_no_appointment()
        res.append(no_appointment)

        checker.init_url_root(root_url)
        checker.click_to_verlaengen(idx_group=2)
        no_appointment = checker.check_if_no_appointment()
        res.append(no_appointment)

        checker.init_url_root(root_url)
        checker.click_to_verlaengen(idx_group=3)
        no_appointment = checker.check_if_no_appointment()
        res.append(no_appointment)

        now = datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        with open('./log.txt', 'a') as log:
            log.write(f'{time_string}: {"kein Termin" if res[0] else "Termin"} | {"kein Termin" if res[1] else "Termin"} | {"kein Termin" if res[2] else "Termin"}\n')
        if not res[0] or not res[1] or not res[2]:
            lis_nums = []
            for i, ele in enumerate(res):
                if not ele:
                    lis_nums.append(i)
            
            response = client.publish(
                PhoneNumber=PHONE_NUMBER,
                Message=f"{time_string}: Es gibt Termin in der Gruppe {lis_nums}!!!"
            )
        
        time.sleep(CHECK_INTERVAL)