---
order: -3
---

# Kali Linux Installation

We recommend installing **Kali Linux**. Kali Linux is a cybersecurity-focused operating system with many tools that could be useful for solving CTFs.

For Windows users, we recommend the following installation (run as admin):
```
wsl --install --distribution kali-linux
```

Then run the following commands inside Kali Linux:
```
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y kali-linux-default
```

**Tip:** You can access your Windows files from the following directory in WSL: `/mnt/c`