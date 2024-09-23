Outage of Nursing Management App Attendance Feature

Issue Summary
Duration: The outage lasted for 2 hours, from 11:00 AM to 1:00 PM UTC on September 20th, 2024.
Impact: The biometric attendance feature became unavailable, affecting 85% of users. Nursing school administrators and instructors were unable to log student attendance. Users experienced timeouts and errors when trying to capture fingerprints, disrupting normal class check-ins.
Root Cause: The root cause was a misconfigured database query that led to excessive load times, compounded by a memory leak in the biometric device integration module.

Timeline
11:00 AM: Issue detected by automatic system monitoring alerts showing increasing API response times.
11:05 AM: The engineering team was notified via Slack after receiving multiple error logs from the biometric system.
11:10 AM: Initial investigation focused on the backend API serving attendance data.
11:30 AM: Assumption made that the API gateway configuration was the issue due to recent changes in traffic management, but no irregularities were found.
11:45 AM: Escalation to the database and biometric integration team after realizing the problem persisted beyond the API layer.
12:00 PM: Misleading investigation into a suspected timeout issue between the biometric device and the server.
12:30 PM: Discovery of a memory leak in the biometric SDK integration and inefficient database queries causing excessive load on the server.
12:45 PM: Patch applied to fix the SQL query and restart the affected services.
1:00 PM: Biometric attendance system fully restored and performance normalized.

Root Cause and Resolution
Root Cause: The primary issue was a poorly optimized SQL query used in the biometric attendance feature. The query retrieved unnecessary data, causing it to take longer to execute under heavy load. Additionally, a memory leak in the biometric SDK integration module gradually consumed available system resources, slowing the entire service.
Resolution: The inefficient query was rewritten to only retrieve the necessary fields, reducing execution time by 80%. A memory leak fix was applied by refactoring the biometric device interaction module to handle multiple biometric scans without excessive memory consumption. After these patches were deployed, the system was restarted, and the attendance feature resumed normal operations.

Corrective and Preventative Measures
Areas of Improvement:
Database Query Optimization: Improve query performance for high-traffic scenarios to prevent future slowdowns.
SDK Integration Testing: Strengthen integration testing with biometric devices to catch memory leaks before production.
Alert System Enhancement: Enhance real-time alerting for abnormal memory consumption and slow database queries.
Load Testing: Perform more thorough load testing on biometric integrations to ensure the system scales during peak usage times.
Action Items:
Optimize all SQL queries in the biometric attendance module.
Refactor the biometric device SDK integration to prevent memory leaks and improve efficiency.
Add monitoring on database response times and memory consumption.
Implement end-to-end load testing for the attendance module under simulated peak conditions.
Update the incident response playbook with biometric-specific debugging steps.

By addressing the root cause, the Nursing Management App's performance has been stabilized, and preventative measures are being put in place to avoid similar outages in the future.
