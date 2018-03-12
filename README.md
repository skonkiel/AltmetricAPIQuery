# AltmetricAPIQuery

This is a bare-bones Python script that's intended to be used by researchers who
are just learning how to query the Altmetric API, as well as those that want the freedom to tinker. You will have to
tweak it to be able to locally save the data that's pulled from the API. It assumes you have a CSV file
full of DOIs and/or PMIDs that you want to use to query the API.

There are Python packages already out there for querying the Altmetric
API in Python, but for a variety of reasons you may want to use a simple script instead. (At least,
that's what I wanted when I was first starting out so I could learn how everything works, so I thought I'd share my own script for others to use, too.)

Edits welcome.

I may not be able to provide technical support, so caveat emptor.

## How to use

1. Make sure Python 3 is installed on your machine
2. Download the script to the directory where your CSV file lives
3. Open your command line tool (Terminal on Mac), navigate to the directory where the script has been downloaded, then
type ```python3.6 AltmetricAPIQuery_Basic.py``` to run the script
4. Tweak the script to meet your needs, then run it again
5. Rinse and repeat

## Resources

* [Altmetric API documentation](https://api.altmetric.com)
* To join the Altmetric Researcher Data Access Program and get an API key issued, email info@altmetric.com.
* [For a good primer on querying the Altmetric API and how to build out your script, check out this video.](https://www.youtube.com/watch?v=k981sK4ODWI)
* Existing Python scripts for using the Altmetric API include [pyAltmetric](https://github.com/wearp/pyAltmetric), [PyAltmetric](https://github.com/CenterForOpenScience/PyAltmetric), and [Python-Altmetric](https://github.com/lnielsen/python-altmetric)
