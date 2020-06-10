import json

PMD_REPORT = '../../pmd_checker/pmd-result-report.json'
FULL_SCORE = 20
PIRORITY_DEDUCT_MARKS = {1: 3, 2: 2, 3: 0.5, 4: 0.2, 5: 0.1}

def get_report():
    with open(PMD_REPORT) as json_file:
        return json.load(json_file)
        
def calculate_score():
    score = FULL_SCORE
    data = get_report()    
    for checked_file in data['files']:
        for violation in checked_file['violations']:
            deduct_marks = PIRORITY_DEDUCT_MARKS[violation['priority']]
            score = score - deduct_marks
    return score if score > 0 else 0

def main():
    print('code smell score is: {}'.format(calculate_score()))

if __name__ == "__main__":
    main()