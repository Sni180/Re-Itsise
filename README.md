# Re Itsise - Community Fault Reporting Platform

**See, Inform, Track — Together**

A Django-based web application that empowers communities to report, track, and manage infrastructure issues (faults) in real-time. Re Itsise is designed to facilitate communication between residents and service providers about infrastructure problems like water leaks, burst pipes, potholes, and electrical issues.

### Core Features
- **📍 Fault Reporting**: Users can log infrastructure issues with location, category, description, images, and audio evidence
- **🔍 Search & Discovery**: Search reports by location, category name, or reference number
- **👥 Community Participation**: Mark yourself as affected by a reported issue to stay updated
- **📊 Real-time Status Tracking**: Track fault status from Logged → Dispatched → In Progress → Resolved
- **📱 Responsive Design**: Mobile-friendly interface with modern UI/UX
- **🏷️ Categorized Issues**: Support for multiple fault categories including:
  - ⚡ Electricity Issues
  - 💧 Water Leaks
  - 🌊 Burst Pipes
  - 🕳️ Missing Manholes
  - 🏗️ Rubble
  - ⛈️ Storm Water
  - 🚽 Sanitation
  - 🚧 Potholes
  - 🌳 Other Issues

### Additional Features

- Admin dashboard for managing reports
- Multi-step report creation process
- Evidence collection (photos and audio)
- Automatic reference number generation
- Community activity timeline

---

## Project Overview
Purpose

Re Itsise creates a bridge between communities and service providers by:
- Enabling transparent, real-time reporting of infrastructure issues
- Allowing multiple residents to join and track the same issue
- Maintaining accountability through status tracking
- Building community awareness of ongoing work

### Target Users
- **Residents**: Report issues and stay informed about repairs
- **Service Providers**: Manage and track incoming reports
- **Administrators**: Monitor platform activity and manage content
- 
## Technology Stack

- **Backend**: Django 6.0.3
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: Pillow (PIL)
- **Database Tools**: sqlparse

## Features in Detail

### 1. Fault Explorer (Homepage)

- **Search Functionality**: Search reports by:
  - Location address
  - Fault category (with keyword mapping)
  - Reference number
  - Description text
  
- **Report Cards**: Each report displays:
  - Category with emoji icon
  - Location and description
  - Current status with progress bar
  - Time since reported (relative time)
  - Number of affected residents
  - "I'm Affected" button

- **Live Status**: Shows "Kimberley Live" indicating the active location

### 2. Report Creation

Multi-step process to collect:
- **Step 1**: Reporter's name and phone number
- **Step 2**: Fault category and location details
- **Step 3**: Description, photo evidence, and optional audio

### 3. "I'm Affected" Feature

- Modal dialog for residents to join an existing report
- Collects affected resident's name and phone number
- Updates affected resident count
- Notifications sent to joined residents on status updates

### 4. Status Tracking

Four-stage workflow with visual progress indicator:
1. **LOG** (25%): Issue logged in system
2. **DIS** (50%): Dispatched to service team
3. **PROG** (75%): Currently being worked on
4. **RES** (100%): Problem resolved

Proudly designed and developed by Sinikiwe Phiri
