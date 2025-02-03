A = str(input("Введите ваше имя: "))

B = str(input("Введите вашу фамилию: "))

def EnterNameSurname(A, B):
    c = f"Здравствуйте, {A} {B}!"
    return c

print(EnterNameSurname(A, B))