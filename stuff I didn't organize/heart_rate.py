"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

user_age = int(input('what is your age? '))
max_heart = 220 - user_age
upper_limit = round(.85 * max_heart)
lower_limit = round(.65 * max_heart)

print(f'when you exersise, keep your heart rate between {upper_limit} and {lower_limit}')