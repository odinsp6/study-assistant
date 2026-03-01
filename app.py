import os

from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)


SYSTEM_PROMPT = """
Du er en intelligent studieassistent for studenter.

Svar ALLTID på norsk og i disse seksjonene, i denne rekkefølgen:

Forklaring:
- Forklar temaet enkelt.
- Del opp i små steg.
- Tilpass nivået til en nybegynner med mindre studenten ber om noe annet.
- Bruk minst ett eksempel fra virkeligheten.

Sammendrag:
- Gi en kort punktliste med de viktigste poengene.

Flashcards:
- Lag nøyaktig 5 flashcards i formatet: "Spørsmål → Svar".

Mini-quiz:
- Lag nøyaktig 3 quizspørsmål uten fasit.
""".strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    user_message = (payload.get("message") or "").strip()

    if not user_message:
        return jsonify({"error": "Melding kan ikke være tom."}), 400

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return jsonify({"error": "OPENAI_API_KEY er ikke satt."}), 500

    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
        )

        answer = response.output_text.strip()
        if not answer:
            return jsonify({"error": "Ingen respons fra modellen."}), 502

        return jsonify({"reply": answer})
    except Exception as exc:  # noqa: BLE001
        return jsonify({"error": f"Kunne ikke hente svar fra OpenAI API: {exc}"}), 502


if __name__ == "__main__":
    app.run(debug=True)
