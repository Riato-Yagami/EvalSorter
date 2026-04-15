# 📄 EvalSorter

Outil Python pour **trier automatiquement des copies scannées (PDF)** par élève, avec une interface rapide et un système d’auto-complétion basé sur les listes de classe.

---

## 🚀 Fonctionnalités

* 📂 Parcourt automatiquement les PDFs dans `input/`
* 🧠 Détection automatique de la classe depuis le nom du fichier (`B.6C`, `6A`, etc.)
* 👥 Chargement des élèves depuis `input/classes/`
* ✏️ Saisie assistée avec **auto-complétion en temps réel**
* 🚫 Évite les doublons (élèves déjà traités exclus)
* 🔁 Reprise automatique si interruption
* 💾 Sauvegarde immédiate des pages
* ⚡ Mode rapide (affichage PDF) ou mode image (OCR/debug)

---

## 📁 Structure du projet

```
EvalSorter/
│
├── main.py
├── config.py
│
├── src/
│   ├── core/
│   │   ├── pdf/
│   │   ├── image/
│   │
│   ├── utils/
│
├── input/
│   ├── classes/
│   │   ├── 6C.txt
│   │   ├── B.6C.txt
│   │
│   ├── E-3-B.6C.pdf
│
├── output/
└── tesseract/
```

---

## 🧑‍🏫 Format des listes de classe

Dans `input/classes/6C.txt` :

```
PESIN jules
VINCENT jean-adrien
MOKTAR-ABDIRASHIID anas
```

👉 Format attendu :

```
NOM prénom
```

---

## ⚙️ Configuration

Dans `config.py` :

```python
VIEW_MODE = "pdf"   # "pdf" (rapide) ou "image"
PDF_DPI = 150       # utilisé en mode image
```

---

## ▶️ Utilisation

```bash
python main.py
```

---

## 🖥 Interface

Pendant l’exécution :

```
📄 Traitement : E-3-B.6C.pdf
🖥 Mode affichage : pdf
⏩ Reprise à la page 21
📄 Page 21 / 30

✏️ Nom prénom :
```

👉 Fonctionnalités :

* suggestions en direct pendant la frappe
* `Entrée` → valide la première suggestion
* `Ctrl+C` → arrêt propre + sauvegarde

---

## 📦 Sortie

Les fichiers sont générés dans :

```
output/NOM_DU_PDF/
```

Exemple :

```
E-3-B.6C-MOKTAR_anas.pdf
E-3-B.6C-VINCENT_jean-adrien.pdf
```

---

## 🔁 Reprise automatique

Si le programme est interrompu :

* les pages déjà traitées sont détectées
* les élèves déjà faits sont exclus
* reprise automatique à la bonne page

---

## ⚡ Modes d’affichage

### 🟢 Mode PDF (recommandé)

* rapide
* fluide
* affichage natif

### 🟡 Mode image

* plus lent
* utile pour OCR/debug

---

## 📦 Création d’un exécutable

Avec **PyInstaller** :

```bash
pyinstaller --onefile main.py
```

---

## 💡 Améliorations possibles

* sélection des suggestions avec ↑ ↓
* estimation du temps restant
* interface graphique
* export Excel des élèves
* détection automatique du nom (OCR)

---

## 🧠 Philosophie

Cet outil est conçu pour :

* gagner du temps en correction
* éviter les erreurs de saisie
* rester simple, rapide et robuste

---

## 👨‍💻 Auteur

Projet personnel pour automatiser la gestion de copies en classe.

---

## 📜 Licence

Libre d’utilisation et modification.
