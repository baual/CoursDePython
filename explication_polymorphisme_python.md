# Le polymorphisme en Python

Le **polymorphisme** est un concept fondamental de la programmation orientée objet (POO).

Il permet d'utiliser une même interface pour différents objets, ce qui rend le code plus flexible, extensible et maintenable.

---

## Le code étudié

```python
class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        print("Wouf!")

class Chat(Animal):
    def parler(self):
        print("Miaou!")

def faire_parler(animal):
    animal.parler()

faire_parler(Chien())  # Affiche "Wouf!"
faire_parler(Chat())   # Affiche "Miaou!"
```

---

## 1. La classe de base `Animal`

```python
class Animal:
    def parler(self):
        pass
```

Cette classe représente un concept générique d'animal.

La méthode `parler()` définit un comportement attendu pour tous les animaux.

Le mot-clé `pass` signifie :

> « Ne rien faire pour l'instant. »

Cette méthode sert de modèle que les classes dérivées devront redéfinir.

On peut l'interpréter ainsi :

> Tous les animaux savent parler, mais chacun à sa façon.

---

## 2. La classe `Chien`

```python
class Chien(Animal):
```

La classe `Chien` hérite de la classe `Animal`.

Cela signifie que :

- un chien est un animal ;
- il récupère les attributs et les méthodes de `Animal` ;
- il peut modifier certains comportements.

Ici, il redéfinit la méthode `parler()` :

```python
def parler(self):
    print("Wouf!")
```

Si l'on exécute :

```python
chien = Chien()
chien.parler()
```

le résultat est :

```text
Wouf!
```

---

## 3. La classe `Chat`

```python
class Chat(Animal):
```

La classe `Chat` hérite également de `Animal`.

Elle redéfinit elle aussi la méthode `parler()` :

```python
def parler(self):
    print("Miaou!")
```

Ainsi :

```python
chat = Chat()
chat.parler()
```

produit :

```text
Miaou!
```

---

## 4. La fonction polymorphe

```python
def faire_parler(animal):
    animal.parler()
```

Cette fonction accepte un paramètre nommé `animal`.

Elle ne sait pas si l'objet reçu est :

- un `Chien` ;
- un `Chat` ;
- ou un autre type d'animal.

Elle sait seulement que l'objet possède une méthode `parler()`.

Elle exécute simplement :

```python
animal.parler()
```

---

## 5. Premier appel

```python
faire_parler(Chien())
```

### Étape 1 : création de l'objet

```python
Chien()
```

### Étape 2 : transmission à la fonction

```python
faire_parler(Chien())
```

### Étape 3 : appel de la méthode

La fonction exécute :

```python
animal.parler()
```

Python constate que `animal` est un objet de type `Chien`. Il appelle donc :

```python
Chien.parler()
```

Résultat :

```text
Wouf!
```

---

## 6. Second appel

```python
faire_parler(Chat())
```

La fonction exécute de nouveau :

```python
animal.parler()
```

Cette fois, `animal` est un objet de type `Chat`. Python appelle donc :

```python
Chat.parler()
```

Résultat :

```text
Miaou!
```

---

## 7. Pourquoi parle-t-on de polymorphisme ?

Le polymorphisme signifie :

> Une même instruction peut produire des comportements différents selon le type réel de l'objet manipulé.

La ligne suivante est identique dans tous les cas :

```python
animal.parler()
```

Pourtant, le résultat varie :

| Type réel de l'objet | Méthode exécutée | Résultat |
|---|---|---|
| `Chien` | `Chien.parler()` | `Wouf!` |
| `Chat` | `Chat.parler()` | `Miaou!` |

La méthode appelée est choisie dynamiquement lors de l'exécution.

---

## 8. Ajout d'un nouvel animal

Supposons que l'on ajoute une vache :

```python
class Vache(Animal):
    def parler(self):
        print("Meuh!")
```

On peut immédiatement écrire :

```python
faire_parler(Vache())
```

Résultat :

```text
Meuh!
```

Aucune modification n'est nécessaire dans la fonction :

```python
def faire_parler(animal):
    animal.parler()
```

C'est l'un des grands avantages du polymorphisme.

---

## 9. Comparaison avec une approche non polymorphe

Sans polymorphisme, on pourrait écrire :

```python
def faire_parler(animal):
    if isinstance(animal, Chien):
        print("Wouf!")
    elif isinstance(animal, Chat):
        print("Miaou!")
```

### Inconvénient

À chaque ajout d'un nouvel animal, il faudrait modifier la fonction `faire_parler()` pour gérer ce nouveau cas.

Avec le polymorphisme, la fonction reste inchangée :

```python
def faire_parler(animal):
    animal.parler()
```

---

## 10. Principe fondamental

Grâce au polymorphisme, on programme en utilisant une **interface commune** :

```python
parler()
```

plutôt qu'en dépendant de types particuliers :

```text
Chien
Chat
Vache
```

Cela rend le programme :

- plus extensible ;
- plus facile à maintenir ;
- moins dépendant des classes concrètes ;
- plus simple à faire évoluer.

---

## Résumé visuel

```text
                 Animal
                    │
        ┌───────────┴───────────┐
        │                       │
      Chien                   Chat
        │                       │
    parler()                parler()
        │                       │
      Wouf!                  Miaou!

                    │
                    ▼

          faire_parler(animal)
              animal.parler()
```

Une seule fonction :

```python
animal.parler()
```

Plusieurs comportements possibles :

```text
Chien  → Wouf!
Chat   → Miaou!
Vache  → Meuh!
```

C'est exactement cela, le **polymorphisme**.
