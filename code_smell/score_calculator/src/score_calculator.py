import json

PMD_REPORT_NAME = 'pmd-result-report.json'
CURRENT_WORKSPACE_DATA = '../../../data/currentWorkspacePath.txt'
FULL_SCORE = 20
PRIORITY_DEDUCT_MARKS = {1: 3, 2: 2, 3: 0.5, 4: 0.2, 5: 0.1}


def get_pmd_report():
    pmd_report_path = get_current_workspace_path().strip() + "/" + PMD_REPORT_NAME
    with open(pmd_report_path) as json_file:
        return json.load(json_file)


def get_current_workspace_path():
    with open(CURRENT_WORKSPACE_DATA) as text_file:
        return text_file.read()


def calculate_score():
    score = FULL_SCORE
    data = get_pmd_report()
    for checked_file in data['files']:
        for violation in checked_file['violations']:
            deduct_marks = PRIORITY_DEDUCT_MARKS[violation['priority']]
            score = score - deduct_marks
    return score if score > 0 else 0


def main():
    print('code smell score is: {}'.format(calculate_score()))


if __name__ == "__main__":
    main()
