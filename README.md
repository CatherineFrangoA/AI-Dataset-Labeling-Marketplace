# AI Dataset Labeling Marketplace

## 📌 Project Overview

The AI Dataset Labeling Marketplace is a web-based application designed to simplify dataset labeling management.

The platform allows users to register and log in, upload datasets, assign labeling tasks, complete tasks, review submitted work, and download dataset files. It also includes an AI Agent that demonstrates the Perceive → Plan → Act → Observe workflow for basic dataset analysis.

## 🎯 Objectives

- Provide user registration and login.
- Allow dataset owners to upload datasets.
- Store dataset information in a database.
- Assign labeling tasks to labelers.
- Track task completion status.
- Submit reviews and approval/rejection status.
- Download stored dataset files.
- Demonstrate an AI Agent workflow.
- Maintain a modular backend structure.

## 👥 User Roles

- **Admin** – manages and monitors the platform.
- **Dataset Owner** – uploads datasets and manages labeling activities.
- **Labeler** – completes assigned labeling tasks.
- **Reviewer** – reviews completed tasks.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| SQLAlchemy | Database ORM |
| SQLite | Current development database |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend interaction and API integration |
| Git & GitHub | Version control |
| Swagger / OpenAPI | API testing |

## 🏗️ Project Structure

```text
AI-Dataset-Labeling-Marketplace/
│
├── backend/
│   ├── api/
│   │   ├── user.py
│   │   ├── dataset.py
│   │   ├── task.py
│   │   └── review.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── dataset.py
│   │   ├── label_task.py
│   │   └── review.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── dataset_schema.py
│   │
│   ├── uploads/
│   ├── agent.py
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── agent.html
│   ├── task.html
│   ├── script.js
│   └── style.css
│
├── docs/
├── .gitignore
├── Problem_Statement.md
└── README.md

## 🔄 System Workflow

text
Register
   ↓
Login
   ↓
Upload Dataset
   ↓
Assign Labeling Task
   ↓
Labeler Completes Task
   ↓
Review Task
   ↓
Approve / Reject
   ↓
Download Dataset

🤖 AI Agent Workflow

The project includes an AI Agent based on the following workflow:

PERCEIVE
   ↓
PLAN
   ↓
ACT
   ↓
OBSERVE

Perceive

Receives and reads the supplied data.

Plan

Determines the processing approach.

Act

Performs the planned dataset analysis or action.

Observe

Records the result and observations.

🔌 API Endpoints

Method	Endpoint	Description

POST	/api/register	Register a user
POST	/api/login	Login a user
POST	/api/dataset/upload	Upload a dataset
GET	/api/dataset/download/{dataset_id}	Download a dataset file
POST	/api/task/assign	Assign a labeling task
PUT	/api/task/complete/{task_id}	Complete a task
POST	/api/review/submit	Submit a review
POST	/agent/run	Run the AI Agent


🗄️ Database Entities

User

id – Primary Key

fullname

email

username

password


Dataset

id – Primary Key

name

filename

owner_id

status


LabelTask

id – Primary Key

dataset_id

labeler_id

status


Review

id – Primary Key

task_id

reviewer_id

status


🧪 Testing

The following features have been tested:

User registration

User login

Dataset upload

AI Agent execution

Task assignment

Task completion

Review submission

Dataset download

Frontend and backend API integration


▶️ How to Run

1. Clone the repository

git clone https://github.com/CatherineFrangoA/AI-Dataset-Labeling-Marketplace.git

2. Open the backend

cd AI-Dataset-Labeling-Marketplace/backend

3. Install dependencies

pip install -r requirements.txt

4. Start FastAPI

python -m uvicorn app:app --reload

Backend:

http://127.0.0.1:8000

5. Open Swagger

http://127.0.0.1:8000/docs

6. Run the frontend

Open the frontend folder using VS Code Live Server.

📂 Dataset Handling

Uploaded dataset files are stored in the backend upload directory.

The download endpoint allows the stored dataset file to be downloaded using its dataset ID.

🔐 Security Notes

The current project is an academic MVP/development implementation.

Future security improvements include:

Bcrypt password hashing

Environment variables for secrets

Role-based authorization

File type and file size validation

Stronger authentication


🚀 Future Enhancements

MySQL database integration

Automatic generation of final labeled datasets

Label and category management

Advanced role-based access control

Automated API testing

Improved dataset validation

Dataset analytics dashboard

Production deployment


📌 Project Scope

Included

User registration and login

Dataset upload

Dataset management

Task assignment

Task completion

Review and approval

Dataset download

AI Agent demonstration


Out of Scope

Payment Gateway

Mobile Application

Live Chat

Multi-language Support


📚 Documentation

The project includes:

Problem Statement

ER Diagram

Architecture Diagram

Class / Module Diagram

Project Documentation

API documentation through Swagger


👩‍💻 Author

Catherine Frango

B.Tech Information Technology
J.J. College of Engineering and Technology (JJCET), Trichy

📄 License

This project is developed for academic and educational purposes.