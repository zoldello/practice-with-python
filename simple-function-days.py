__author__ = "Phil"

import random

def get_days():
  days = ["Monday", "Tuesday", "Wedesday", "Thursday", "Friday", "Saturday", "Sunday"]

  return days


def get_weather_report():
  weather = ["Sunny", "Rainy", "Hot", "Lovely"]
  report = weather[random.randint(0, len(weather)- 1)]

  return report

def main():
  days = get_days()

  for day in days:
    report = get_weather_report()
    print("Weather on {0} is {1}".format(day, report))


if __name__ == "__main__":
  main()
