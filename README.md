
# Secure Password Manager

A simple, elegant, and efficient password manager built with **Tkinter** and **ttkbootstrap**. Generate strong passwords, save credentials securely to a CSV file, and search for them with ease.

## Project Structure

```
 Project Folder
├── main.py               # Main application file
├── requirements.txt      # Required Python packages
├── LICENSE               # License file
└── README.md             # Project overview and usage guide
```

## Features

- Strong password generator with custom length & character types
- Save credentials (Platform, Email/Phone, Password) to CSV
- Search saved credentials by platform name
- Password visibility toggle & strength meter
- Easy-to-use UI with `ttkbootstrap` themes

##  Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

### Python Libraries Used

- `ttkbootstrap`
- `pandas`
- `tkinter` (standard with Python)
- `os`, `random`

## How to Run

Make sure you have Python installed (>= 3.6). Then run:

```bash
python main.py
```

## Data Handling

Passwords are saved in a `Passwords.csv` file in the same directory. Ensure this file is handled securely.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> Made with ❤️ for offline use and secure password management.
