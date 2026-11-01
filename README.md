# Project-Tikirilia

### An Interactive Cultural Companion Doll and App for Tourists and Children

---

## 📌 Project Overview

**Smart Tikirilia 1.0** is an interactive cultural companion doll designed to introduce Sri Lankan culture, languages, traditions, and tourism to tourists and children.

The project combines a physical smart doll with a companion mobile application. The doll can speak, sing, teach Sinhala and Tamil phrases, and share Sri Lankan folk stories. Its companion app acts as a visitor's guide and travel diary, allowing users to unlock tourist destinations, earn badges, upload photographs, and record their travel experiences.

The project aims to make cultural learning more interactive while encouraging visitors to explore Sri Lanka and appreciate its cultural heritage.

## 🎯 Project Objectives

- Promote Sri Lankan cultural heritage, traditions, and folk stories.
- Introduce tourists and children to Sinhala and Tamil languages.
- Develop an interactive doll capable of speaking, singing, and responding to user interactions.
- Provide a companion mobile application for controlling and interacting with the doll.
- Encourage tourism through destination unlocking and achievement badges.
- Allow visitors to document their journeys through photographs and travel diaries.
- Support the preservation and sharing of Sri Lankan cultural knowledge.

## 🌍 Sustainable Development Goals (SDG Alignment)

The project supports the following United Nations Sustainable Development Goals:

| SDG | Goal | Project Contribution |
|---|---|---|
| SDG 4 | Quality Education | Promotes cultural diversity and heritage through language teaching, stories, and festivals. |
| SDG 8 | Decent Work and Economic Growth | Encourages sustainable tourism and promotes local culture and products. |
| SDG 11 | Sustainable Cities and Communities | Helps preserve and share Sri Lankan folk stories, songs, and festivals. |

---

## 🧸 Project Components

The Smart Tikirilia system consists of four main development components.

### 1. Physical Doll and Firmware

The physical doll is designed in traditional Sri Lankan costume, with electronic components integrated into its body while maintaining its appearance as a traditional doll.

**Main hardware features:**

- **Costume NFC Tags:** NFC tags are placed inside flowers or accessories on the doll's head. Different accessories represent different costumes, cultures, regions, or festivals.
- **Microphone and Speaker:** Built into the face to support listening, speaking, conversations, and audio playback.
- **Chest button:** Triggers the "Ayubowan" greeting when touched.
- **Stomach button:** Triggers traditional songs and kavi when touched.
- **LED Bracelet:** Displays the doll's status:
  - Red – Low battery.
  - Green – Fully charged.
  - Blinking – Doll is speaking.
- **Tracker:** Worn on the hand opposite the LED bracelet.
- **Rechargeable Battery:** Housed inside a battery box within the doll.
- **Charging Port:** Located at the ankle of one leg.
- **Volume Control and ON/OFF Switch:** Located on the back of the doll.

The firmware is responsible for controlling the electronic components, reading sensor inputs, processing NFC interactions, and managing the doll's responses.

### 2. Mobile Application

The mobile application acts as the companion interface for interacting with the doll and exploring Sri Lankan tourism and culture.

**Main application features:**

#### Front Interface
- About Doll
- Customised Doll Profile

#### Teaching Mode
- Sinhala and Tamil phrases.
- Simple conversation practice.
- Sri Lankan cultural and folk stories.
- Information about Sri Lankan culture and festivals.

#### Diary / Journal Mode
- All tourist destinations initially appear locked.
- Destinations become unlocked when visitors travel to the respective places.
- Visitors earn badges for unlocked destinations.
- Upload photographs and record travel experiences.
- Add photographs taken with the doll.

#### Journey Timeline
- Displays the visitor's overall journey.
- Allows users to view their travel experiences in chronological order.

### 3. Backend System

The backend provides the server-side functionality required by the mobile application and other system components.

**Planned responsibilities:**

- Manage application data and user information.
- Provide APIs for mobile application communication.
- Store and retrieve travel journal entries and photographs.
- Manage tourist destinations, unlocking records, and badges.
- Support cultural and educational content.
- Handle external service integrations where required.

### 4. Team Website

The team website provides information about Smart Tikirilia 1.0 and introduces the development team.

**Planned responsibilities:**

- Introduce the Smart Tikirilia project.
- Present team members and their responsibilities.
- Explain project objectives and features.
- Showcase the doll, mobile application, and project development.

---

## 🏗️ Repository Architecture

This project follows a **Monorepo Architecture**.

A monorepo is a single Git repository that contains multiple related components of the same project. Each component maintains its own source code, dependencies, configuration, documentation, and tests.

### Repository Folder Structure

```text
smart-tikirilia/
│
├── README.md
├── .gitignore
│
├── docs/
│   ├── client-brief.md
│   ├── requirements.md
│   ├── system-architecture.md
│   ├── database-design.md
│   ├── API-documentation.md
│   ├── team-working-agreement.md
│   ├── product-backlog.md
│   ├── release-roadmap.md
│   └── meeting-minutes/
│
├── team-website/
│   ├── README.md
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── assets/
│   │   └── styles/
│   ├── tests/
│   └── package.json
│
├── mobile-app/
│   ├── README.md
│   ├── lib/
│   │   ├── screens/
│   │   │   ├── home/
│   │   │   ├── teaching/
│   │   │   ├── journal/
│   │   │   ├── journey/
│   │   │   └── profile/
│   │   │
│   │   ├── widgets/
│   │   ├── models/
│   │   ├── services/
│   │   ├── providers/
│   │   └── navigation/
│   │
│   ├── assets/
│   │   ├── images/
│   │   ├── icons/
│   │   ├── audio/
│   │   └── fonts/
│   │
│   ├── test/
│   └── pubspec.yaml
│
├── backend/
│   ├── README.md
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── ...
│   │   │   └── resources/
│   │   └── test/
│   └── pom.xml
│
├── firmware/
│   ├── README.md
│   ├── src/
│   │   ├── main.cpp
│   │   ├── sensors/
│   │   ├── nfc/
│   │   ├── audio/
│   │   ├── communication/
│   │   └── power/
│   │
│   ├── include/
│   ├── test/
│   └── platformio.ini
│
├── integration-tests/
│   ├── README.md
│   ├── app-backend/
│   ├── app-firmware/
│   ├── system-tests/
│   └── test-data/
│
└── .github/
    ├── workflows/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

**Note:** This is the proposed repository structure. Some directories and configuration files will be created during implementation. The exact technologies and folder arrangements will be finalised by the development team.

---

## 🛠️ Proposed Technology Stack

The following technologies are potential choices for implementation and are subject to team agreement.

| Component | Proposed Technologies |
|---|---|
| Team Website | React, TypeScript, HTML, CSS |
| Mobile Application | Flutter, Dart |
| Backend | Java, Spring Boot |
| Firmware | C++, ESP32 |
| Version Control | Git, GitHub |
| API Testing | Postman |
| Mobile Testing | Flutter Test |
| Backend Testing | JUnit |
| Firmware Development | PlatformIO |
| Project Management | Jira / GitHub Projects |

---

## 🔗 System Integration

The project contains several components that must work together to deliver the complete Smart Tikirilia experience.

- The mobile application provides the user interface and doll interaction features.
- The firmware controls the doll's electronic components and responds to sensor and NFC interactions.
- The backend manages application information, travel records, destination unlocking, and other server-side functionality.
- The team website presents the project and its development team.

Communication methods and integration approaches will be defined during system design.

---

## 🧪 Testing Strategy

Testing will be performed throughout the development process to ensure that individual components and the complete system function correctly.

| Testing Type | Purpose |
|---|---|
| Unit Testing | Test individual functions and components. |
| UI Testing | Verify website and mobile application interfaces. |
| API Testing | Verify backend endpoints and responses. |
| Firmware Testing | Test sensor, NFC, audio, and hardware-control functionality. |
| Integration Testing | Verify communication between the application, backend, and doll. |
| System Testing | Test the complete integrated Smart Tikirilia system. |
| Usability Testing | Evaluate the experience for intended users. |

---

## 👥 Team Collaboration

The project is developed collaboratively using Git and GitHub.

**Development workflow:**

1. Assign tasks using the agreed project management board.
2. Create feature branches for development tasks.
3. Implement and test changes.
4. Commit changes using meaningful commit messages.
5. Push feature branches to GitHub.
6. Create Pull Requests for code review.
7. Merge reviewed changes into the main branch.

**Branch naming examples:**

```text
main
feature/team-website
feature/teaching-mode
feature/journal
feature/nfc-detection
feature/doll-audio
feature/destination-unlocking
bugfix/sensor-response
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/smart-tikirilia.git
```

### 2. Navigate to the Project

```bash
cd smart-tikirilia
```

### 3. Set Up Individual Components

Each component has its own README file containing installation, configuration, and execution instructions.

- `team-website/README.md`
- `mobile-app/README.md`
- `backend/README.md`
- `firmware/README.md`
- `integration-tests/README.md`

Follow the relevant README before developing or running a component.

---

## 📚 Project Documentation

Additional project documentation is maintained in the `docs/` directory.

| Document | Description |
|---|---|
| Client Brief | Original project requirements and objectives. |
| Requirements | Functional and non-functional requirements. |
| System Architecture | Overall system design and component interactions. |
| Database Design | Proposed data models and database structure. |
| API Documentation | Backend API specifications. |
| Team Working Agreement | Team roles, responsibilities, and collaboration rules. |
| Product Backlog | Prioritised project features and tasks. |
| Release Roadmap | Planned development stages and milestones. |

---

## 📌 Project Status

**Current Status:** Planning and Initial Development Setup

The project will be developed incrementally, with progress tracked through the team's agreed Agile framework and project management board.

---

## 📄 License

Developed for academic coursework purposes. Licensing arrangements will be determined by the project team.

---

**Smart Tikirilia 1.0**  
*Discover Sri Lanka Through Culture, Stories, and Interactive Experiences.*
