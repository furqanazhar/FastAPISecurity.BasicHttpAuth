import json, os, secrets


def convert_response_to_json(data):
    return json.loads(json.dumps(data, default=str, indent=2))

def validate_credentials(username, password):
    key = os.getenv('fastApiUser')
    value = os.getenv('fastApiPassword')
    print('key', key)
    print('value', value)
    correct_username = secrets.compare_digest(username, key)
    correct_password = secrets.compare_digest(password, value)
    if not (correct_username and correct_password):
        return False
    else:
        return True
