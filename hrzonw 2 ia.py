# Function to compute maximum heart rate
def maxHR(age):
    return 208 - 0.7 * age

# Function to determine heart rate zone
def hrZone(hr, max_hr):
    percentage = (hr / max_hr) * 100
    if percentage < 50:
        return "Below Zone 1"
    elif percentage < 60:
        return "Zone 1 (Very Light)"
    elif percentage < 70:
        return "Zone 2 (Light)"
    elif percentage < 80:
        return "Zone 3 (Moderate)"
    elif percentage < 90:
        return "Zone 4 (Hard)"
    else:
        return "Zone 5 (Maximum)"

# Ask user for age
age = int(input('Enter your age: '))
max_hr = maxHR(age)
print(f'Your max heart rate is {max_hr:.0f} bpm')

# Ask user for heart rate during training
hr = int(input('Enter your heart rate during training: '))

# Determine and display heart rate zone
zone = hrZone(hr, max_hr)
print(f'Your training was in: {zone}')
