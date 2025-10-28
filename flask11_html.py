from flask import Flask
app = Flask(__name__)
@app.route('/')
def foo():
    return '''
<html lang="en">
<body>
	<label for="myTextbox">Enter Text : </label>
	<input type="text" id="myTextbox" name="myTextbox"><br><br>
	
	
 <label for="myCheckbox">Check this:</label>

 <input type="checkbox" id="myCheckbox" name="myCheckbox"><br><br>
 <label for="radio1">Option 1:</label>
 <input type="radio" id="radiol" name="myRadio" value="1">
 <label for="radio2">Option 2:</label>
 <input type="radio" id="radio" name="myRadio" value="2"><br><br>
 <button type="button">Click me</button>
</body>
</html>

'''

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False,port=4000)
    
# run this code and then write 127.0.0.1:4000 in url