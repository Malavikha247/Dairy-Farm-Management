# Dairy-Farm-Management
A web-based Dairy Farm Management System built with Django and PostgreSQL to manage cattle, milk production, feeding, inventory, tasks, health records, and vaccination schedules with role-based dashboards and reporting.It also provides reporting features to help farm administrators and veterinarians monitor farm activities efficiently.

---

## 📌 Project Overview

Managing dairy farm operations manually can be time-consuming and prone to errors. This project provides a centralized web application where important farm records can be stored, managed, and accessed through a user-friendly interface.

The system supports different user roles, allowing administrators and veterinarians to access features according to their responsibilities.

### Key Objectives

- Digitize dairy farm management activities
- Maintain centralized cattle records
- Track daily milk production
- Manage cattle feeding records
- Monitor inventory and stock
- Schedule and track vaccination activities
- Maintain cattle health records
- Manage farm-related tasks
- Provide role-based access and dashboards
- Generate useful reports for monitoring and decision-making

---

## ✨ Features

### 👨‍💼 Admin Dashboard

Administrators can manage and monitor major farm operations through a centralized dashboard.

- Manage cattle records
- Monitor milk production
- Manage inventory
- Assign and track tasks
- View health records
- Monitor vaccination schedules
- Access farm reports
- Manage system data

### 🩺 Veterinarian Dashboard

The veterinarian module focuses on cattle health and medical management.

- View cattle information
- Add and update health records
- Maintain vaccination records
- Monitor vaccination schedules
- Track health-related activities
- Generate health-related reports

### 🐄 Cattle Management

Maintain detailed information about cattle, including:

- Cattle identification
- Breed information
- Age and gender
- Purchase details
- Other relevant cattle information

### 🥛 Milk Production Tracking

Record and monitor milk production data.

- Daily milk production records
- Production tracking
- Historical production data
- Production reports

### 🌾 Feeding Management

Manage cattle feeding activities and records.

- Feeding records
- Feed details
- Quantity tracking
- Feeding history

### 📦 Inventory Management

Track farm inventory and stock information.

- Add inventory items
- Update stock
- Monitor available quantities
- Track inventory usage

### 📋 Task Management

Manage and monitor farm-related tasks.

- Create tasks
- Assign tasks
- Track task status
- Monitor pending and completed tasks

### 🩺 Health Records

Maintain health information for individual cattle.

- Record health issues
- Add treatment information
- Maintain health history
- Track veterinary activities

### 💉 Vaccination Management

Manage vaccination schedules and records.

- Record vaccinations
- Track vaccination dates
- Monitor upcoming vaccinations
- Maintain vaccination history

### 📊 Reports

The system provides reporting functionality for monitoring farm operations.

- Farm management reports
- Milk production reports
- Cattle health reports
- Vaccination reports
- Inventory-related reports
- PDF report generation

---

## 🛠️ Technologies Used

### Backend
- Python
- Django

### Database
- PostgreSQL

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Reporting & Visualization
- Chart.js
- PDF Report Generation

### Development Tools
- Git
- GitHub
- Visual Studio Code

---

## 🏗️ System Architecture

The application follows a Django-based architecture:

```text
User
  │
  ▼
Web Interface
  │
  ▼
Django Application
  │
  ├── Authentication & Authorization
  ├── Cattle Management
  ├── Milk Production
  ├── Feeding Management
  ├── Inventory Management
  ├── Task Management
  ├── Health Records
  ├── Vaccination Management
  └── Reporting
  │
  ▼
PostgreSQL Database
