# Zecpath AI Security Framework

## Objective

Protect candidate information and hiring intelligence data.

---

# Security Architecture

Candidate
↓
HTTPS API Gateway
↓
Authentication Layer
↓
Authorization Layer
↓
AI Processing
↓
Encrypted Database
↓
Audit Logging

---

# Storage Security

| Data | Security |
|--------|------------|
| Transcripts | AES/Fernet Encryption |
| Reports | Encryption |
| Scores | Secure Database |
| Logs | Write-only Storage |

---

# Authentication

Supported Methods:

- JWT
- OAuth

---

# Authorization

Role-Based Access Control (RBAC)

Roles:

- Admin
- Recruiter
- Viewer

---

# Security Benefits

- Data protection
- Unauthorized access prevention
- Auditability
- Compliance readiness