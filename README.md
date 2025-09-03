# 🔐 Avangard Cybersecurity – Password Generator

![GitHub last commit](https://img.shields.io/github/last-commit/avangard7860/password-generator)
![GitHub repo size](https://github.com/Mahwish2007/Password-generator/blob/main/password_generator.py)
![GitHub stars](https://img.shields.io/github/stars/avangard7860/password-generator?style=social)

A simple **Python password generator** using the `secrets` module for strong,
cryptographically secure passwords.

---

## 🚀 Features
- Cryptographically secure randomness (`secrets`)
- Adjustable length (8–128)
- Multiple password generation
- Option to exclude ambiguous characters (O, 0, l, 1, |)
- CLI-friendly (run from terminal)

---

## 💻 Usage
```bash
python password_generator.py              # one 16-char password
python password_generator.py -l 24        # 24-char password
python password_generator.py -n 3         # three passwords
python password_generator.py --no-symbols # letters + digits only

