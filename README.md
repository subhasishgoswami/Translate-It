<h1 align="center" >Translate It</h1>
<h3 align="center"> A Web App made with Textblob and Flask</h3>

## Technologies used
* Python
* textblob
* flask
* HTML, CSS

### Demo
https://ratemovie.herokuapp.com/

<p align="center">
  <img src="demo.png"/>
</p>

### Project Structure
This project has three major parts :
1. app.py - This part has the python code to get the text in form of blob and then translating it.
2. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
3. app.html - The HTML template to allow user to enter the text which is then translated.

### Steps to run the application

1. Run app.py using the command below to start Flask API
```
python app.py
```
   
2. Navigate to URL http://localhost:5000

3. Enter your text and translate it

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the command below to send the request with some pre-popuated values -
```
python request.py
```

<br>


