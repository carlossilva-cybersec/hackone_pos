
# 💻 HackOne Pós-Graduação - Inteligência Artificial Aplicada a Redes e Cibersegurança
> Repositório oficial de estudos e laboratórios da disciplina ministrada por  
> **[Carlos Silva](https://www.linkedin.com/in/carlossilva-cybersec/)**  
> Instrutor HackOne | Especialista em SOC, CTI e Inteligência Artificial Aplicada à Segurança

---

## 🚀 Sobre o Curso

Este repositório reúne **materiais práticos, notebooks e datasets reais** utilizados nas aulas de **Inteligência Artificial Aplicada a Redes e Cibersegurança**.

Durante as aulas, você aprenderá a:

- Processar **logs de rede** (firewall, proxy, IDS, endpoint);
- Desenvolver **modelos de Machine Learning** para detectar anomalias;
- Integrar IA a ferramentas de SOC (Wazuh, MISP, SIEM);
- Visualizar **tráfego e ameaças** com grafos interativos;
- Compreender como a IA pode agir como um **analista SOC automatizado**.

---

## 🧩 Estrutura do Repositório
```text
hackone_pos/
│
├── network-anomaly-detection-lab/        # Laboratório 1 - FortiGate + ML
│   ├── pipeline_ids_fortigate.ipynb      # Notebook principal
│   ├── fortigate_syslog.log.gz           # Dataset de amostra
│   └── img/
│       └── topologia_csbank.png          # Topologia do caso de uso
│
├── requirements.txt                      # Dependências Python
└── README.md                             # Este arquivo
```


---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o Repositório
```
git clone https://github.com/carlossilva-cybersec/hackone_pos.git
cd hackone_pos/network-anomaly-detection-lab
```
### 2️⃣ Instalar Dependências
`pip install -r requirements.txt` 

ou, manualmente: 
`pip install pandas scikit-learn matplotlib networkx pyvis` 

### 3️⃣ Abrir o Notebook
`jupyter notebook pipeline_ids_fortigate.ipynb`
