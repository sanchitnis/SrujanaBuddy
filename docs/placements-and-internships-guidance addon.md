# SYSTEM SPECIFICATION: SrujanaBuddy – Career Planning & Placement Module

## 1. EXECUTIVE SUMMARY & TARGET STATE

* **Context**:  
  SrujanaBuddy Career Planning & Placement Module addresses fragmented student career readiness, lack of structured placement workflows, and absence of AI-driven insights for employability.

* **Core Objective**:  
  Build an AI-native platform that integrates **career discovery, skill mapping, training, assessment, and placement automation**, enabling outcome-driven employability and data-driven institutional decision-making.

* **Target State**:  
  A unified digital ecosystem where:
  * Students progress from **career discovery → skill acquisition → assessment → placement**
  * Faculty and administrators access **real-time analytics for curriculum and placements**
  * Recruiters engage through **automated campus hiring pipelines**

* **Agent Operational Rule**:  
  Do not write code outside the boundaries defined in this document. Prioritize type safety and test coverage.

## 2. SYSTEM ARCHITECTURE & SCOPE

* **Stack**:
  * Frontend: Next.js (student, faculty, recruiter portals)
  * Backend: FastAPI (AI services + orchestration layer)
  * Database: PostgreSQL (relational + structured skill graph)
  * AI Services: Python microservices (resume parsing, interview AI scoring)
  * Analytics: Apache Superset / Metabase

* **Deployment**:
  * Dockerized microservices
  * AWS ECS / Kubernetes cluster
  * CDN via Vercel for frontend

* **Security Requirements**:
  * JWT Authentication
  * Role-Based Access Control (RBAC): Student / Faculty / Admin / Recruiter
  * Data encryption at rest and in transit
  * Audit logging for placement decisions

* **System Scope (Derived from email)**:
  * AI Interview & assessment platforms
  * Resume copilot and ATS optimization
  * LMS + placement management
  * Career intelligence analytics (skills taxonomy, job tracking)

## 3. DATA ARCHITECTURE & API SCHEMA

### AI Agent Instruction

Implement strict runtime validation matching schema structures.

### 3.1 Primary Entity Schema

#### 3.1.1 Student Career Profile

```json
{
  "$schema": "https://json-schema.org",
  "title": "StudentProfile",
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "studentName": { "type": "string", "maxLength": 100 },
    "program": { "type": "string" },
    "skills": {
      "type": "array",
      "items": { "type": "string" }
    },
    "careerGoal": { "type": "string" },
    "resumeScore": { "type": "number" },
    "placementStatus": { "type": "string", "enum": ["unplaced", "in-process", "placed"] },
    "createdAt": { "type": "string", "format": "date-time" }
  },
  "required": ["id", "studentName", "skills", "placementStatus"]
}
```

#### 3.1.2 Job Opportunity Entity

```json
{
  "title": "JobOpportunity",
  "type": "object",
  "properties": {
    "jobId": { "type": "string", "format": "uuid" },
    "companyName": { "type": "string" },
    "role": { "type": "string" },
    "requiredSkills": {
      "type": "array",
      "items": { "type": "string" }
    },
    "ctcRange": { "type": "string" },
    "status": { "type": "string", "enum": ["open", "closed"] }
  },
  "required": ["jobId", "companyName", "role"]
}
```

#### 3.1.3 Placement Process Entity

```json
{
  "title": "PlacementProcess",
  "type": "object",
  "properties": {
    "processId": { "type": "string", "format": "uuid" },
    "studentId": { "type": "string" },
    "jobId": { "type": "string" },
    "stage": {
      "type": "string",
      "enum": ["applied", "assessment", "interview", "offer"]
    },
    "aiInterviewScore": { "type": "number" },
    "status": { "type": "string", "enum": ["active", "rejected", "selected"] }
  },
  "required": ["processId", "studentId", "jobId", "stage"]
}
```

### 3.2 Endpoint Registry

| Method | Path                          | Payload            | Response Code | Description               |
| ------ | ----------------------------- | ------------------ | ------------- | ------------------------- |
| POST   | /api/v1/student               | StudentProfile     | 201           | Create student profile    |
| GET    | /api/v1/student/:id           | None               | 200           | Fetch student profile     |
| POST   | /api/v1/job                   | JobOpportunity     | 201           | Create job posting        |
| GET    | /api/v1/jobs                  | None               | 200           | List jobs                 |
| POST   | /api/v1/apply                 | PlacementProcess   | 201           | Apply for job             |
| GET    | /api/v1/placements/:studentId | None               | 200           | Track placement pipeline  |
| POST   | /api/v1/interview/score       | Assessment payload | 200           | Store AI interview result |

## 4. FUNCTIONAL CAPABILITIES (ACCEPTANCE CRITERIA)

### Feature 1: Career Discovery & Guidance (IKIGAI-based)

(grounded in email mention of career discovery tools)

```
Scenario: Student identifies career path
Given a student logs into the system
When the student completes career discovery assessment
Then the system should suggest 3–5 career paths
And map required skills for each path
```

### Feature 2: AI Resume Copilot

(derived from resume copilot capability)

```
Scenario: Resume optimization
Given a student uploads a resume
When the AI processes the document
Then the system should generate a score
And suggest improvements aligned to job roles
```

### Feature 3: Skill Gap Identification & LMS Mapping

(derived from LMS + skills taxonomy)

```
Scenario: Skill gap detection
Given a student profile and selected job role
When the system compares skills with job requirements
Then it should identify missing skills
And recommend learning modules
```

### Feature 4: AI Interview Preparation

(derived from AI interview tools)

```
Scenario: Mock interview evaluation
Given a student starts an AI interview session
When the student answers questions
Then the system should evaluate confidence, fluency, correctness
And return a detailed performance score
```

### Feature 5: Placement Workflow Automation

(derived from placement automation system)

```
Scenario: End-to-end placement tracking
Given a recruiter posts a job
When a student applies for the job
Then the system should track stages from application to offer
And update placement status in real time
```

### Feature 6: Career Intelligence Analytics

(derived from Nexus analytics)

```
Scenario: Institutional analytics dashboard
Given placement and skill data exists
When admin views dashboard
Then system should show trends in job roles, skills, placements
And enable curriculum insights
```

### Feature 7: Recruiter Engagement System

```
Scenario: Recruiter posts job
Given a recruiter is authenticated
When they submit job details
Then system publishes job to eligible students
And notifies matching candidates
```

## 5. REFACTORING & EXTENSION GUIDELINES

* **Style Guide**:
  * Modular microservices
  * Strict separation of career engine, placement engine, AI services

* **Dependencies**:
  * AI models only where required (resume parsing, interview scoring)
  * Avoid unnecessary third-party SDKs

* **Extensibility**:
  * Add global immersion programs / executive education modules (future integration aligned with email offerings)
  * Integrate with government skill mission frameworks

* **Error Handling**:
  * All AI service failures fallback to manual scoring
  * Placement failures logged with retry workflows
  * User messages must be clear and non-technical

