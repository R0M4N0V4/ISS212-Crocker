# Simulated database containing user information
database = {
    'users': [
        {'username': 'john_doe', 'role': 'admin', 'email': 'john@example.com', 'website': 'CSScripts.example.com'},
        {'username': 'alice_smith', 'role': 'user', 'email': 'alice@example.com', 'website': 'example-CSScripts.com'},
        {'username': 'guest', 'role': 'guest', 'email': 'guest@CSScripts.com', 'website': 'otherwebsite.com'},
        {'username': 'bob_carter', 'role': 'user', 'email': 'bob@CSScripts.com', 'website': 'CSScripts.org'},
        # Add more user entries with CSScripts-related data here
    ]
}

# Simulated log data containing access information
log_data = [
    {'timestamp': '2023-11-14 08:23:17', 'username': 'john_doe', 'action': 'login', 'status': 'success', 'ip': '192.168.1.100'},
    {'timestamp': '2023-11-14 08:45:21', 'username': 'admin', 'action': 'access_denied', 'resource': '/admin_panel', 'ip': '192.168.1.102'},
    {'timestamp': '2023-11-14 09:30:12', 'username': 'guest', 'action': 'login', 'status': 'failed', 'ip': '123.456.789.10'},
    {'timestamp': '2023-11-14 10:20:30', 'username': 'bob_carter', 'action': 'login', 'status': 'success', 'ip': '203.0.113.5'},
    {'timestamp': '2023-11-14 11:00:00', 'username': 'alice_smith', 'action': 'accessed_data', 'status': 'success', 'ip': '192.168.1.103'},

]

# Function to correlate data based on user input
def correlate_data_based_on_user_input(database, log_data):
    user_input = input("Enter username to correlate data: ")
    correlated_results = []
    for log_entry in log_data:
        if log_entry['username'] == user_input:
            for user_info in database['users']:
                if log_entry['username'] == user_info['username']:
                    correlation_result = {
                        'timestamp': log_entry['timestamp'],
                        'username': log_entry['username'],
                        'action': log_entry['action'],
                        'status': log_entry['status'],
                        'ip': log_entry['ip'],
                        'role': user_info['role'],
                        'email': user_info['email'],
                        'website': user_info['website']
                    }
                    correlated_results.append(correlation_result)
    return correlated_results

# Perform correlation based on user input
correlated_data = correlate_data_based_on_user_input(database, log_data)

# Display correlated results
if correlated_data:
    for entry in correlated_data:
        print("Correlated data for user:")
        print(entry)
else:
    print("No data found for the entered username.")
