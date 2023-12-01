from zoneinfo import ZoneInfo
from datetime import datetime
import json
import requests
from pathlib import Path
from string import Template
from subprocess import run
from time import sleep
from webbrowser import open as open_browser
import os

aoc_start = datetime(2023, 12, 1, 0, 0, 0, tzinfo=ZoneInfo("America/New_York"))

if "TEST" in os.environ:
    year = 2022
    day = 1
else:
    year = aoc_start.year
    day = (datetime.now(tz=ZoneInfo("America/New_York")) - aoc_start).days + 1

if day < 1:
    print("Advent of Code has not started yet!")
    exit(1)

root_dir = Path(__file__).parent.parent.absolute()
input_file = root_dir / "input" / f"{day}"

if not input_file.exists():
    print(f"Downloading input for day {day}...")
    cookies_file = root_dir / "cookies.json"
    print(cookies_file)
    if not cookies_file.exists():
        print("Please create a cookies.json file with your session cookie!")
        exit(1)
    cookies = json.load(open(cookies_file))
    res = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies)
    res.raise_for_status()

    input_file.write_text(res.text)
    print("Downloaded input!")


tpl = Template(open(root_dir / "scripts" / "solution_template.py").read()).substitute(day_id=day)

solution_file = root_dir / "solutions" / f"{day}.py"
if not solution_file.exists():
    solution_file.write_text(tpl)
    open_browser(f"https://adventofcode.com/{year}/day/{day}")

print(f"Opening solution file for day {day}...")
run(["code", solution_file])

modified_time = solution_file.stat().st_mtime
while True:
    print("\033[2J\033[H") # clear screen
    print("Running solution... (will rerun on file change)")
    out = run(["python", solution_file])

    print("Exit code", out.returncode)

    while True:
        sleep(0.5)
        new_modified_time = solution_file.stat().st_mtime
        if new_modified_time != modified_time:
            modified_time = new_modified_time
            break