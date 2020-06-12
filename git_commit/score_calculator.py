GIT_COMMIT_REPORT_NAME = 'git-commit-report.txt'
CURRENT_WORKSPACE_DATA = '../data/currentWorkspacePath.txt'
FULL_SCORE = 10
SCORE_OF_COMMIT_COUNT = 7
SCORE_OF_COMMIT_MESSAGE = 3
COMMIT_MESSAGE_LENGTH_BASE_LINE = 8
commit_count_base_line = 10


def get_current_workspace_path():
    with open(CURRENT_WORKSPACE_DATA) as text_file:
        return text_file.read()


def get_git_commit_report():
    git_commit_report_path = get_current_workspace_path().strip() + "/git_commit/" + GIT_COMMIT_REPORT_NAME
    with open(git_commit_report_path) as text_file:
        return text_file.read()


def calculate_score_of_commit_count(commit_count):
    if commit_count > commit_count_base_line:
        return SCORE_OF_COMMIT_COUNT
    return (commit_count / commit_count_base_line) * SCORE_OF_COMMIT_COUNT


def calculate_score_of_commit_message(commits):
    commit_count = len(commits)
    deduct_marks = 0
    for commit in commits:
        commit_message_start_index = commit.index(" ") + 1
        commit_message = commit[commit_message_start_index:]
        if len(commit_message) < COMMIT_MESSAGE_LENGTH_BASE_LINE:
            deduct_marks += 0.5 * (commit_count_base_line / commit_count)
    score = SCORE_OF_COMMIT_MESSAGE - deduct_marks
    return score if score > 0 else 0


def calculate_score():
    commits = get_git_commit_report().splitlines()
    score_of_commit_count = calculate_score_of_commit_count(len(commits))
    score_of_commit_message = calculate_score_of_commit_message(commits)
    return score_of_commit_count + score_of_commit_message


def main():
    print('git commit score is: {}'.format(calculate_score()))


if __name__ == "__main__":
    main()
