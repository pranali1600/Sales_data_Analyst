# etl/scheduler.py
import schedule 
import time 
import subprocess
from datetime import datetime
import os

def run_fetch_script():

    """Run fetch_data.py script automatically"""
    print("\n-------------------------------------")
    print("⏰ Fetch job started at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    try:
        # Run fetch_data.py as a separate process
        script_path = os.path.join(os.path.dirname(__file__), "fetch_data.py")
        subprocess.run(["python", script_path], check=True)
      
        print("✅ Fetch job completed successfully!")
    except subprocess.CalledProcessError as e:
        print("❌ Error while running fetch_data.py:", e)
    
    print("-------------------------------------\n")

# -----------------------------
# Schedule the job
# -----------------------------
schedule.every(1).minutes.do(run_fetch_script)
# Alternatives:
# schedule.every().day.at("09:00").do(run_fetch_script)
# schedule.every().hour.do(run_fetch_script)

print("🚀 Scheduler started... Press Ctrl+C to stop.\n")


while True:
    schedule.run_pending()
    time.sleep(60)  
