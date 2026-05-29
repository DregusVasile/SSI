import rarfile

rar_path = "arhiva.rar"
password_list = "parole.txt"

try:
    rf = rarfile.RarFile(rar_path)

    with open(password_list, "r", encoding="utf-8") as file:
        passwords = file.readlines()

    found = False

    for password in passwords:
        password = password.strip()

        try:
            rf.extractall(pwd=password)
            print(f"[+] Parola gasita: {password}")
            found = True
            break

        except:
            print(f"[-] Parola gresita: {password}")

    if not found:
        print("Parola nu a fost gasita in lista.")

except FileNotFoundError:
    print("Fisierul RAR sau lista de parole nu exista.")