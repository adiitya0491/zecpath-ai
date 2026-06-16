def export_report_text(report):

    text = f"""

Candidate ID:
{report['candidate_id']}

Job ID:
{report['job_id']}

Final Score:
{report['final_score']}

Decision:
{report['decision']}

"""

    return text