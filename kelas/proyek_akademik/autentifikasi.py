def login(username, password):
    print(f"Memverifikasi akun {username}...")
    if username == "admin" and password == "123":
        return True
    return False