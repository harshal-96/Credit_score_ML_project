# Automated Credit Risk Assessment System Documentation

## Overview

The Automated Credit Risk Assessment System is a Flask web application that predicts the credit risk score of loan applicants based on user inputs. The system utilizes a pre-trained machine learning pipeline to analyze various applicant details and provides a prediction on their credit risk.

## Features

- **User-Friendly Interface**: An easy-to-use web interface for entering applicant details.
- **Predictive Analysis**: Predicts credit risk score using a machine learning model.
- **Dynamic Input Options**: Includes dropdowns for states, cities, occupations, and employment profiles to streamline user input.

## Setup and Installation

### Prerequisites

- **Python 3.7+**
- **Flask**
- **pandas**
- **pickle**

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**:
    ```bash
    pip install Flask pandas
    ```

3. **Place the Model Pipeline**:
    - Ensure that the pickled machine learning pipeline (`pipeline.pkl`) is in the project directory.

## How to Run

1. **Start the Flask Application**:
    ```bash
    python app.py
    ```

2. **Access the Web Application**:
    - Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

### Home Page

- **Form Fields**:
    - **Age**: Enter the applicant's age.
    - **Gender**: Select the applicant's gender (Male/Female).
    - **Income**: Enter the applicant's income.
    - **Credit History Length**: Enter the length of the applicant's credit history.
    - **Number of Existing Loans**: Enter the number of existing loans the applicant has.
    - **Loan Amount**: Enter the amount of loan the applicant is applying for.
    - **Loan Tenure**: Enter the tenure of the loan in months.
    - **Existing Customer**: Select if the applicant is an existing customer (Yes/No).
    - **State**: Select the applicant's state from the dropdown.
    - **City**: Select the applicant's city from the dropdown.
    - **LTV Ratio**: Enter the loan-to-value ratio.
    - **Employment Profile**: Select the employment profile from the dropdown.
    - **Occupation**: Select the occupation from the dropdown.

### Prediction

- **Submit the Form**: Click the "Submit" button to process the input data.
- **View Results**: The prediction result will be displayed on a new page, indicating the applicant's credit risk score.

## Project Structure

- `app.py`: Main application script containing routes and prediction logic.
- `templates/`: Directory containing HTML templates for the web pages.
    - `index.html`: Home page template with the input form.
    - `result.html`: Result page template displaying the prediction.
- `pipeline.pkl`: Pickled machine learning pipeline used for predictions.

## Dependencies

- Flask: For creating the web application.
- pandas: For data manipulation.
- pickle: For loading the pre-trained machine learning model.

## Acknowledgements

This project uses the following technologies and libraries:
- Flask
- pandas
- pickle

## Contact

For any inquiries or support, please contact Harshal Dhandrut at harshal.dhandrut@gmail.com.
