# Heart Attack Prediction System (Tkinter + Machine Learning)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A **beautiful desktop application** built with **Tkinter** that predicts the risk of heart disease using a **Logistic Regression** model trained on the famous UCI Heart Disease dataset.

Live input → Real-time graphs → Instant prediction with visual report!

---

### Screenshots (Add these later – they make your repo 10x better!)

| Main Interface                  | Analysis Result (No Risk)         | Analysis Result (Risk Detected)   |
|----------------------------------|-----------------------------------|-----------------------------------|
| ![Main](screenshots/main.png)    | ![Safe](screenshots/safe.png)     | ![Risk](screenshots/risk.png)     |

> Tip: Take screenshots of your app running and put them in a folder called `screenshots/` inside the project.

---

### Features

- Clean & modern GUI using **Tkinter + custom images**
- Real-time **4 interactive graphs** showing patient parameters
- Input validation with helpful error messages
- Instant heart disease risk prediction
- Detailed **feature info window** explaining medical terms
- Smoking / Non-smoking toggle
- Save & Clear functionality ready

---

### Tech Stack

| Technology           | Purpose                          |
|----------------------|----------------------------------|
| Python               | Core language                    |
| Tkinter              | GUI framework                    |
| Pandas               | Data handling                    |
| scikit-learn         | Logistic Regression model        |
| Matplotlib           | Embedded live graphs             |
| NumPy                | Numerical operations             |

---

### Dataset

- Source: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease)
- 303 patient records
- 14 attributes (age, sex, cp, trestbps, chol, etc.)
- Target: 0 = No disease, 1 = Disease present

---

### How to Run the Project

```bash
# 1. Clone the repo (or this folder)
git clone https://github.com/lalitrajput11/ML-Projects.git
cd ML-Projects/Tkinter-ML-HeartAttack-Prediction

# 2. Install requirements
pip install pandas scikit-learn matplotlib numpy

# 3. Run the app
python main.py
Make sure heart.csv is in the same folder as main.py

Model Performance
textAccuracy on Training data : ~85.95%
Accuracy on Test data     : ~83.61%
(Trained with Logistic Regression, max_iter=1000)

Project Structure
textTkinter-ML-HeartAttack-Prediction/
├── main.py              → Main GUI + prediction logic
├── new.py               → Model training script (for testing)
├── heart.csv            → Dataset
├── Images/              → All UI icons & backgrounds
├── screenshots/         → (Recommended) Add your own screenshots
└── README.md            → This file

Future Enhancements (You can add these later!)

 Save patient reports as PDF
 Add more models (Random Forest, XGBoost)
 Dark mode toggle
 Export graphs as images
 Docker support


Author
Lalit Rajput
GitHub: @lalitrajput11
Portfolio-ready ML + GUI Project

Star this repo if you like it!
Helps a lot for job applications & college submissions

text### Next Steps (Do these now – takes 2 minutes)

1. Create a folder inside your project:  
   ```bash
   mkdir screenshots

Run your app → take 3 beautiful screenshots → save as main.png, safe.png, risk.png
Create/replace README.md with the content above
Commit & push:Bashgit add README.md screenshots/
git commit -m "Add awesome README with screenshots"
git push

Your project will instantly go from "normal" to "Wow, this guy knows what he's doing!" — perfect for internships, placements, and portfolio.
Want me to generate the screenshots folder structure or help you add PDF report saving next? Just say the word!
