import requests
import datetime
import random

url = 'http://localhost:8000/analytics/salesperformance/'

entities = [3, 4, 5]
channels = [1, 2, 3, 4]
products = [1 , 2, 3, 4, 5, 6]
lookback_days = 60

def make_sales():
    
    for e in entities:

        # base size of the entity
        contracts = random.random() * 200
        volume = contracts * 250.

        # any number between -.5 and .5
        k = random.random() - 0.5 

        for delta in range(lookback_days):

            day = datetime.date.today() - datetime.timedelta(delta)

            correction = delta / lookback_days * k 

            contracts2 = contracts * (1 + correction)
            volume2 = volume * (1 + correction)

            if day.isoweekday() in [6,7]:
                contracts2 = contracts * .15
                volume2 = volume * .15

            for c in channels:
                
                # consistently split across channels
                contracts3 = contracts2 / c
                volume3 = volume2 / c

                for p in products:

                    # split across products
                    # add some jitter
                    contracts4 = contracts3 / p * (1 + random.random()**2)
                    volume4 = volume3 / p * (1 + random.random()**2)

                    request(day, e, c, p, volume4, int(contracts4))

def request(day, e, c, p, volume, contracts):
    print(day, e, c, p, volume, contracts)

    payload = {
        "date": day,
        "contracts": contracts,
        "volume": volume,
        "entity": e,
        "channel": c,
        "product": p,
    }

    requests.post(
        url,
        data = payload
    )


if __name__ == '__main__':
    make_sales()