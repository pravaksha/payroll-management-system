# 📑 Payroll Management System

This project is a **Payroll Management System** built using **Python**, **Tkinter** for the GUI, and **PostgreSQL** for secure data storage.  
It allows an employer to calculate gross pay, tax, pension, student loan, NI payments, and deductions, and store or update employee payroll records in a database.

---

## 📌 Features

✅ User-friendly Payroll Management UI  
✅ CRUD operations (Create, Read, Update, Delete) with PostgreSQL  
✅ Built-in calculator for quick computations  
✅ Dynamic payroll calculations: gross pay, deductions, net pay  
✅ View all payroll records in a table  
✅ Integrated notepad for notes within the app  
✅ Modern theme using **sv-ttk**

---

## ⚙️ Technologies Used

- **Python 3.12**
- **Tkinter**
- **sv-ttk** (modern Tkinter theming)
- **PostgreSQL**
- **psycopg2** (Python PostgreSQL adapter)

---

## 📂 Project Structure

```
.
├── main.py           # Main Python script
├── README.md         # Project documentation
├── 1.png             # Screenshot - Payroll System Tab
├── 2.png             # Screenshot - View Payroll Tab
├── 3.png             # Screenshot - Notes Tab
```

---

## 🔑 Prerequisites

1️⃣ **Python 3.12** installed.  
2️⃣ **PostgreSQL** installed with a database created.

---

## 🗂️ Database Setup

Before running the project, set up the PostgreSQL database:

```sql
CREATE DATABASE payroll;

CREATE TABLE payment (
    ref VARCHAR(255),
    fullname VARCHAR(255),
    address VARCHAR(255),
    employername VARCHAR(255),
    cityweighting VARCHAR(255),
    basicsalary VARCHAR(255),
    overtime VARCHAR(255),
    grosspay VARCHAR(255),
    tax VARCHAR(255),
    pension VARCHAR(255),
    nipayment VARCHAR(255),
    deductions VARCHAR(255),
    postcode VARCHAR(255),
    gender VARCHAR(255),
    payday VARCHAR(255),
    taxperiod VARCHAR(255),
    taxcode VARCHAR(255),
    ninumber VARCHAR(255),
    netpay VARCHAR(255)
);
```

---

## 🏃‍♂️ How to Run

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/yourusername/payroll-management-system.git
cd payroll-management-system
```

2️⃣ **Create & activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate   # Windows
```

3️⃣ **Install dependencies:**

```bash
pip install psycopg2-binary sv-ttk
```

4️⃣ **Update database credentials:**  
In `main.py`, update:

```python
conn = psycopg2.connect(database="payroll", user="postgres", password="your_password", host="localhost", port="5432")
```

with your PostgreSQL credentials.

5️⃣ **Run the application:**

```bash
python main.py
```

---

## 📸 Screenshots

| Payroll System | View Payroll | Notes |
|---|---|---|
| ![Payroll System](1.png) | ![View Payroll](2.png) | ![Notes](3.png) |

---

## 🎓 What this Project Demonstrates

- **Python GUI development (Tkinter, sv-ttk)**  
- **SQL database integration (PostgreSQL)**  
- **Data parsing & CRUD operations**  
- **Basic statistical computations for payroll**  
- **Clean code structure and modular design**

---

## 📧 Contact

For any questions or suggestions, feel free to reach out.  
Happy Coding! 🚀

---

## ✅ License

This project is for educational purposes only.

---

## ✅ Note for Internship Submission

This project serves as a project reference for demonstrating skills in:
- Python
- SQL
- Data parsing
- Statistics
- Basic ML-ready structured data handling
