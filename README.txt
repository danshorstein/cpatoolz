To run the application:

1) make sure Flask is installed
   ('pip install flask' to install it via command line)

2) run the runserver.py file via command line. 

3) In the browser, navigate to localhost:5000/dashboard
   You should see the basic dashboard.
   
NOTE: for deploying on an actual server, we'll need to setup 
      something for the server to communicate with Flask. This
	  could be gunicorn or other intermediary.
	  
	  References: 
	  https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04
	  https://damyanon.net/flask-series-deployment/
	  http://flask.pocoo.org/docs/0.12/deploying/
	  
	  
	  