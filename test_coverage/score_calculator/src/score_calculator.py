import xml.etree.ElementTree as ET

JACOCO_REPORT_NAME = 'jacoco.xml'
CURRENT_WORKSPACE_DATA = '../../../data/currentWorkspacePath.txt'
FULL_SCORE = 10
SCORE_REPORT_NAME = 'score.txt'


def get_jacoco_report():
    jacoco_report_path = get_current_workspace_path() + "/jacoco/" + JACOCO_REPORT_NAME
    return ET.parse(jacoco_report_path).getroot()


def get_current_workspace_path():
    with open(CURRENT_WORKSPACE_DATA) as text_file:
        return text_file.read().strip()


def calculate_score():
    root = get_jacoco_report()
    instruction_percentage = 0
    branch_percentage = 0
    for child in root:
        if child.tag == 'counter' and child.attrib['type'] == 'INSTRUCTION':
            instruction_percentage = float(child.attrib['covered']) / (float(child.attrib['covered']) + float(child.attrib['missed']))
        if child.tag == 'counter' and child.attrib['type'] == 'BRANCH':
            branch_percentage = float(child.attrib['covered']) / (float(child.attrib['covered']) + float(child.attrib['missed']))

    return (instruction_percentage + branch_percentage) / 2 * FULL_SCORE


def save_score():
    score_path = get_current_workspace_path() + "/" + SCORE_REPORT_NAME
    f = open(score_path, "a")
    f.write("Test Coverage Score: " + str(calculate_score()) + "\n")
    f.close()


def main():
    save_score()
    print('test coverage score is: {}'.format(calculate_score()))


if __name__ == "__main__":
    main()
