# AI Dataset Labeling Marketplace

## Project Description

AI Dataset Labeling Marketplace is a platform designed to help users manage datasets, perform data labeling, review labels, and receive AI-assisted labeling suggestions.

The project contains a frontend interface, a FastAPI backend, a database, and an AI Agent Loop.

## Features

- User Registration
- User Login
- Dataset Management
- Dataset Labeling
- Label Review
- AI-assisted Label Suggestions
- AI Agent Loop
- Agent activity logging

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### AI Agent

The AI Agent follows the Agent Loop:

Perceive → Plan → Act → Observe

The agent uses two tools:

1. Dataset Row Counting Tool
2. Label Suggestion Tool

All agent activities are recorded in the agent log file.

## Project Structure

```text
AI-Dataset-Labeling-Marketplace/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── script.js
│   └── style.css
│
├── backend/
│   ├── app.py
│   ├── agent.py
│   ├── agent.log
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── users.db
│
├── docs/
│   ├── Architecture.png
│   ├── architecture_src code.xml.drawio
│   ├── ER_Diagram.png
│   ├── ER_Diagram_src code.dbml
│   └── README.md
│
├── Problem_Statement.md
└── README.md