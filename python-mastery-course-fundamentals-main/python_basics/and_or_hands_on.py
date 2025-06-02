activities = ["hiking", "swimming", "museum", "picnic"]
group_interests = ["art", "history", "swimming"]

# check if an activity aligns with group interest
# "museum" in activities ==> True
# ("art" in group_interests  or "history" in group_interests) ==> True
# True and True = True
if "museum" in activities and (
    "art" in group_interests or "history" in group_interests
):
    print("We should visit the museum!")
elif "swimming" in activities and "swimming" in group_interests:
    print("Looks like a day at the pool is in order!")
else:
    print("Let's plan a picnic instead.")
