# Coursework 2 - Multi-Domain Intelligence Platform 
**Name:** Madiyar Auyelbek

**Student ID:** M01033592

**Lecturer:** Mr.Santosh Menon 

**Module:** CST1510

## This project is a Web Application where user can work with diffrent domains, such as: Cybersecurity, IT Support, and Datasets.
### In the system user can register, log in, see data, and use AI assistant chat.(OPENAI)


## 1.  Home Page.
User allows to register or log in, afterwards he will be directed to the Dashboard page. 

## 2. Dashboard Page.
On this page user can view the data of all three domains:
- Number of Cybersecurity incidents
- Number of IT support tickets
- Number of Datasets
- The graph for each domains

## Cybersecurity Incident Page.
- Displays all incidents and shows the status
- User allows to add or delete incidents

## IT Support Tickets Page.
- Displays all IT tickets and shows the status
- User allows to add or delete tickets

## Datasets Page.
- Displays all datasets with detailed information
- User allows to add or delete dataset

## AI Assistant.
- Helpful chat assistant using OpenAI 
- User can choose a domain:
- Cybersecurity
- IT Support
- Datasets
- General
- Assistant replies base on the chosen domain

## How the Web Application Works

- When the application runs, it creates database tables 
- CSV files are loaded into the tables
- User can register and log in 
- After login, all the pages will be available to a user 



## Project Structure.

```
CW2_M01033592_CST1510/
├── .streamlit/
│   └── secrets.toml
├── .venv/
├── app/
│   ├── data/
│   │   ├── DATA/
│   │   │   ├── cyber_incidents.csv
│   │   │   ├── datasets_metadata.csv
│   │   │   ├── it_tickets.csv
│   │   │   └── users.txt
│   │   ├── datasets.py
│   │   ├── db.py
│   │   ├── incidents.py
│   │   ├── schema.py
│   │   ├── tickets.py
│   │   └── users.py
│   ├── services/
│   │   ├── ai_service.py
│   │   └── user_services.py
│   └── DATA/
│       ├── cyber_incidents.csv
│       ├── datasets_metadata.csv
│       ├── it_tickets.csv
│       └── users.txt
├── logo/
│   └── barcelona.png
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Incidents.py
│   ├── 3_Tickets.py
│   ├── 4_Datasets.py
│   └── 5_AI_Assistent.py
├── Home.py
├── README.md
└── requirements.txt
```

## How to run.
- Run Home.py, copy streamlit run, and paste the streamlit run in the terminal. 

