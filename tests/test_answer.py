from screening_ai.answer_engine import (
    process_answer
)

answer = """

I have 4 years experience
in AWS Docker Terraform

"""

result = process_answer(
    "Q3",
    answer
)

print(result)