from screening_ai.transcript_cleaner import (
    process_audio_answers
)

audio_inputs = [

    "um i have 3 years experience in aws",

    "uh currently working as cloud engineer",

    ""
]

print(
    process_audio_answers(
        audio_inputs
    )
)