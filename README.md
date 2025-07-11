# 🏥 Hospital Management System

A comprehensive **Hospital Management System** built using **Python (Tkinter)** for the graphical user interface and **MySQL** for backend data management. This desktop application streamlines hospital operations by efficiently managing patient details, prescriptions, and medical records.

---

## ✅ Features

- ➕ Add, ✏️ update, ❌ delete, and 📄 view patient information.
- 💊 Manage and store prescription details.
- 🖥️ Interactive and user-friendly **Tkinter-based GUI**.
- 🗃️ Secure and structured data storage using **MySQL**.
- 🧾 Auto-generates and displays patient prescriptions.
## 🛠️ Tech Stack

- **Frontend**: Python with Tkinter
- **Backend**: MySQL
- **Database Connector**: `mysql-connector-python`

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library

### 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system
```

2. **Install Required Packages**

```bash
pip install mysql-connector-python
```

3. **Set Up the MySQL Database**

- Open MySQL and create a new database:

```sql
CREATE DATABASE hospital_db;
```

- Use the SQL script provided in the repository (`schema.sql` or similar) to create necessary tables.

4. **Configure Database Connection**

- Update your Python code with your MySQL username, password, and database name.

```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="hospital_db"
)
```

5. **Run the Application**

```bash
python main.py
```

---

## 📁 Project Structure

```
hospital-management-system/
├── main.py
├── db_config.py
├── requirements.txt
├── schema.sql
└── README.md
```

---



---

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance this project, feel free to fork the repo and submit a pull request. For major changes, open an issue first to discuss your ideas.
