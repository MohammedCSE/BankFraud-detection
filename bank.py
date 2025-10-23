import smtplib
import random
from collections import Counter
num = 100
transactions = []
for i in range(num):
    card_id = "hsbc001"
    amount = random.randint(1, 5000)
    country = random.choices(["uk", "us"], weights=[0.98, 0.02])[0]  
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    random_time = f"{hour:02d}:{minute:02d}:{second:02d}"
    slip = {
        "transaction_id": f"tx_{i+1}",
        "time": random_time,
        "card_id": card_id,
        "amount": amount,
        "country": country

    }
    transactions.append(slip)
amounts = [t["amount"] for t in transactions]
countries = [t["country"] for t in transactions]
times = [t["time"] for t in transactions]
mean_amount = (sum(amounts)/len(amounts))*1.9
common_country = Counter(countries).most_common(1)[0][0]
timeee=random.choice(times)
for t in transactions:
    reasons = []

    if t["amount"] > mean_amount :
        reasons.append("Unusually high transaction amount")

    if t["country"] != common_country:
        reasons.append("Transaction from unusual country")


    if reasons:
        print("\nALERT DETECTED!")
        print(f"card id: {'card_id'}")
        print(f"Transaction ID: {t['transaction_id']}")
        print(f"Amount: £{t['amount']}")
        print(f"Country: {t['country']}")
        print(f"time: {t["time"]}")
        print("Reasons:", ", ".join(reasons))
        continue



print("send an email to receiver to alert him")
sender_email = "studentsguide359@gmail.com"
receiver_email =input("Enter the receiver email: ")
password ="aeeb mpsk ehsx urki"
subject="Suspected Fraud transactions "
message="Suspected Fraud transactions ,Please Freeeze your card on the HSBC bank else ignore it "
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
text = f"{subject},{message}"
server.sendmail(sender_email,receiver_email,text)
print(f"the email has been sent successfully to {receiver_email}" )


