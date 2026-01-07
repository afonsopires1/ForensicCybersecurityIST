# ForensicCybersecurityIST
Digital forensic investigation of the Ariane 6 case, conducted across three stages as part of the Forensics &amp; Cyber-Security course at Instituto Superior Técnico. The project covers file forensics, steganalysis, disk analysis, and network traffic analysis to trace credential theft, data exfiltration, and assess a potential insider conspiracy.


# Ariane 6 – Digital Forensics Investigation

This repository contains the work developed for the **Forensics & Cyber-Security** course at Instituto Superior Técnico (MEIC/METI), focused on a multi-stage digital forensic investigation known as the **Ariane 6 case**.

The investigation is divided into three progressive lab assignments, each expanding the scope of the analysis and introducing new forensic techniques, evidence sources, and investigative goals.

---

## 🧩 Case Overview

The Ariane 6 case investigates alleged cybercriminal activity involving:
- Theft of university credentials
- Concealed and exfiltrated sensitive documents
- Possible insider threats within IST’s Satellite Lab
- A suspected conspiracy related to the ISTSat-1 satellite

Across the three stages, the investigation follows João Musk, a master’s student suspected of storing stolen credentials and classified material, and gradually expands to include disk forensics and network-level analysis.

---

## 🔍 Lab Assignments Summary

### **Lab Assignment I – File Forensics & Steganalysis**
**Objective:**  
Analyze files extracted from a private Sigma cluster account to uncover stolen credentials and hidden artifacts.

**Key Activities:**
- Steganalysis of images, audio, and documents
- Identification of concealed files
- Recovery of stolen credentials
- Construction of an initial event timeline
- Hypothesis formulation and investigative recommendations


---

### **Lab Assignment II – Disk & File System Forensics**
**Objective:**  
Analyze forensic images of João Musk’s workstation and backup server to trace the origin, handling, and lifecycle of previously discovered artifacts.

**Key Activities:**
- File system analysis of disk images
- Tracking file provenance and transfers
- Detection of anti-forensic behavior
- Correlation with earlier findings
- Expanded timeline reconstruction

:contentReference[oaicite:1]{index=1}

---

### **Lab Assignment III – Network Forensics**
**Objective:**  
Investigate potential data exfiltration and information leaks from IST’s Satellite Lab network.

**Key Activities:**
- Analysis of network traffic captures (PCAPs)
- Decryption of HTTPS traffic using SSL key logs
- Identification of document transfers
- Attribution of actions to specific users or machines
- Evaluation of the conspiracy hypothesis
- Final consolidated timeline and conclusions

:contentReference[oaicite:2]{index=2}

---

## 🛠 Tools & Techniques

- Kali Linux (forensically sound environment)
- Steganalysis tools
- File system forensic tools
- Wireshark (with SSL/TLS decryption)
- Cryptographic hash verification (SHA-256)
- Timeline reconstruction methodologies

---

## 🎯 Learning Outcomes

- Practical experience in digital forensics
- Evidence-based reasoning and reporting
- Chain-of-custody awareness
- Correlation of artifacts across multiple forensic domains
- End-to-end investigation workflow

---

## ⚠️ Disclaimer

This project was developed **strictly for academic purposes**.  
All data, characters, and scenarios are fictional and part of a controlled educational exercise.

---

## 👤 Authors

- Afonso Pires, António Silva, Inês Alves
- Instituto Superior Técnico  
- Forensics & Cyber-Security (2024/2025)
