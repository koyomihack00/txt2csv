import xml.etree.ElementTree as ET
import pandas as pd

# Define columns
cols = ["SSL Status", "Years", "ProviderOrderID", "IsExpiredYN", "ActivationExpireDate", "ExpireDate", "PurchaseDate", "SSLType", "HostName", "CertificateID"]
rows = []

# Sample XML data (replace with your actual XML lines)
xml_data = '''
<root>
Your text
</root>
'''

# Parse XML lines
root = ET.fromstring(xml_data)
for elem in root:
    row = {col: elem.get(col) for col in cols}
    rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows, columns=cols)

# Save to CSV
df.to_csv('NC_SSL.csv', index=False)
print("CSV file saved as 'NC_SSL.csv'")
