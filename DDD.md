# Domain Driven Design

## Opis zadania

Zadanie polega na zamodelowaniu bezpiecznej aplikacji bankowej wykorzystującej zasady Domain Driven Design. Model ten składać powienien się z Bounded Context, Agregatów, Encji i Objektów Wartości. Dla tych obiektów powinny być zdefiniowane również atrybuty i akceptowane formaty danych.

## Model

![image](https://github.com/Matixx22/task1/assets/52577030/5d5230f2-ceff-4312-8ba7-0f94cb8d1c99)


## Założenia

Założenia dotyczące budowy konkretnych encji i obiektów wartości są przedstawione w modelu.

Formaty danych:
- Ulica (string)
- Miejscowość (string)
- Poczta (regex kodu pocztowego)
- Nazwa (string)
- Rodzaj (user defined string, enum)
- Oferta (string)
- Nr telefonu (universal phone number format string)
- Adres email (email address format string)
- Nr konta (account number format string)
- Saldo (float, number)
- Historia (user defined history object, list)
- Docelowy nr konta (account number format string)
- Kwota (float, number)
- Data (universal date format)
- Nr karty (universla banking card format)
- Limity (list of banking card limits)
- Karta płatnicza (banking card entity object)
