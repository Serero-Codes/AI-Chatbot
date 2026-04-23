"""
Health Buddy - Flask Backend
Powered by Groq (LLaMA 3.1) with conversation memory
"""

import os
import re
from flask import Flask, request, jsonify, render_template, session
from groq import Groq
from dotenv import load_dotenv

# ─────────────────────────────────────────────
# Load environment variables
# ─────────────────────────────────────────────
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "health-buddy-secret-key-change-in-production")

# ─────────────────────────────────────────────
# Groq Client Setup
# ─────────────────────────────────────────────
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ─────────────────────────────────────────────
# System Prompt
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """
You are a professional, polite, and empathetic Health Buddy chatbot. Your purpose is to assist users with
medical guidance in a safe, informative, and supportive way.

Rules:
1. Always ask the user about the symptoms, sickness, or disease they want help with before providing any advice.
2. Ask relevant background information (such as age, gender, medical history, lifestyle) when necessary to better understand the possible causes.
3. Provide:
   - Possible causes of the reported sickness or symptoms.
   - General medical suggestions.
   - Diet and lifestyle tips to improve health.
4. Always clarify that your advice is informational only and does not replace professional medical consultation.
5. Focus strictly on medical assistance. Do not answer questions unrelated to health, medicine, or wellbeing.
6. If the user asks an out-of-scope or non-medical question, politely respond that you are only here as a Health Buddy focused on medical guidance.
7. Maintain a professional, friendly, and empathetic tone at all times.
8. Avoid making definitive diagnoses or prescribing exact medications unless discussing general over-the-counter guidance with a cautionary note.

Formatting Rules (VERY IMPORTANT):
- Always format your responses with clear spacing and structure.
- Use blank lines between paragraphs and sections.
- Use short, clearly separated paragraphs — never one long block of text.
- When listing items (causes, tips, suggestions), place each item on its own line with a dash or number.
- Keep sentences clear and easy to read.
- End responses with a warm, supportive closing line when appropriate.
"""


# ─────────────────────────────────────────────
# Helper: Format bot reply for clean readability
# ─────────────────────────────────────────────
def format_reply(text: str) -> str:
    """
    Cleans up the raw LLM response to ensure consistent
    paragraph spacing and readable structure.
    """

    # Normalize Windows-style line endings
    text = text.replace("\r\n", "\n")

    # Ensure double newlines before numbered or bulleted list items
    text = re.sub(r"\n(\d+\.\s)", r"\n\n\1", text)
    text = re.sub(r"\n(-\s)", r"\n\n\1", text)

    # Collapse more than two consecutive blank lines into exactly two
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text


# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Serve the main chat page."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    Accepts a user message, appends it to the session conversation history,
    calls the Groq API, formats the reply, and returns it as JSON.
    """

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided."}), 400

    user_message = data["message"].strip()

    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    # ── Initialize conversation history in session if not present ──
    if "messages" not in session:
        session["messages"] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    # ── Append the new user message ──
    session["messages"].append({
        "role": "user",
        "content": user_message
    })

    # Flask sessions need explicit flag to save mutable objects
    session.modified = True

    try:
        # ── Call Groq API ──
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=session["messages"],
            temperature=0.7,
            max_tokens=1024
        )

        raw_reply = response.choices[0].message.content

        # ── Format for readability ──
        formatted_reply = format_reply(raw_reply)

        # ── Append assistant reply to history ──
        session["messages"].append({
            "role": "assistant",
            "content": formatted_reply
        })

        session.modified = True

        return jsonify({
            "reply": formatted_reply,
            "status": "ok"
        })

    except Exception as e:
        error_message = f"Sorry, I encountered an error: {str(e)}"
        return jsonify({"error": error_message}), 500


@app.route("/reset", methods=["POST"])
def reset():
    """Clears the conversation history from the session."""
    session.pop("messages", None)
    return jsonify({"status": "ok", "message": "Conversation reset."})


@app.route("/history", methods=["GET"])
def history():
    """Returns the current conversation history (excluding system prompt)."""
    messages = session.get("messages", [])
    # Filter out the system message before returning to frontend
    visible = [m for m in messages if m["role"] != "system"]
    return jsonify({"history": visible})


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)
