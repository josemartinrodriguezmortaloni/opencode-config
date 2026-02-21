# Common Vulnerabilities

## SQL Injection

**Vulnerable:**
```python
query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)
```

**Secure:**
```python
cursor.execute(
    "SELECT * FROM users WHERE email = %s", 
    (email,)
)
```

## Command Injection

**Vulnerable:**
```python
os.system(f"convert {user_filename} output.pdf")
```

**Secure:**
```python
subprocess.run(
    ["convert", user_filename, "output.pdf"],
    check=True
)
```

## Path Traversal

**Vulnerable:**
```python
def get_file(filename: str) -> bytes:
    return open(f"/uploads/{filename}", "rb").read()
    # Attack: filename = "../etc/passwd"
```

**Secure:**
```python
def get_file(filename: str) -> bytes:
    base = Path("/uploads").resolve()
    target = (base / filename).resolve()
    
    if not target.is_relative_to(base):
        raise ValueError("Invalid path")
    
    return target.read_bytes()
```

## Unsafe Deserialization

**Vulnerable:**
```python
data = pickle.loads(user_data)  # Can execute arbitrary code
```

**Secure:**
```python
data = json.loads(user_data)  # Safe, data only
```

## SSRF (Server-Side Request Forgery)

**Vulnerable:**
```python
response = requests.get(user_provided_url)
```

**Secure:**
```python
ALLOWED_DOMAINS = {"api.example.com", "cdn.example.com"}

def fetch_url(url: str) -> Response:
    parsed = urlparse(url)
    if parsed.netloc not in ALLOWED_DOMAINS:
        raise ValueError("Domain not allowed")
    return requests.get(url)
```

## Hardcoded Secrets

**Vulnerable:**
```python
API_KEY = "sk-1234567890abcdef"
db_password = "super_secret_123"
```

**Secure:**
```python
import os

API_KEY = os.environ["API_KEY"]
db_password = os.environ["DB_PASSWORD"]
```

## Insecure Random

**Vulnerable:**
```python
import random
token = ''.join(random.choices(string.ascii_letters, k=32))
```

**Secure:**
```python
import secrets
token = secrets.token_urlsafe(32)
```

## XML External Entity (XXE)

**Vulnerable:**
```python
from xml.etree import ElementTree
tree = ElementTree.parse(user_xml)
```

**Secure:**
```python
import defusedxml.ElementTree as ET
tree = ET.parse(user_xml)
```
