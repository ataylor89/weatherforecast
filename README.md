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

After starting the server with the command `python main.py`, the website can be opened in a web browser by visiting the URL `http://localhost:8080`.

## Some notes on the world wide web

What happens when a web browser opens a website?

The web browser creates a connection with a web server. A connection is uniquely defined by a pair of sockets. Each socket has the form ipaddr:port, where ipaddr is an IP address and port is a port number.

I think that the word *socket* comes from electrical engineering. We connect a computer to a source of electricity by plugging the computer into a socket. The connection between a wall socket and a computer socket allows for electricity to flow into a computer.

In order to exchange data between two computers, we create a connection. The two computers communicate according to a protocol. One defition of protocol is this: a protocol is a set of rules. We can think of a communication protocol as a set of rules for communication.

HTTP is a protocol that helps two computers exchange hypertext documents. A hypertext document is written in code that is understood by the web browser (HTML, JavaScript, CSS). 

HTTP is based on requests and responses. A web browser can retrieve a web page from a server using a GET request. The web server can respond to a GET request with the HTML of the web page.

In the weatherforecast application, the file `main.py` contains the code for a web server. When we run the command `python main.py`, we start the web server. We can run the web server locally, which means, running it on the same machine as the client. We can open a web browser and visit the URL `http://localhost:8080` to get the index page of the web server. The domain name `localhost` gets translated to the IP address 127.0.0.1. We add the port number 8080 to the URL because the web server is listening on port 8080.

So far the web server has two web services that can be called by the web browser. The first web service handles a GET request for the index page and it has the path `/`. The second web service handles a POST request for the forecast and it has the path `/forecast`. It is customary to use a GET request to retrieve a web page. It is common to use a POST request to submit a form. A POST request can fit a large amount of data into the request body, making it deal for submitting a form. When we click the "search" button in the search form, we submit the form as a POST request. The web server processes the POST request and responds with a JSON that contains the data of the forecast. A JSON is a data structure that stores data in a key-value format.

On a more technical level, the web browser opens a socket to communicate with the web server. After that, the web browser opens a stream to send and receive data over the connection. Socket programming is easier to understand when we are given formal definitions for important words. My understanding is this... A socket is a data structure consisting of an IP address and a port. A stream is a data structure consisting of a series of packets and a series of time intervals. I think that we send the packets in a stream at different time intervals. The transmission contol protocol (TCP) requires the server to inform the client that a packet was received.

The Internet and the World Wide Web both refer to a network of computers. Users can download code from a web server and run that code inside a web browser. The code has to be written in a language that is understood by the web browser. HTML, JavaScript, and CSS are three languages that are understood by web browsers.

The weatherforecast application is a web server that can be accessed by a web browser. In addition to generating a web page in HTML, we create a set of web services that can be used by the web page.