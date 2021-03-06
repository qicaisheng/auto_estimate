import json

GIT_COMMIT_REPORT_NAME = 'git-commit-report.txt'
CURRENT_WORKSPACE_DATA = '../data/currentWorkspacePath.txt'
CURRENT_QUESTION_NAME = '../data/currentQuestionName.txt'
CONFIG_FILE = '../config.json'
SCORE_REPORT_NAME = 'score.txt'
FULL_SCORE = 10
SCORE_OF_COMMIT_COUNT = 7
SCORE_OF_COMMIT_MESSAGE = 3
COMMIT_MESSAGE_LENGTH_BASE_LINE = 8
commit_count_base_line = 10


def get_current_workspace_path():
    with open(CURRENT_WORKSPACE_DATA) as text_file:
        return text_file.read().strip()


def get_git_commit_report():
    git_commit_report_path = get_current_workspace_path() + "/git_commit/" + GIT_COMMIT_REPORT_NAME
    with open(git_commit_report_path) as text_file:
        return text_file.read()


def get_config():
    with open(CONFIG_FILE) as json_file:
        return json.load(json_file)


def get_current_question_name():
    with open(CURRENT_QUESTION_NAME) as text_file:
        return text_file.read().strip()


def set_commit_count_base_line():
    global commit_count_base_line
    config = get_config()
    current_question_name = get_current_question_name()
    commit_count_base_line = config[current_question_name]["gitCommit"]


def calculate_score_of_commit_count(commit_count):
    if commit_count > commit_count_base_line:
        return SCORE_OF_COMMIT_COUNT
    return (float(commit_count) / float(commit_count_base_line)) * SCORE_OF_COMMIT_COUNT


def calculate_score_of_commit_message(commits):
    commit_count = len(commits)
    deduct_marks = 0
    for commit in commits:
        commit_message_start_index = commit.index(" ") + 1
        commit_message = commit[commit_message_start_index:]
        if len(commit_message) < COMMIT_MESSAGE_LENGTH_BASE_LINE:
            deduct_marks += 0.5 * (float(commit_count_base_line) / float(commit_count))
    score = SCORE_OF_COMMIT_MESSAGE - deduct_marks
    return score if score > 0 else 0


def calculate_score():
    set_commit_count_base_line()
    commits = get_git_commit_report().splitlines()
    score_of_commit_count = calculate_score_of_commit_count(len(commits))
    score_of_commit_message = calculate_score_of_commit_message(commits)
    return score_of_commit_count + score_of_commit_message


def save_score():
    score_path = get_current_workspace_path() + "/" + SCORE_REPORT_NAME
    f = open(score_path, "a")
    f.write("Git Commit Score: " + str(calculate_score()) + "\n")
    f.close()


def main():
    save_score()
    print('git commit score is: {}'.format(calculate_score()))


if __name__ == "__main__":
    main()
