QA Automation Framework

End-to-End Test Automation Framework built using Python, Selenium, PyTest, and Page Object Model (POM).
This framework automates user flows, validates functionality, and generates HTML execution reports.

🚀 Tech Stack

🐍 Python

🌐 Selenium WebDriver

🧪 PyTest

📄 PyTest-HTML Report

🏗 Page Object Model (POM)

📂 Project Structure
qa-automation-framework/
│
├── pages/                # Page Object classes
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/                # Test cases
│   ├── test_login.py
│
├── reports/              # HTML test reports
│
├── conftest.py           # PyTest fixtures
├── requirements.txt      # Dependencies
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-link>
cd qa-automation-framework
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run Tests

Run all test cases:

pytest

Run with HTML Report:

pytest --html=reports/report.html

After execution, open:

reports/report.html
🏗 Framework Design
🔹 Page Object Model (POM)

Each page has a separate class

Locators and actions are separated from test logic

Improves reusability and maintainability

🔹 PyTest Fixtures

WebDriver setup & teardown handled in conftest.py

Supports scalability and parallel execution

✅ Features

✔ End-to-End User Flow Automation
✔ Assertions & Validations
✔ Scalable Structure
✔ Reusable Page Objects
✔ HTML Reporting
✔ Clean & Maintainable Code

📌 Author

Suraj G