import mysql.connector
import requests
import csv
from datetime import datetime
import time
#Update function

# Add this function near the top of your script (after imports)
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyHTTPMonitor/1.0)"
}

def get_status(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10, headers=headers)
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {url} (attempt {attempt + 1}): {e}")
            time.sleep(1)
    return 0

# Connect to database etc.
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Applesauce1234',
    database='http_monitoring'
)

cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT url, description FROM urls")
urls = cursor.fetchall()

report_rows = []

for row in urls:
    url = row['url']
    desc = row['description']

    # Use the new function here
    status = get_status(url)

    # Update database and build report as before
    cursor.execute("UPDATE urls SET http_status = %s WHERE url = %s", (status, url))
    cursor.execute("SELECT description FROM http_status WHERE status_code = %s", (status,))
    status_desc_row = cursor.fetchone()
    status_desc = status_desc_row['description'] if status_desc_row else 'Unknown'
    report_rows.append([url, desc, status, status_desc])

conn.commit()
cursor.close()
conn.close()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"http_report_{timestamp}.csv"

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Description', 'HTTP Status', 'Status Description'])
    writer.writerows(report_rows)

print(f"Report saved to {filename}")
