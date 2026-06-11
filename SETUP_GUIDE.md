# Employee Management System - Quick Setup Guide

Simple step-by-step guide to clone and run this Django application on any machine.

## 📋 Prerequisites

Install these before starting:

1. **Python 3.8+** - [Download](https://www.python.org/downloads/)
2. **MySQL** - [Download](https://dev.mysql.com/downloads/mysql/) or use [XAMPP](https://www.apachefriends.org/)
3. **Git** - [Download](https://git-scm.com/downloads)

## 🚀 Quick Start (5 Minutes)

### Step 1: Clone the Repository

```bash
# Clone the project
git clone https://github.com/suneeshms96/employee-portal.git

# Navigate into folder
cd employee-portal
```

### Step 2: Install Dependencies

```bash
# Install required packages
pip install Django==4.0.4
pip install mysqlclient
pip install numpy pandas scikit-learn tensorflow
```

Or use requirements file if available:

```bash
pip install -r requirements.txt
```

### Step 3: Setup Database

**Option A: Using MySQL Command Line**

```bash
# Login to MySQL
mysql -u root -p

# Create database
CREATE DATABASE employee;
EXIT;

# Import database (if SQL file provided)
mysql -u root -p employee < "employee (2).sql"
```

**Option B: Using phpMyAdmin (XAMPP)**

1. Start XAMPP → Start MySQL
2. Open http://localhost/phpmyadmin
3. Create new database: `employee`
4. Import SQL file if available

### Step 4: Configure Database Connection

Edit `employee/settings.py` - Find the DATABASES section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',  # Change this
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### Step 5: Run the Application

```bash
# Run migrations (if needed)
python manage.py migrate

# Start the server
python manage.py runserver
```

### Step 6: Access the Application

Open your browser and go to:

- **Application**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## 🖥️ Platform-Specific Instructions

### Windows

```cmd
# Clone
git clone https://github.com/suneeshms96/employee-portal.git
cd employee-portal

# Install
pip install Django==4.0.4 mysqlclient numpy pandas scikit-learn tensorflow

# Configure database in employee/settings.py

# Run
python manage.py runserver
```

### macOS/Linux

```bash
# Clone
git clone https://github.com/suneeshms96/employee-portal.git
cd employee-portal

# Install
pip3 install Django==4.0.4 mysqlclient numpy pandas scikit-learn tensorflow

# Configure database in employee/settings.py

# Run
python3 manage.py runserver
```

## 📁 Project Structure

```
employee-portal/
├── employee/              # Main project settings
│   ├── settings.py       # Configure database here
│   ├── urls.py           # URL routing
│   └── wsgi.py
├── employeeapp/          # Main application
│   ├── views.py          # Application logic
│   ├── models.py         # Database models
│   ├── templates/        # HTML files
│   └── static/           # CSS, JS, images
├── manage.py             # Django management
└── employee (2).sql      # Database schema
```

## 🔧 Common Issues & Solutions

### Issue 1: "No module named 'MySQLdb'"

```bash
# Solution:
pip install mysqlclient

# If that fails on Windows:
pip install pymysql
# Then add to employee/__init__.py:
import pymysql
pymysql.install_as_MySQLdb()
```

### Issue 2: "Access denied for user 'root'"

```python
# Solution: Update password in employee/settings.py
'PASSWORD': 'your_actual_mysql_password',
```

### Issue 3: "Port 8000 already in use"

```bash
# Solution: Use different port
python manage.py runserver 8080
```

### Issue 4: "Table doesn't exist"

```bash
# Solution: Run migrations or import SQL file
python manage.py migrate
# OR
mysql -u root -p employee < "employee (2).sql"
```

### Issue 5: Static files not loading

```bash
# Solution: Collect static files
python manage.py collectstatic
```

## 📦 Required Python Packages

```
Django==4.0.4
mysqlclient==2.1.1
numpy==1.23.5
pandas==1.5.3
scikit-learn==1.2.2
tensorflow==2.12.0
```

## 🎯 Features

- Employee Management
- Department Management
- Task Assignment
- Work Allocation
- Employee Surveys
- Stress Detection
- Attrition Prediction (ML)
- Emotion Recognition

## 👥 Default Login

After setting up, you may need to create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create admin account.

## 🌐 Accessing from Other Devices

To access from other devices on same network:

1. Find your IP address:

   ```bash
   # Windows
   ipconfig

   # Mac/Linux
   ifconfig
   ```

2. Run server on all interfaces:

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. Access from other device:
   ```
   http://YOUR_IP_ADDRESS:8000
   ```

## 📝 Quick Reference

### Start Application

```bash
cd employee-portal
python manage.py runserver
```

### Stop Application

Press `Ctrl + C` in terminal

### Reset Database

```bash
python manage.py flush
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Check for Errors

```bash
python manage.py check
```

## 🔄 Updating the Application

```bash
# Navigate to project
cd employee-portal

# Pull latest changes
git pull origin main

# Install any new dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Restart server
python manage.py runserver
```

## 💡 Tips

1. **Always activate virtual environment** (if using one)
2. **Keep MySQL running** before starting Django
3. **Check database credentials** in settings.py
4. **Use Python 3.8 or higher**
5. **Don't commit database passwords** to Git

## 📞 Need Help?

Common commands to check your setup:

```bash
# Check Python version
python --version

# Check Django installation
python -m django --version

# Check MySQL connection
mysql -u root -p

# List installed packages
pip list
```

## ✅ Setup Checklist

- [ ] Python 3.8+ installed
- [ ] MySQL installed and running
- [ ] Git installed
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] Database created
- [ ] Database credentials configured in settings.py
- [ ] Migrations run (if needed)
- [ ] Server starts without errors
- [ ] Can access http://localhost:8000

## 🎓 For Development

If you want to modify the code:

1. Make changes to files
2. Test locally with `python manage.py runserver`
3. Commit changes: `git add .` → `git commit -m "message"`
4. Push to GitHub: `git push origin main`

---

**That's it!** Your Employee Management System should now be running.

For any issues, check the troubleshooting section above or verify all prerequisites are installed correctly.

**Repository**: https://github.com/suneeshms96/employee-portal
