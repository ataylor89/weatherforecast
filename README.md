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

The web browser establishes a connection with a web server. A connection is uniquely defined by a pair of sockets. Each socket has the form ipaddr:port, where ipaddr is an IP address and port is a port number.

I think that the word *socket* originates in electrical sockets. When we plug a computer into an electrical socket, we create a connection between a wall socket and a socket (or port) on a computer that is designed to receive electricity. This connection allows for a current of electricity to pass between the wall socket and the computer.

A connection between two processes (in this case a web browser and a web server) allows for a stream of bytes to be sent over a connection. The web browser and the web server communicate using the hypertext transfer protocol (HTTP). A protocol is a set of rules. A communication protocol is a set of rules for communication.

HTTP is based on requests and responses. The web browser makes a GET request for the index page of a website. The web server responds to this GET request with the index page of the website.

The file `main.py` is literally the code for a web server. When we run the command `python main.py`, we start the web server. The web server is running on localhost (the client host machine) and listening on port 8080. When we open a web browser, we start the client. When we visit the URL `http://localhost:8080` in a web browser, we establish a connection between the web browser and the web server running at 127.0.0.1:8080. (The domain name `localhost` gets resolved to the IP address 127.0.0.1). The web browser makes a GET request for the index page of the web server. The web server responds with the contents of the `weather.html` index page.

So far the web server `main.py` has two web services that can be called by the browser. The first web service handles a GET request for the index page and it has the path `/`. The second web service handles a POST request for the forecast and it has the path `/forecast`. It is customary to use a GET request to retrieve a web page. It is common to use a POST request to submit a form. A POST request can send a large amount of data in the request body, which makes it ideal for submitting a form. When we click the "search" button in the search form, we send a POST request to the web server, which responds with a JSON containing the weather forecast. A JSON is a data structure that stores data in a key-value format.

I think that socket programming is easier to understand when we have formal definitions of key terms, like "socket" and "stream". A socket is a data structure consisting of an IP address and a port. A stream is a data structure consisting of a series of packets and a series of time intervals. We use streams to communicate over a connection. The stream breaks the data into chunks called "packets" and sends them at different time intervals. After opening a connection, we can write to a stream or read from a stream to send or receive data. 

When a web browser opens a web site, it opens a socket to the server, using the domain name and the port. Then it opens an input stream and an output stream, and communicates with the server according to the rules of the hypertext transfer protocol (HTTP). There are rules for a GET request, rules for a POST request, and rules for all kinds of HTTP requests. These rules are designed to make communication reliable and efficient.

The Internet and the World Wide Web both refer to a network of computers. Two computers in this network can communicate by establishing a connection. There are many communication protocols that they can use to communicate. HTTP is one communication protocol, and it allows a client to retrieve a webpage from a server. The client is called a web browser, and the server is called a web server. The client can issue a GET request to retrieve a web page from a server. If the GET request is successful, then the server provides the HTML of the web page in the response.