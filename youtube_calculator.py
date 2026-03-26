# Goal: Calculate YouTube earnings based on views
channel_name = input("Enter your YouTube channel name: ")
views = int(input("How many views did you get? "))
earnings = views * 0.50

print(f"--- {channel_name} Report ---")
if earnings >= 50000:
    print("Goal Reached! You can work from home.")
else:
    needed = 50000 - earnings
    print(f"Current Earnings: ₹{earnings}")
    print(f"You need ₹{needed} more to reach your 50k goal.")