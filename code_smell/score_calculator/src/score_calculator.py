import json
import os

PMD_REPORT_NAME = 'pmd-result-report.json'
CURRENT_WORKSPACE_DATA = '../../../data/currentWorkspacePath.txt'
FULL_SCORE = 20
PRIORITY_DEDUCT_MARKS = {1: 3, 2: 2, 3: 0.5, 4: 0.2, 5: 0.1}
CURRENT_QUESTION_NAME = '../../../data/currentQuestionName.txt'
CONFIG_FILE = '../../../config.json'
SCORE_REPORT_NAME = 'score.txt'

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
    class_count = get_class_count_from_code()
    if class_count < class_count_base_line:
        return SCORE_OF_CLASS_COUNT
    return 0


def get_class_count_from_code():
    class_count = 0
    src_main_path = get_current_workspace_path() + "/code/src/main"
    for (root, dirs, files) in os.walk(src_main_path):
        for file in files:
            if file.endswith(".java"):
                class_count = class_count + 1
    return class_count


def get_pmd_report():
    pmd_report_path = get_current_workspace_path() + "/" + PMD_REPORT_NAME
    with open(pmd_report_path) as json_file:
        return json.load(json_file)


def get_current_workspace_path():
    with open(CURRENT_WORKSPACE_DATA) as text_file:
        return text_file.read().strip()


def deduct_score_for_pmd():
    deduct_marks = 0
    data = get_pmd_report()
    for checked_file in data['files']:
        for violation in checked_file['violations']:
            deduct_marks += PRIORITY_DEDUCT_MARKS[violation['priority']]
    return deduct_marks


def calculate_score():
    score = FULL_SCORE - deduct_score_for_pmd() - deduct_score_of_class_count()
    return score if score > 0 else 0


def save_score():
    score_path = get_current_workspace_path() + "/" + SCORE_REPORT_NAME
    f = open(score_path, "a")
    f.write("Code Smell Score: " + str(calculate_score()) + "\n")
    f.close()


def main():
    save_score()
    print('code smell score is: {}'.format(calculate_score()))


if __name__ == "__main__":
    main()
