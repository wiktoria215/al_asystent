🤖 AI Inventory Agent – Lokalny Asystent SQL (RAG)
📝 Opis projektu

Projekt przedstawia inteligentnego asystenta bazy danych, który pozwala na komunikację z zasobami IT (plik SQLite) przy użyciu języka naturalnego. Zamiast pisać zapytania SQL, użytkownik zadaje pytania po polsku (np. „Który laptop jest najdroższy?”), a Agent AI samodzielnie planuje kroki, analizuje schemat bazy i generuje odpowiedź.

Jest to implementacja wzorca RAG (Retrieval-Augmented Generation) na danych strukturalnych, z naciskiem na prywatność danych poprzez wykorzystanie lokalnego modelu LLM.
🛠️ Tech Stack

    Python 3.11+

    LangChain – orkiestracja agenta i łańcuchów myślowych (Chain-of-Thought).

    Ollama (Llama 3) – lokalny silnik LLM zapewniający bezpieczeństwo danych.

    SQLite – relacyjna baza danych przechowująca zasoby firmy.

    SQLAlchemy – komunikacja między AI a bazą danych.

🚀 Kluczowe funkcjonalności

    Natural Language to SQL: Automatyczna translacja zapytań tekstowych na poprawny kod SQL.

    Pętla ReAct (Reasoning & Acting): Agent nie zgaduje – najpierw sprawdza listę tabel, potem ich strukturę, a dopiero na końcu wykonuje zapytanie.

    Local-First AI: Rozwiązanie działa w 100% offline, co jest kluczowe w pracy z wrażliwymi danymi firmowymi.

    Verbose Debugging: Widoczny proces myślowy AI, pozwalający na audyt decyzji podejmowanych przez model.

🧠 Czego się nauczyłam? (Troubleshooting)

Podczas pracy nad tym projektem rozwiązałam kilka zaawansowanych problemów typowych dla GenAI:

    Eliminacja pętli halucynacji: Gdy model Llama 3 wpadał w pętlę pytań o tabele, zoptymalizowałam System Prompt oraz parametry max_iterations, aby wymusić konkretne działanie.

    Output Parsing: Skonfigurowałam handle_parsing_errors, aby agent potrafił skorygować format swojej odpowiedzi, gdy model nie trzymał się rygorystycznego formatu LangChain.

    Local LLM Connectivity: Skonfigurowałam endpointy API dla lokalnego serwera Ollama, co pozwoliło na stabilną integrację z kodem Pythona.

📖 Jak uruchomić?

    Zainstaluj Ollama i pobierz model: ollama pull llama3.

    Zainstaluj biblioteki: pip install langchain langchain-ollama langchain-community.

    Upewnij się, że baza firma_it.db znajduje się w folderze projektu.

    Uruchom: python AL_Asystent.py.
