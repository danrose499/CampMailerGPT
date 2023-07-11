import openai
import smtplib
from config import Config

# Generate email content using ChatGPT
def generate_email_content():
    response = openai.ChatCompletion.create(
        model=Config.gpt_model,
        messages=[{"role": "user", "content": Config.gpt_prompt}],
        temperature=Config.gpt_temperature
    )
    email_content = response.choices[0].message["content"]
    return email_content

# Send the email
def send_email(content):
    with smtplib.SMTP(Config.smtp_server, Config.smtp_port) as server:
        server.starttls()
        server.login(Config.smtp_username, Config.smtp_password)
        message = "Subject: " + Config.subject + f"\n\n{content}"
        server.sendmail(Config.your_email, Config.friend_email, message)

# Generate and send email
print("Generating email content using the following prompt:\n\n", Config.gpt_prompt)
email_content = generate_email_content()
print("\n\nThe following email body was generated:\n\n", email_content)
print("\n\nAttempting to send the generated email from ", Config.your_email, " to ", Config.friend_email)
send_email(email_content)
print("\n\nEmail sent!")
