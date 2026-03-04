import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

report_path = f"reports/report_{timestamp}.html"

os.system(f"python -m pytest tests --html={report_path} --self-contained-html")