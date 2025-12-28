# uk-healthcare-ai-systems
UK Healthcare AI Support Systems
Overview

This repository contains anonymised, non-clinical implementations of AI-enabled systems developed independently by Hitendrasinh Rathod, Director & Founder of Akshar AI Ltd.

The systems are designed to support operational efficiency, workflow optimisation, and patient navigation within UK healthcare contexts. They are intended as decision-support and workflow-support tools, not as autonomous clinical or diagnostic systems.

This repository is provided solely for technical verification and professional assessment purposes, including review by authorised assessors for UK Global Talent or Innovator Founder routes.

Key Principles

All systems in this repository have been developed in accordance with the following principles:

No autonomous clinical decision-making

Mandatory human oversight (“human-in-the-loop”)

Use of anonymised or simulated data only

No integration with live NHS or production healthcare systems

Alignment with UK data protection and responsible AI principles

Clear documentation, testing artefacts, and version control history

Repository Structure
uk-healthcare-ai-systems/
├── diagnostic-reporting-support/
│   ├── backend/
│   ├── models/
│   ├── docs/
│   └── tests/
│
├── healthcare-navigation-assistant/
│   ├── backend/
│   ├── frontend/
│   ├── docs/
│   └── tests/
│
├── primary-care-support-systems/
│   ├── medication-adherence-tool/
│   ├── administrative-automation-agent/
│   ├── docs/
│   └── tests/
│
├── docs/
│   ├── architecture-overview.md
│   ├── data-governance.md
│   └── system-design-notes.md
│
├── tests/
│   └── shared-testing-utilities/
│
└── README.md


Each project folder corresponds directly to a section in the accompanying technical report.

Project Summaries
1. AI-Assisted Diagnostic Reporting Support (Ongoing)

Purpose:
To support clinicians by reducing repetitive drafting tasks in diagnostic imaging workflows while maintaining full professional accountability.

Key Characteristics:

Secure image ingestion and anonymisation pipeline

Vision Transformer–based feature extraction highlighting regions of interest

Language-model-assisted structured draft report generation

Mandatory human review and sign-off

No autonomous diagnostic output

Status:
Core modules implemented and internally tested using anonymised and simulated data.

2. Digital Healthcare Navigation Assistant (Completed)

Purpose:
To assist patients in navigating appropriate healthcare services by providing structured, rule-based guidance.

Key Characteristics:

Symptom-to-service navigation logic (non-diagnostic)

Integration with UK healthcare service directories

Accessibility considerations (WCAG 2.1 Level AA)

Designed to improve confidence and reduce inappropriate service usage

Status:
Completed functional implementation with validation scenarios using simulated user data.

3. Primary Care Support Systems (Completed)

Components:

a) Medication Adherence Support Tool

Reminder scheduling and adherence tracking

Designed for complex prescription scenarios

Validated using simulated patient data

b) Administrative Automation Agent

Automation of routine non-clinical tasks (e.g. reminders, form handling)

Internal MVP developed and evaluated

Focused on reducing administrative burden

Status:
Completed implementations with internal evaluation artefacts.

Data and Privacy Statement

No patient-identifiable data is included in this repository

All datasets are anonymised or synthetically generated

No live NHS systems or production healthcare environments are accessed

Code is provided for demonstration, validation, and assessment purposes only

Intended Use

This repository is intended for:

Technical verification of system architecture and implementation

Review of AI integration and software engineering practices

Assessment of independent authorship and development progression

It is not intended for:

Clinical deployment

Diagnostic use

Direct patient interaction in live environments

Access and Permissions

This repository is maintained as a private repository.

Access is granted on a read-only basis

Limited to authorised reviewers and assessors

No modification or redistribution is permitted without explicit consent

Authorship

All systems in this repository were:

Conceived

Architected

Implemented

Documented

by Hitendrasinh Rathod.

Commit history and repository metadata provide verifiable evidence of sustained individual technical contribution.

Contact

Akshar AI Ltd
Website: https://aksharaiworks.com

Email: hello@aksharaiworks.com

Disclaimer

The software and documentation contained in this repository are provided for professional review and assessment purposes only. They do not constitute medical advice, clinical decision-making tools, or deployed healthcare products.
