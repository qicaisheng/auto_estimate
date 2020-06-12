import json

PMD_REPORT_NAME = 'pmd-result-report.json'
CURRENT_WORKSPACE_DATA = '../../../data/currentWorkspacePath.txt'
FULL_SCORE = 20
PRIORITY_DEDUCT_MARKS = {1: 3, 2: 2, 3: 0.5, 4: 0.2, 5: 0.1}
CURRENT_QUESTION_NAME = '../../../data/currentQuestionName.txt'
CONFIG_FILE = '../../../config.json'

SCORE_OF_CLASS_COUNT = 3
class_count_base_line = 3


def get_config():
    with open(CONFIG_FILE) as json_file:
        return json.load(json_file)


def get_current_question_name():
    with open(CURRENT_QUESTION_NAME) as text_file:
        return text_file.read().strip()


def set_class_count_base_line():
    global class_count_base_line
    config = get_config()
    current_question_name = get_current_question_name()
    class_count_base_line = config[current_question_name]["classCount"]


def deduct_score_of_class_count():
    set_class_count_base_line()
    return class_count_base_line


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
    print('class deduct score is: {}'.format(deduct_score_of_class_count()))


if __name__ == "__main__":
    main()
