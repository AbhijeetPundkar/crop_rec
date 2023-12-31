from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = [float(request.form['nitrogen']),
                    float(request.form['phosphourus']),
                    float(request.form['potassium']),
                    float(request.form['temperature']),
                    float(request.form['humidity']),
                    float(request.form['ph']),
                    float(request.form['rainfall']),
                    ]
        prediction1 = model.predict([features])[0]
        url = f"static/images/{prediction1}.jpg"

        return render_template('result.html', prediction1=prediction1, url = url)

if __name__ == '__main__':
    app.run(debug=True)
