from backend.security import CommandPolicy


def test_command_policy_blocks_dangerous_input():
    try:
        CommandPolicy.validate("rm -rf /tmp")
        assert False, "dangerous command should be blocked"
    except ValueError:
        pass


def test_command_policy_allows_safe_git_command():
    CommandPolicy.validate("git status")
