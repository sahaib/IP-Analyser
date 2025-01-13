import requests
import json
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import pandas as pd

def get_ip_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        return {
            'ip': ip,
            'country': data.get('country', 'N/A'),
            'region': data.get('regionName', 'N/A'),
            'city': data.get('city', 'N/A'),
            'isp': data.get('isp', 'N/A'),
            'org': data.get('org', 'N/A'),
            'as': data.get('as', 'N/A')
        }
    except Exception as e:
        return {
            'ip': ip,
            'error': str(e)
        }

def analyze_ips(ip_list):
    # Get unique IPs
    unique_ips = list(set(ip_list))
    
    # Get info for each IP using threading for faster results
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(get_ip_info, unique_ips))
    
    # Convert to DataFrame for better visualization
    df = pd.DataFrame(results)
    
    # Basic statistics
    total_ips = len(ip_list)
    unique_ip_count = len(unique_ips)
    
    print(f"Total IPs: {total_ips}")
    print(f"Unique IPs: {unique_ip_count}")
    print("\nDetailed Information:")
    print(df.to_string())
    
    # Save to CSV
    df.to_csv('ip_analysis.csv', index=False)
    
# Your IP list
ips = [
"ip_list"
]

analyze_ips(ips)