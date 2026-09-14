import pandas as pd
import sqlite3

# 1. Load the raw data
df = pd.read_csv('../data/production_orders.csv')

# 2. Define the risk scoring logic
def calculate_risk(row):
    score = 0
    primary_reason = []

    if row['Inspection_Status'] == 'Failed':
        score += 40
        primary_reason.append('Inspection Failed')
        
    if row['Material_Status'] == 'Delayed':
        score += 30
        primary_reason.append('Material Delayed')
        
    if row['Approval_Status'] == 'Overdue' or row['Approval_Status'] == 'Pending':
        score += 25
        primary_reason.append('Approval Pending/Overdue')
        
    if row['Packaging_Status'] == 'Delayed':
        score += 15
        primary_reason.append('Packaging Delayed')
        
    if row['Shipment_Status'] == 'Unbooked':
        score += 10
        primary_reason.append('Shipment Unbooked')

    return score, " + ".join(primary_reason) if primary_reason else "None"

# Apply the logic to our data
df[['Risk_Score', 'Risk_Reason']] = df.apply(lambda row: pd.Series(calculate_risk(row)), axis=1)

# 3. Categorize the risk levels
def categorize_risk(score):
    if score >= 80: return 'CRITICAL'
    if score >= 50: return 'HIGH'
    if score >= 25: return 'MEDIUM'
    return 'LOW'

df['Risk_Level'] = df['Risk_Score'].apply(categorize_risk)

# 4. Save the Action Queue to a new CSV (for the dashboard)
action_queue = df[df['Risk_Level'].isin(['CRITICAL', 'HIGH'])].sort_values(by='Risk_Score', ascending=False)
action_queue.to_csv('../outputs/prioritized_action_queue.csv', index=False)

# 5. Create the SQLite Database and load all data into it
conn = sqlite3.connect('../database/production_control.db')
df.to_sql('production_orders', conn, if_exists='replace', index=False)
conn.close()

print("Risk engine executed. Database and action queue generated.")
