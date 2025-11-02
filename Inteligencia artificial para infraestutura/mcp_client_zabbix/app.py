from flask import Flask, render_template, request, jsonify
import requests, json, os, textwrap

app = Flask(__name__)

# Configs
MCP_URL = os.getenv("MCP_URL") 
HEADERS = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
def call_mcp(tool, limit=5, args=None):
    """Consulta o Zabbix MCP (formato SSE) e retorna JSON interno tratado"""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool,
            "limit": limit,
            "arguments": args or {}
        }
    }

    try:
        r = requests.post(MCP_URL, headers=HEADERS, json=payload, timeout=30)
    except requests.exceptions.RequestException as e:
        return f"[ERRO] Falha ao conectar no MCP: {e}"

    raw = r.text.strip()
    if not raw:
        return "[ERRO] MCP respondeu vazio — possivelmente travado ou sem JSON."

    print(f"[DEBUG] MCP status={r.status_code} bytes={len(raw)}")
    print(raw[:200], "...\n")

    # 🧩 Limpeza do formato SSE (remove linhas com 'event:' e extrai o 'data:' puro)
    cleaned_lines = []
    for line in raw.splitlines():
        if line.startswith("data:"):
            cleaned_lines.append(line[len("data:"):].strip())
    cleaned = "".join(cleaned_lines)
    if not cleaned:
        cleaned = raw  # fallback, caso não ache 'data:'

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"[ERRO] Falha ao decodificar JSON SSE: {e}")
        return f"[ERRO] JSON SSE inválido recebido do MCP:\n{cleaned[:300]}"

    # Verifica se veio erro no JSON-RPC
    if "error" in data:
        msg = data["error"].get("message", "Erro desconhecido")
        return f"[ERRO MCP] {msg}"

    try:
        text_content = data["result"]["content"][0]["text"]
        inner_clean = (
            text_content.replace("\\n", "\n")
                        .replace("\\\"", "\"")
                        .replace("\r", "")
                        .strip()
        )
        try:
            decoded = json.loads(inner_clean)
            return json.dumps(decoded, indent=2, ensure_ascii=False)
        except Exception:
            return inner_clean[:2000]
    except Exception as e:
        return f"[ERRO] Estrutura inesperada na resposta: {e}\n{json.dumps(data, indent=2)}"




def ask_deepseek(prompt):
    """Usa o modelo DeepSeek Chat (API oficial)"""
    if not DEEPSEEK_API_KEY:
        return "[ERRO] DEEPSEEK_API_KEY não configurada no .env"

    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Você é um assistente SOC conectado ao Zabbix MCP. Seja direto, técnico e claro."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 700
    }

    try:
        r = requests.post(url, headers=headers, json=data, timeout=60)
        j = r.json()
        return j["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[ERRO] Falha na API DeepSeek: {e}\nCorpo: {r.text[:300]}"


# ===================== Rotas Flask =====================

@app.route("/")
def index():
    """Renderiza a interface do chat"""
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Processa mensagens em linguagem natural"""
    user_msg = (request.json or {}).get("message", "").strip()
    if not user_msg:
        return jsonify({"response": "Por favor, digite uma mensagem."})

    # 1️⃣ Identificação de intenção
    intent_prompt = f"""
    Você é um assistente SOC conectado ao Zabbix via MCP.
    Decida qual ferramenta do Zabbix usar para responder à pergunta abaixo:
    - Use 'host_get' para perguntas sobre hosts, servidores, máquinas, status, disponibilidade, etc.
    - Use 'event_get' para perguntas sobre eventos, alertas, incidentes e logs.
    - Use 'problem_get' para perguntas sobre problemas ativos, falhas, status crítico ou pendente.
    - Use 'trigger_get' para perguntas sobre condições ou gatilhos.
    - Se não tiver relação com o Zabbix, responda 'none'.
    Retorne apenas o nome da ferramenta (host_get, event_get, problem_get, trigger_get ou none).

    Pergunta do usuário: "{user_msg}"
    """
    try:
        decision = ask_deepseek(intent_prompt).strip().lower()
    except Exception as e:
        return jsonify({"response": f"[ERRO] Falha ao decidir intenção: {e}"})

    # 2️⃣ Execução do comando
    if decision == "problem_get":
        data = call_mcp("problem_get", limit=1)
        final_prompt = f"Analise o problema retornado pelo Zabbix e descreva a gravidade, impacto e ação sugerida:\n{data}"
    elif decision == "event_get":
        data = call_mcp("event_get", limit=3)
        final_prompt = f"Analise e explique esses eventos do Zabbix:\n{data}"
    elif decision == "host_get":
        data = call_mcp("host_get", limit=3)
        final_prompt = f"Resuma o status desses hosts do Zabbix:\n{data}"
    elif decision == "trigger_get":
        data = call_mcp("trigger_get", limit=3)
        final_prompt = f"Descreva os triggers ativos do Zabbix:\n{data}"
    else:
        final_prompt = f"Responda normalmente como um analista SOC sobre: {user_msg}"
    try:
        response_text = ask_deepseek(final_prompt)
    except Exception as e:
        response_text = f"[ERRO] Falha ao gerar resposta: {e}"

    return jsonify({"response": response_text})


# ===================== Execução =====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)