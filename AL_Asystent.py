from langchain_community.utilities import SQLDatabase
from langchain_ollama import ChatOllama
from langchain_community.agent_toolkits import create_sql_agent


path_to_db = r"C:\Users\Wiktoria\PyCharmMiscProject\Zasoby_IT\firma_it.db"
db = SQLDatabase.from_uri(f"sqlite:///{path_to_db}")


llm = ChatOllama(model="llama3:latest", temperature=0)


instrukcja = """Jesteś ekspertem SQL w firmie IT Wiktorii.
Twoja główna tabela nazywa się: Zasoby.
Kolumny w tej tabeli to: id, model, typ.

Zasady:
1. Pracuj wyłącznie na tabeli 'Zasoby'.
2. Zawsze najpierw sprawdź schemat tabeli (sql_db_schema).
3. Na koniec podaj odpowiedź po polsku.
"""


agent_executor = create_sql_agent(
    llm,
    db=db,
    agent_type="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True,
    prefix=instrukcja
)


print("--- ASYSTENT AI MAGAZYNU IT ONLINE ---")

while True:
    pytanie = input("\nO co chcesz zapytać? (lub wpisz 'koniec'): ")
    if pytanie.lower() in ['koniec', 'exit', 'quit']:
        break

    try:
        print("🤖 Analizuję bazę danych...")

        wynik = agent_executor.invoke({"input": pytanie})
        print(f"\n🤖 Odpowiedź: {wynik['output']}")

    except Exception as e:

        print("\n❌ WYKRYTO PROBLEM TECHNICZNY:")
        if "sensitive information" in str(e).lower():
            print("Model AI zablokował odpowiedź ze względów bezpieczeństwa. Spróbuj zadać pytanie inaczej.")
        else:
            print(f"Szczegóły: {e}")