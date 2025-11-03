# Detecção de Anomalias em Redes

### 🧠 Caso de Uso: Exfiltração de Dados no Ambiente CSBANK

**Topologia**

![Topologia CSBANK](https://raw.githubusercontent.com/carlossilva-cybersec/hackone_pos/refs/heads/main/network-anomaly-detection-lab/img/topologia.png)

O cenário simula o ambiente da **CSBANK**, uma fintech alvo de incidentes de segurança envolvendo **malware** e **exfiltração de dados via rede**.  
Os logs coletados do firewall e das máquinas comprometidas serão usados como base para **treinar e testar modelos de IA** voltados à detecção dessas atividades.

---

## 🧪 **LAB I — Detecção de Malware com Machine Learning**

### 🎯 **Objetivo**
Desenvolver um modelo de aprendizado de máquina capaz de identificar comportamentos anômalos em logs de rede e detectar **máquinas potencialmente comprometidas**.

### 🧩 **Desafios**
- [ ] Analisar o conjunto de dados fornecido no repositório (`Data/`)  
- [ ] Identificar **quais máquinas foram afetadas** pelo malware  
- [ ] Descobrir **quem realizou a exfiltração de dados**  
- [ ] Desenvolver um **algoritmo de Machine Learning** que identifique automaticamente o IP envolvido na exfiltração  

💡 **Dica:** Utilize o modelo `IsolationForest` ou `LocalOutlierFactor` para detectar comportamentos fora do padrão (picos de envio de dados, volume anômalo de bytes, etc.)

### 📂 **Dados para Análise**
> Sample dataset disponível em:  
> `Data/fortigate_syslog.log.gz`

---

## 🧪 **LAB II — Detecção de Exfiltração de Dados**

### 🎯 **Objetivo**
Aprofundar a análise utilizando logs de tráfego ICMP, DNS e HTTPS para identificar **técnicas avançadas de exfiltração**.

### 🧩 **Desafios**
- [ ] Tratar e transformar logs de múltiplas fontes (firewall, proxy, endpoint)  
- [ ] Criar features derivadas (ex: taxa de bytes por segundo, duração média, entropia dos pacotes)  
- [ ] Aplicar um modelo não supervisionado e gerar **ranking de destinos suspeitos**  
- [ ] Visualizar as conexões em **grafo interativo** (PyVis / NetworkX)  
- [ ] Redigir um breve relatório técnico: “Como a IA detectou o tráfego suspeito?”

---

## 💡 **Extra (para alunos avançados)**

- Implemente um **detector de anomalias temporal**, considerando o padrão de tráfego hora a hora.  
- Integre seu modelo ao **Wazuh / MISP / SIEM** e simule um alerta em tempo real.  
- Teste diferentes técnicas: `OneClassSVM`, `KMeans`, ou `DBSCAN` para clustering de atividades suspeitas.

---

## 🧰 **Resultados Esperados**

Ao final dos laboratórios, você deverá ser capaz de:
- Identificar e isolar **máquinas comprometidas**;  
- Mapear **fluxos de exfiltração** dentro da topologia simulada;  
- Implementar **pipelines de IA aplicadas à detecção de ameaças em redes reais**.

---

🧑‍🏫 **Professor:** [Carlos Silva](https://www.linkedin.com/in/carlossilva-cybersec/)  
📍 HackOne Pós-Graduação — *Inteligência Artificial Aplicada a Redes e Cibersegurança*  
📘 [LinkedIn](https://www.linkedin.com/in/carlossilva-cybersec/) | [GitHub](https://github.com/carlossilva-cybersec)

> _“Não basta capturar logs — é preciso ensinar a máquina a pensar como um analista SOC.”_

---
