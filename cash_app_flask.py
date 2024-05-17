from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pickled pipeline
with open('pipeline.pkl', 'rb') as pipeline_file:
    pipeline = pickle.load(pipeline_file)

# Define options for select boxes
states = ['Karnataka', 'Uttar Pradesh', 'Tamil Nadu', 'West Bengal', 'Rajasthan', 'Maharashtra', 
          'Gujarat', 'Telangana', 'Kerala', 'Delhi']

cities = ['Mysuru', 'Bengaluru', 'Kanpur', 'Coimbatore', 'Lucknow', 'Kolkata', 'Jaipur', 'Nagpur', 
          'Surat', 'Hyderabad', 'Chennai', 'Thiruvananthapuram', 'Udaipur', 'New Delhi', 'Mumbai', 
          'Manjari', 'Dhulagori', 'Pune', 'Nellikuppam', 'Kochi', 'Ahmedabad', 'Channarayapatna', 
          'Bishanpura']

occupations = ['Doctor', 'Software Engineer', 'Banker', 'Contractor', 'Teacher', 'Farmer', 'Writer', 
               'Shopkeeper', 'Photographer', 'Student', 'Civil Servant', 'Unoccupied', 
               'Independent Consultant', 'Graphic Designer', 'Business Owner']

employment_profiles = ['Salaried', 'Self-Employed', 'Freelancer', 'Student', 'Unemployed']

@app.route('/')
def home():
    return render_template('index.html', states=states, cities=cities, occupations=occupations, employment_profiles=employment_profiles)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input data
        age = int(request.form['age'])
        gender = request.form['gender']
        income = float(request.form['income'])
        credit_history_length = float(request.form['credit_history_length'])
        num_existing_loans = float(request.form['num_existing_loans'])
        loan_amount = float(request.form['loan_amount'])
        loan_tenure = float(request.form['loan_tenure'])
        existing_customer = request.form['existing_customer']
        state = request.form['state']
        city = request.form['city']
        ltv_ratio = float(request.form['ltv_ratio'])
        employment_profile = request.form['employment_profile']
        occupation = request.form['occupation']

        # Preprocess user input
        input_data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Income': [income],
            'Credit History Length': [credit_history_length],
            'Number of Existing Loans': [num_existing_loans],
            'Loan Amount': [loan_amount],
            'Loan Tenure': [loan_tenure],
            'Existing Customer': [existing_customer],
            'State': [state],
            'City': [city],
            'LTV Ratio': [ltv_ratio],
            'Employment Profile': [employment_profile],
            'Occupation': [occupation]
        })

        # Make loan score prediction
        prediction = pipeline.predict(input_data)

        # Return prediction
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
