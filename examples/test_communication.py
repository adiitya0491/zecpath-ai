import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from interview_ai.communication_engine import (
    calculate_communication_score
)

text = (
    "I have experience in Python because I worked "
    "on backend systems and API development."
)

result = calculate_communication_score(text)

print("\n=== COMMUNICATION SCORE ===")
print(result)