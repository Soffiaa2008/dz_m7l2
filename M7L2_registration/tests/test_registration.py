import pytest
from registration.registration import add_user, initialize_users

def test_add_new_user():
    users = initialize_users()
    result = add_user(users, "new_user", "new_password")
    assert result == "Новый пользователь new_user успешно добавлен."
    assert "new_user" in users
    assert users["new_user"] == "new_password"


def test_add_existing_user():
    users = initialize_users()
    add_user(users, "user1", "password1")
    result = add_user(users, "user1", "new_password")
    assert result == "Пользователь с логином user1 уже существует."
