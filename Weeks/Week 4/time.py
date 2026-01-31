import time

def send_emails():
    for i in range(50):
        pass
        print(f"Sending email {i + 1}")
        time.sleep(1)  # Simulate time taken to send an email

start = time.time()
send_emails()
end = time.time()
duration = end - start
print(f"Time taken to send emails: {duration} seconds")
