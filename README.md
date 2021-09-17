# Technika Programowania
![alt text](https://github.com/iwnlMski/TechnikaProgramowania3/blob/master/readmeimg/TP3image1.PNG?raw=true)

### Projekt numer 4
### Autor projektu: Seweryn Majewski ACiR WETI 2sem. Indeks: 181675
### Użyta technologia: Python

### Dokumentacja:
### 1. Działanie programu: 
Celem programu jest wizualizajca działania windy, w dwóch wymiarach.
Zaimplementowałem takie funkcjonalności jak algorytm priorytetow windy,
możliwość zdefiniowania ilości osób wsiadających i wysiadających, 
ekran pokazujący obecną sumaryczną wagę pasażerów i inne

#### a. Funkcje rysujące
##### (void) draw_building - rysuje budynek wokół windy
##### (void) draw_elevator - funkcja ta przyjmuje arugmenty o obecnym położeniu windy,
##### o masie pasażerów oraz o ilości klatek programu
##### (void) draw_buttons - funckja ta rysuje wszystkie przyciski znajdujace sie w programie
##### (void) draw_window - funkcja ta wypelnia okno białem kolorem i wywołuje rysowanie budynku i przycisków
##### (void) draw_amount_of_people_waiting - funckja przymuje hashmape jako argument i rysuje 
##### aktualne informacje o tym ile uzytkownik chce wybrac osob na danym pietrze

#### b. Funckja główna - main()
Ta funckja pełni rolą głównego silnika programu gdyż definiuje wartości początkowe oraz stałe,
które będą używane w całym programie. Główną częścią kodu w funkcji main jest pętla while,
gdzie wykonuje się cała logika związana z odświeżaniem programu, dodawaniem i usuwaniem pasażerów,
otrzymywaniem inputu od użytkownika czy też odliczaniem czasu do zjazdu pustej windy na parter


#### c. Funkcja wyznaczania priorytetu windy - add_to_queue()
Funckja ta jest odpowiedzialna za jeden z najważniejszych elementów programu, czyli wyznaczanie
kolejności w jakiej winda ma poruszać się po piętrach. Zastosowałem w niej algorytm typowy dla wind
który został również użyty w dyskach twardych z tego samego powodu

#### d. Klasy w programie
##### Klasa Person - definiuje i inicjalizuje wszystkie potrzebne parametry każdej danej osoby
##### wygenerowanej przez uzytkownika. KLasa ta również implementuje metode zmieniającą status pasażera
##### Klasa Level - została stworzona z myślą o łatwym przechowywaniu danych dotyczących każdego piętra
##### dzięki niej dużo łatwiej odwołać się do numeru piętra i jednocześnie do jego położenia w osi Y

### 2. GUI
![alt text](https://github.com/iwnlMski/TechnikaProgramowania3/blob/master/readmeimg/TP3image2.PNG?raw=true)
#
Po włączeniu programu jedynym włączonym przyciskiem jest przycisk “Submit”, który
przekazuję do programu liczbę wpisaną obok. Liczba ta jest liczbą linii pliku które chcemy
pominąć. 
#
![alt text](https://github.com/iwnlMski/TechnikaProgramowania3/blob/master/readmeimg/TP3image3.PNG?raw=true)
#
Po wpisaniu poprawnej wartości podśwetlają się dodatkowe przyciski. W tym momencie
możemy dostosować szybkośc symulacji oraz przybliżenie wykresu. Warto dodać iż gdy
klikniemy “Run”, nie będziemy w stanie tego już zmienić aż do zakończenia symulacji albo
zakończenia programu. 

