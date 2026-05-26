# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
Define baseline requirements for an AI-powered timetable generation system.

### 1.2 Scope
The system creates conflict-free timetable drafts for learners by considering subjects, availability, and constraints.

## 2. Overall Description

### 2.1 Product Perspective
This project is an early scaffold with documentation and starter source code.

### 2.2 Users
- Students
- Instructors
- Administrators

### 2.3 Constraints
- Initial scaffold only (no optimization engine yet)
- Must remain easy to extend

## 3. Functional Requirements

- FR1: Accept input constraints (courses, time windows, blocked slots).
- FR2: Generate a timetable candidate.
- FR3: Detect and avoid overlapping class slots.
- FR4: Return machine-readable output for UI/API use.

## 4. Non-Functional Requirements

- NFR1: Readable, maintainable code structure.
- NFR2: Deterministic behavior for identical input.
- NFR3: Basic input validation for safety and correctness.

## 5. Future Enhancements

- AI ranking of timetable options.
- Preference-aware optimization.
- Calendar export (ICS/Google Calendar).
