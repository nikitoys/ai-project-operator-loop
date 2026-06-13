# Project Operation Profile — Task Tracker

Status: Draft

## Purpose

This file defines surface-level operating preferences for AI_Development_System inside the Task Tracker example project.

It is for behavior defaults, not product requirements or implementation scope.

## Human Interaction

Human Owner Language: English
Answer Language: English
Answer Detail Level: Concise by default; expand when asked.
Prompt Language: English

## Verification Defaults

Default Verification Mode: FAST_VALIDATION
Default Verification Budget: 120 sec
Allowed Slow Checks: false
Runtime Tracking: enabled
Browser Checks: explicit request only
Visual QA: explicit request only
Full Checks: explicit request only
Release Checks: explicit request only

## Permissions

Can Modify Application Code: only with approved task
Can Modify AI_PROJECT: planning, state, prompts, verification policy or project control tasks only
Can Modify AI_Development_System: system update, synchronization or evolution tasks only
Can Install Dependencies: explicit approval only
Can Commit: explicit request only
Can Push / Create PR: explicit request only

## Project Layout

Target App Directory: task-tracker-app
Project Control Directory: AI_PROJECT/
AI System Directory: AI_Development_System/

Application Code Paths:
- task-tracker-app/

Read Only Paths:
- secrets/
- production config

## Review Defaults

Review Required: true
QA Required: when behavior changes or acceptance criteria require it
Blocking Severity: Critical, Major
Advisory Failures: allowed only when reported

## Local Exceptions

None

## Rules

- This profile provides defaults only.
- It does not authorize execution without an approved task or prompt package.
- It may restrict global AI Development System rules, but must not weaken them.
- If this profile conflicts with global safety rules, report the conflict and stop.
- If this profile conflicts with specialized local control files, report project-control drift.
