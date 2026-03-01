# study-assistant

En enkel prototype av en AI-studieassistent med Python-backend, HTML/JavaScript-frontend og OpenAI API.

## Prosjektstruktur

```text
study-assistant/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── app.js
    └── style.css
```

## 1) Installer avhengigheter

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) Sett OpenAI API-nøkkel

```bash
export OPENAI_API_KEY="din_api_nøkkel"
```

Tips: legg linjen i `~/.bashrc` eller bruk en `.env`-løsning senere.

## 3) Start serveren lokalt

```bash
python app.py
```

Åpne deretter: <http://127.0.0.1:5000>

## Hvordan appen fungerer

- Studenten skriver spørsmål/tema i chatfeltet.
- Backend sender meldingen til OpenAI med en systemprompt som styrer formatet.
- AI svarer i seksjoner:
  - Forklaring
  - Sammendrag
  - Flashcards (5 stk)
  - Mini-quiz (3 spørsmål)

## API-endepunkt

- `POST /api/chat`
  - Request body: `{ "message": "Forklar fotosyntese" }`
  - Response body: `{ "reply": "...formatert AI-svar..." }`
