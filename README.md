# weatherforecast

## Setting up the weather.ini file

In the root directory of the project, I have a weather.ini file that stores my Bing API key.

My weather.ini file looks like this:

    [DEFAULT]
    BING_API_KEY = # insert key here

To get a Bing API key, I followed the directions on this website:

https://learn.microsoft.com/en-us/bingmaps/getting-started/bing-maps-dev-center-help/getting-a-bing-maps-key

Bing Maps is a web service from Microsoft that is a lot like Google Maps.

Microsoft provides users with an API called the Bing Maps API.

One feature of the Bing Maps API is that it does geocoding, which means, it looks up the longitude and latitude for a city, and it looks up the place name for a pair of coordinates.

I followed the directions on the Microsoft website to get my Bing Maps API key, and then I pasted the key into my weather.ini file.

    [DEFAULT]
    BING_API_KEY = IPastedMyKeyHere

This property is all that's needed to setup the weather.ini file.

The webapp uses the BING_API_KEY property to retrieve the Bing Maps API key.

## Installing the requirements

I installed the requirements with pip.

The requirements can be installed all at once with the command:

    pip install -r requirements.txt

This command should be run in the root directory of the project, where the requirements.txt file resides.

It is also possible to install the requirements separately (one-by-one) on the commandline:

    % pip install Flask
    % pip install requests
    % pip install geocoder

I use the geocoder module to do geocoding (translating a city name to geoographical coordinates, and vice versa).

I use Flask as my web framework.

I use the requests module to query the api.weather.gov Weather API.

## Running the web application

The web application can be started by running the following command in the root directory of the project:

    python main.py

To get the webapp working properly, the requirements have to be installed, a weather.ini file has to be created, and a Bing Maps API key has to be pasted into the weather.ini file.

The weatherforecast application gets a weekly forecast for a city or a place. The user can search on the name of a city, or search on geographical coordinates (longitude and latitude), to look up a forecast.

## Opening the website

After starting the server with the command `python main.py`, the website can be opened in a web browser by visiting the URL

    http://localhost:8080

The web browser resolves the domain name "localhost" to the IP address 127.0.0.1. The port number 8080 is needed to open a socket with the server. The port number specifies which port the server is listening on.

## Some notes on network programming

Here are some definitions of words that are used in network programming.

1. A socket is a data structure consisting of an IP address and a port.
2. A stream is a data structure consisting of a series of packets and a series of time intervals.
3. A protocol is a set of rules.
4. A communication protocol is a set of rules for communication.
5. A web browser is a client that renders web content.
6. A web server is a server that distributes web content.

These definitions help us understand what's happening when we browse the internet using protocols like HTTP.