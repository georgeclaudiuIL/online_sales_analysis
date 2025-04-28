# online_sales_analysis
proiect final introd to git and github

# Online Sales Analysis

## Descriere proiect
Acest proiect este o aplicație simplă de gestionare a vânzărilor online. Permite adăugarea, afișarea și gestionarea produselor, gestionarea unui coș de cumpărături și calcularea valorii totale a inventarului sau a coșului.

## Clase

### Product
- Atribute: `name`, `price`, `quantity`
- Metode:
  - `afisare_info()`: Afișează informațiile produsului.
  - `actualizare_cantitate()`: Actualizează cantitatea produsului.

### ProductManager
- Atribut: listă de produse (`products`).
- Metode:
  - `add_products()`: Adaugă produse noi în listă.
  - `show_products()`: Afișează toate produsele.
  - `total_value()`: Calculează valoarea totală a stocului.
  - `remove_product()`: Elimină un produs din listă după nume.

### Cart
- Atribut: listă de produse (`cart_items`).
- Metode:
  - `add_product_to_cart()`: Adaugă produse în coș.
  - `total_payment()`: Calculează valoarea totală de plată.
  - `show_cart_items()`: Afișează conținutul coșului.

## Funcționalități principale
- Gestionarea inventarului de produse.
- Calcularea valorii totale a inventarului.
- Crearea și gestionarea unui coș de cumpărături.
- Ignorarea fișierelor sensibile (`config.json`) și capturilor de ecran în Git.

---


