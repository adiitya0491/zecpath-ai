import re
from collections import defaultdict
import json

with open("data/skill_synonyms.json") as f:
    SKILL_SYNONYMS = json.load(f)

def normalize_skill(skill):

    skill = skill.lower()

    if skill in SKILL_SYNONYMS:
        return SKILL_SYNONYMS[skill]

    return skill
# ==========================================================
# ENTERPRISE CLOUD ENGINEERING SKILL UNIVERSE
# Built from your JD dataset
# ==========================================================

TECH_SKILLS = {

    # ==============================
    # CLOUD PLATFORMS
    # ==============================
    "aws", "amazon web services",
    "azure", "microsoft azure",
    "gcp", "google cloud",
    "hybrid cloud", "multi-cloud",
    "cloud-native", "cloud architecture",

    # ==============================
    # AWS SERVICES
    # ==============================
    "ec2", "ecs", "eks",
    "s3", "rds", "dynamodb",
    "lambda", "cloudwatch", "cloudtrail",
    "iam", "route53",
    "elastic load balancer",
    "autoscaling", "cloudformation",
    "codepipeline", "codebuild",

    # ==============================
    # AZURE SERVICES
    # ==============================
    "aks", "azure devops",
    "azure functions",
    "azure active directory",
    "arm template",

    # ==============================
    # GCP SERVICES
    # ==============================
    "gke", "bigquery",
    "cloud storage",
    "cloud run",

    # ==============================
    # CONTAINERS & ORCHESTRATION
    # ==============================
    "docker", "kubernetes",
    "helm", "containerization",
    "container platforms",

    # ==============================
    # CI/CD & DEVOPS
    # ==============================
    "ci/cd", "continuous integration",
    "continuous deployment",
    "jenkins", "github actions",
    "gitlab ci", "bitbucket pipelines",
    "devops", "pipeline automation",

    # ==============================
    # INFRASTRUCTURE AS CODE
    # ==============================
    "terraform",
    "infrastructure as code",
    "iac",
    "cloudformation",
    "arm templates",

    # ==============================
    # CONFIGURATION MANAGEMENT
    # ==============================
    "ansible", "chef", "puppet",

    # ==============================
    # OS & SCRIPTING
    # ==============================
    "linux", "windows",
    "linux administration",
    "shell scripting",
    "bash", "powershell",
    "python", "go", "java",

    # ==============================
    # NETWORKING
    # ==============================
    "vpc", "subnet", "firewall",
    "dns", "nat gateway",
    "load balancer", "network security",
    "cloud networking",

    # ==============================
    # SECURITY
    # ==============================
    "iam", "identity and access management",
    "rbac", "cloud security",
    "encryption", "zero trust",
    "security hardening",
    "governance", "compliance",

    # ==============================
    # MONITORING & OBSERVABILITY
    # ==============================
    "monitoring", "logging",
    "observability",
    "prometheus", "grafana",
    "datadog",
    "alerting",

    # ==============================
    # PERFORMANCE & TESTING
    # ==============================
    "performance testing",
    "load testing",
    "stress testing",
    "jmeter", "k6", "gatling",
    "performance tuning",

    # ==============================
    # STORAGE & DATABASES
    # ==============================
    "mysql", "postgresql",
    "mongodb", "redis",
    "cloud storage",

    # ==============================
    # ARCHITECTURE & DESIGN
    # ==============================
    "distributed systems",
    "microservices",
    "high availability",
    "disaster recovery",
    "cost optimization",
    "scalability",
    "cloud governance",

    # ==============================
    # PLATFORM & SRE
    # ==============================
    "site reliability engineering",
    "sre",
    "incident response",
    "system hardening",
    "system upgrades",
    "patching"
}

# ==========================================================
# CLEAN TEXT
# ==========================================================

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#./\-\s]", " ", text)

    # apply synonym normalization
    for short, full in SKILL_SYNONYMS.items():
        text = text.replace(short, full)

    return text


# ==========================================================
# SKILL DETECTION
# ==========================================================

def detect_skills(text):

    text = clean_text(text)
    found = defaultdict(int)

    for skill in TECH_SKILLS:

        normalized_skill = normalize_skill(skill)

        pattern = r"\b" + re.escape(normalized_skill) + r"\b"
        matches = re.findall(pattern, text)

        if matches:
            found[normalized_skill] += len(matches)

    return found


# ==========================================================
# CONFIDENCE SCORING
# ==========================================================

def assign_confidence(skill_counts):


    results = []

    for skill, count in skill_counts.items():

        if count >= 5:
            confidence = 0.95
        elif count >= 3:
            confidence = 0.85
        else:
            confidence = 0.75

        results.append({
            "skill": skill,
            "frequency": count,
            "confidence": confidence
        })

    return sorted(results, key=lambda x: x["frequency"], reverse=True)