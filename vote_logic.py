import csv
import os

CSV_FILE = 'votes.csv'

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['voter_id', 'candidate'])

def has_voted(voter_id: str) -> bool:
    """
    Checks the ID of the voter, if the voter has already voted,
    False otherwise
    """
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['voter_id'] == voter_id:
                return True
    return False

def register_vote(voter_id: str, candidate: str) -> str:
    """
    The ID of the voter, the candidate to vote for, submitted message or an error message
    """
    if has_voted(voter_id):
        return 'Error: Voter ID has already voted.'

    if candidate not in ['Amy', 'Frank']:
        return 'Error: No candidate selected.'

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([voter_id, candidate])

    return f'{candidate}.'