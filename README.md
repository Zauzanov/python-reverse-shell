<p align="center">
  <h1 align="center"> A minimal Python Reverse Shell: code and explanation of how it works. For Educational Purposes Only. Use only on hosts/networks you own or have permission to test. </h1>
</p>

## 🚀 Quick Start
## 1. Edit 'python-rev-shell.py' file, adding your attacker machine's IP address and port.
## 2. Download 'python-rev-shell.py' file to the target machine.
## 3. Set up a listener on the attacker machine:
```bash
nc -nlvp 1234
```
## 4. Run the script on the target machine:
```bash
python3 python-rev-shell.py
```