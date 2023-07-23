import openai

from dataclasses import dataclass

@dataclass
class Config:
    ### Configure OpenAI API
    # Get your API key here: https://platform.openai.com/account/api-keys
    openai.api_key = 'YOUR_API_KEY'
    # Write your prompt below. I've included mine as a template.
    # You can experiment with different prompts, GPT models, and temperature at https://platform.openai.com/playground
    # Keep in mind pricing differences for different models. See https://openai.com/pricing
    gpt_prompt = """My name is ____. My sister-in-law, ____, is in a summer camp called ____. Can you help me write an email to her? I want to talk about all of the fun things I've done today with my wife, her sister ____. You can make up the things that we did.
Please don't include a subject, only give me the body of the email."""
    gpt_model = 'gpt-3.5-turbo'
    gpt_temperature = 1.35

    ### Configure email settings
    friend_email = 'recipient-email@gmail.com'
    your_email = 'your-email'
    subject = 'you-email-subject'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'your-email@gmail.com'
    # The below can be your email password. But, if using Gmail, you'll need to use an app password, as your regular password won't work.
    # See https://support.google.com/accounts/answer/185833?hl=en for more information.
    smtp_password = 'your-email-password-or-app-password'
