# Student-Management-System-Inheritance-Python
A simple Python-based Student Management System using Object-Oriented Programming concepts like inheritance and file handling to manage student records, attendance, library details, and salary calculation.
# Student Management System (Python)

This project is a **Student Management System** built using **Python** and **Object-Oriented Programming (OOP)** concepts.  
It helps manage student details, attendance percentage, library records, salary calculation, and result generation.

---

## 🚀 Features

- Student marks input and percentage calculation
- Attendance percentage calculation
- Library book record entry
- Employee salary calculation based on attendance
- Result generation in `.txt` file
- Uses OOP concepts:
  - Classes & Objects
  - Inheritance
  - File Handling
  - Date & Time module

---

## 🧱 Classes Used

### 1. `Cal`
- Stores basic details (name, roll no, marks, days)
- Calculates attendance percentage
- Handles library book details

### 2. `Management (inherits Cal)`
- Calculates salary based on number of present days

### 3. `Student (inherits Management)`
- Takes student marks input
- Calculates total & percentage
- Generates result file (`rollno.txt`)

---

## 🛠 Technologies Used

- Python 3
- datetime module
- File handling

---

## 📂 Output

- Result is saved in a text file named as the student's **roll number**
- Example: `101.txt`

---

## ▶ How to Run

1. Install Python 3
2. Clone the repository
3. Run the file:
   ```bash
   python main.py
