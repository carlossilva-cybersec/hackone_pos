# 🧠 HackOne - Inteligência Artificial Aplicada a Redes e Cibersegurança

### Repositório de estudos e apoio aos alunos da disciplina  
> **Pós-graduação HackOne | Inteligência Artificial aplicada a Redes e Segurança de Computadores**

📘 **Professor:** [Carlos Silva](https://www.linkedin.com/in/carlossilva-cybersec/)  
👨‍💻 **Tema:** Aplicações práticas de IA e Machine Learning em redes e ambientes SOC

---

## 🚀 Objetivo da Disciplina

O objetivo é **desmistificar o uso de Inteligência Artificial em segurança da informação** e mostrar, na prática, como usar algoritmos de aprendizado de máquina para **detecção de ameaças, anomalias e comportamentos suspeitos** em redes de computadores.

Durante o curso, os alunos aprenderão a:

- Ler e tratar **logs reais de dispositivos de rede** (FortiGate, Proxy, IDS, etc.)  
- Criar **pipelines de Machine Learning** para detectar anomalias  
- Explorar conceitos de **IA aplicada a SOCs (Security Operations Centers)**  
- Implementar **visualizações e modelos preditivos** de forma prática  

---

## 🔍 Projeto Prático: Detecção de Anomalias com ML

📄 **Notebook:** `pipeline_ids_fortigate.ipynb`  
📂 **Dataset:** [fortigate_syslog.log.gz](https://raw.githubusercontent.com/carlossilva-cybersec/hackone_pos/refs/heads/main/network-anomaly-detection-lab/fortigate_syslog.log.gz)

### 🧩 Descrição
Neste laboratório, você aprenderá a transformar logs brutos do **FortiGate** em dados prontos para análise com **Machine Learning**, utilizando o modelo `IsolationForest` para detectar **exfiltrações de dados via ICMP (PING)**.

O pipeline inclui:
1. **Ingestão dos logs**
2. **Transformação e parsing**
3. **Feature Engineering**
4. **Modelagem e detecção**
5. **Visualização com NetworkX e PyVis**

---
