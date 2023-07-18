import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to search and retrieve matching entries
def search_entries(search_term):
    search_term = search_term.lower()
    df['SAP ID'] = df['SAP ID'].astype(str)  # Convert 'SAP ID' column to string type
    matching_entries = df[(df['SAP ID'].str.lower().str.contains(search_term)) |
                          (df['Student Name'].str.lower().str.contains(search_term))]
    return matching_entries.to_html(index=False)


# Load the Excel file into a pandas DataFrame
df = pd.read_excel('Higher_Studies.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    results = search_entries(search_term)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
