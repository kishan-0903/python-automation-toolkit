# Goal: Analyze views for 3 videos and check progress percentage
all_views = []

for i in range(3):
    view = int(input(f"Enter views for video {i+1}: "))
    all_views.append(view)

total_earnings = sum(all_views) * 0.50

if total_earnings >= 50000:
    print("Success: 50k Goal Reached!")
else:
    percent = (total_earnings / 50000) * 100
    print(f"Progress: {round(percent, 2)}% of the way to 50k.")