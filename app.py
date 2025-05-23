
import flask

app = flask.Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def multiples():
    
    print("Hello, this is a multiplier program")
    
    multiples_list = []
    error = None
    number = None


    if flask.request.method == "POST":
        num_str = flask.request.form.get('number') 
        
        if not num_str or not num_str.isdigit():
            error = "Please enter a valid number."
        else:
            number = int(num_str)
            multiples_list = [number * i for i in range(1, 11)]
            
    return flask.render_template('index.html', multiples=multiples_list, error=error, number=number)

if __name__ == '__main__':
    app.run(debug=True)