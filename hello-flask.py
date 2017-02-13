from flask import Flask,render_template,jsonify
app= Flask(__name__)
# @app.route('/')
@app.route('/hello/')  
@app.route('/hello/<name>')  
def hello(name=None):
	# Test1 Begin
    # response = "<html>\n"
    # response += "<title>Flask Test</title>\n"
    # response += "<body>\n"
    # response += "<h2>Hello World\n</h2>"
    # response += "</body>\n"
    # response += "</html>\n"
    # return response
    # Test1 End
    # return render_template("hello.html")   #Test 2
    if name == None:  
        name = "Neilzp_20170213"  
    templateDate = {'name' : name};  
    return render_template("hello.html", **templateDate)

if __name__ == '__main__':  

