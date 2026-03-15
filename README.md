# AI Interview System

AI Interview System is a web-based application built using Python and Flask that simulates an interview environment for candidates. The system asks interview questions, records answers using speech recognition, evaluates responses using scoring algorithms, and stores results in a database.

## Features
- Automated interview question system
- Speech-based answer input
- Candidate scoring system
- Result tracking and storage
- Admin panel to view results

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Speech Recognition
- SQLite Database

## Project Structure
app.py – Main Flask application  
interview_engine.py – Interview question logic  
scoring_engine.py – Answer evaluation system  
speech_engine.py – Speech recognition module  
database.py – Database operations  
questions.csv – Interview questions dataset  
results.db – Candidate result storage

## Run the Project
pip install -r requirements.txt  
python app.py
