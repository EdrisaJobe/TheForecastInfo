# About TheForecastInfo
This site was made soley for the purpose of testing my abilities to retrive and display data on a custom built website, it displays weather conditions from most countries and cities.
It's very simplistic which was my main goal, make it easy to use yet visually pleasing. Feel free to ask me any information based on how I modeled some of the items within the form or
how I managed to import the OpenweatherAPI to get specific information.

[![Link - The Forecast Info](https://img.shields.io/badge/Link-The_Forecast_Info-3693F3?style=for-the-badge&logo=<svg+role%3D"img"+viewBox%3D"0+0+24+24"+xmlns%3D"http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg"><title>iCloud<%2Ftitle><path+d%3D"M13.762+4.29a6.51+6.51+0+0+0-5.669+3.332+3.571+3.571+0+0+0-1.558-.36+3.571+3.571+0+0+0-3.516+3A4.918+4.918+0+0+0+0+14.796a4.918+4.918+0+0+0+4.92+4.914+4.93+4.93+0+0+0+.617-.045h14.42c2.305-.272+4.041-2.258+4.043-4.589v-.009a4.594+4.594+0+0+0-3.727-4.508+6.51+6.51+0+0+0-6.511-6.27z"%2F><%2Fsvg>)](http://www.theforecast.info)
# Technology Used :hammer_and_wrench:

Frontend :gear:| Description|
-------|------------|
CSS    | Everything within the pages were styled using CSS, the design again is very minimilistic but clean and easy to use. Also, used it as a way to make it responsive to phones and other devices. 
Bootstrap| Visual aspects such as the textfield and button elements.
HTML   | Stores the Home/About pages, also used it to template tag all the necessary elements such as displaying the weather conditions which I defined via the Django application.

Backend :toolbox:| Description|
-------|------------|
Django | Django is a well known Python backend web framework which I used to gather all the necessary information. Mainly used for template tagging and connecting all the HTML pages as well as migrating my project to a database. Also used as a form of site/token protection from malicious intruders.
Python | Scripting language, used alongside Django to apply my logic. Python was used primarily on this project to implement all the key functions of the website. Although not made for web development, alongside Django they make a great duo.
Openweather| Grabbed all the necessary information from [OpenweatherAPI](https://openweathermap.org/api) which is very popular and updates frequently with the latest up-to-date weather information.

Libraries :books:| Description|
-------|------------|
urllib    | Used to fetch URLs for Python, uses the urlopen function to grab any website information using a variety of different protocols. In my case I used it to fetch an API and collected specific information from within the API.
whitenoise| Due to the fact Django does not have a way of supporting static files into production, whitenoise clears this barrier by placing all the required information into it's own separate folder which the web host (Heroku) can read from and apply any new changes.
gunicorn| [Gunicorn](https://github.com/benoitc/gunicorn) known as 'Green Unicorn' is a Python specific web server gateway. I used it as a way to pass requests data to my web application all through Heroku.

Web-services :cloud:| Description|
-------|------------|
Heroku | Heroku is a cloud platform for hosting and maintaining website information which I used to later connect the platform with GoDaddy. 
GoDaddy| Domain was registered from GoDaddy alongside all DNS setup.
