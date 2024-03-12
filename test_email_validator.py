import pytest
from email_validator import validate_email

# Позитивні тести (дійсні email)
@pytest.mark.parametrize("email", [
    "example@example.com",
    "user123@example.com",
    "user.name@example.com",
    "user-name@example.com",
    "user123@example.co.uk"
])
def test_valid_emails(email):
    assert validate_email(email) == True

# Негативні тести (недійсні email)
@pytest.mark.parametrize("email", [
    "example@example",
    "user123@.com",
    "user@name@example.com",
    "user123example.com",
    "user@123@example.com"
])
def test_invalid_emails(email):
    assert validate_email(email) == False
