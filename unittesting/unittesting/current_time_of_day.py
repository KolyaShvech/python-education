from datetime import datetime

def time_of_day():
    """Identifies current time of day.

    Returns:
        str: current time of day. Could be: "night", "morning", "afternoon".
    """
    now = datetime.now()
    if now.hour >= 0 and now.hour < 6:
        return "night"
    if now.hour >= 6 and now.hour < 12:
        return "morning"
    if now.hour >= 12 and now.hour < 18:
        return "afternoon"
    return "night"


print(time_of_day())
