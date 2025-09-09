def calculate_mins(age_years):
    days_in_year=365.25
    hours_in_day=24
    mins_in_hour=60
    total_days=age_years*days_in_year
    total_hours=total_days*hours_in_day
    total_mins=total_hours*mins_in_hour
    print("\n Your are approx:")
    print(f"-- {total_days} days old")
    print(f"-- {total_hours} hours old")
    print(f"-- {total_mins} minutes old")
age= int(input("enter your age: "))
calculate_mins(age)