# Task Scheduler Optimization System

## Overview

The Task Scheduler Optimization System is a Data Structures and Algorithms (DSA) project that optimizes task execution order based on priority, deadlines, execution time, and resource constraints.

The system demonstrates real-world scheduling techniques used in:

* Operating Systems
* CPU Scheduling
* Cloud Computing
* Project Management Tools
* Workflow Automation Systems

---

## Features

* Task Loading from CSV Files
* Data Validation
* Priority-Based Scheduling
* Deadline-Based Scheduling
* Heap (Priority Queue) Scheduling
* Greedy Optimization Algorithm
* Missed Deadline Detection
* Profit/Importance Calculation
* Performance Metrics
* TXT Report Generation
* CSV Export
* Automated Unit Testing using pytest

---

## Technologies Used

* Python
* CSV Processing
* Heap Queue (heapq)
* Pytest
* Object-Oriented Programming

---

## Project Structure

Task-Scheduler-Optimization-System/

├── data/

├── outputs/

├── src/

├── tests/

├── images/

├── main.py

├── requirements.txt

├── README.md

└── pytest.ini

---

## DSA Concepts Used

### Sorting Algorithms

* Priority Sorting
* Deadline Sorting
* Multi-Key Sorting

### Heap (Priority Queue)

Efficient task selection based on highest priority.

Time Complexity:

Insertion: O(log n)

Deletion: O(log n)

### Greedy Algorithm

Chooses the best available task at each step to maximize overall profit and task completion.

---

## Output

The system generates:

* Optimized Task Schedule
* Execution Timeline
* Missed Tasks Report
* Total Profit
* Performance Metrics
* TXT Report
* CSV Report

---

## Running the Project

Install dependencies:

pip install -r requirements.txt

Run:

python main.py

Run tests:

pytest

---

## Sample Result

Completed Tasks: 4

Missed Tasks: 0

Completion Rate: 100%

Total Profit: 1100

---

## Future Enhancements

* GUI Dashboard
* Streamlit Integration
* Gantt Chart Visualization
* Resource Allocation Optimization
* Multiple Scheduling Algorithms Comparison
* Database Integration

---

## Author

Hardik Hipparagi
