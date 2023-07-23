# CampMailerGPT
A simple application that generates an email body using the OpenAI ChatGPT API and emails it to the specified email address.

## Background
My sister-in-law is currently in a summer sleepaway camp and asked us if we can write her emails before she left (the camp prints and distributes the emails to the campers). However, she actually has access to a phone one a day for on hour, so she doesn't actually need the emails for communication. In reality, they become something of a popularity contest to see who gets more emails. Having said that, I discussed with her and devised a plan to write an application to take advantage of the ChatGPT API to generate emails to send to her daily with a scheduler.

## Usage
You need to change some variables in `config.py` to run the application. There's some comments there to help you.
After the configuration is complete, you can either just run `email_generator.py` whenever you want to send an email, or use a scheduler to automate the task.
