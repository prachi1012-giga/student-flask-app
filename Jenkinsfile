pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps { checkout scm }
        }
        stage('Install Dependencies') {
            steps { sh 'pip install -r requirements.txt' }
        }
        stage('Test Application') {
            steps { sh 'python -m py_compile app.py' }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t student-flask-app .' }
        }
        stage('Deploy Application') {
            steps {
                sh 'docker stop student-app || true'
                sh 'docker rm student-app || true'
                sh 'docker run -d -p 5000:5000 --name student-app student-flask-app'
            }
        }
    }
}
```[cite: 6, 7]

---

## 🖥️ Tomorrow's Exam: Step-by-Step Jenkins Guide

Exam room me PC par Jenkins khula hoga (ya browser me `http://localhost:8080` kholna hoga)[cite: 5, 6]. 

### STEP 1: New Item Banayein
1. Jenkins ke Dashboard pe **Left Side Top** par **`New Item`** likha hoga, uspe click kar[cite: 6].
2. **Enter an item name** waale box me likh: `student-flask-app`[cite: 6]
3. Niche option dikhenge, usme **`Pipeline`** wale option pe click kar (Radio button dot ho jayega)[cite: 6].
4. Niche **`OK`** button daba de[cite: 6].

---

### STEP 2: GitHub Repo Connect Karein (Main Step)
Ek naya Configuration page khulega. 

1. Mouse se **bilkul niche scroll kar** jab tak **`Pipeline`** section na aa jaye[cite: 6].
2. **Definition** ke samne ek dropdown box hoga (jisme "Pipeline script" likha hoga). Us dropdown pe click karke select kar:
   👉 **`Pipeline script from SCM`**[cite: 6]
3. Ek naya option aayega **SCM**. Us dropdown me select kar:
   👉 **`Git`**[cite: 6]
4. Ab **`Repository URL`** ka box dikhega. Wahan apne GitHub Repository ka link paste kar de:
   ```text
   https://github.com/YOUR-USERNAME/student-flask-app.git
   ```[cite: 3, 6]
5. Niche **Branch Specifier** check kar, wahan `*/main` ya `*/master` hona chahiye (Jo tere GitHub ka main branch ho, usually `*/main` hota hai)[cite: 6].
6. Niche **Script Path** me check kar ki **`Jenkinsfile`** likha hai ya nahi (Ye by default `Jenkinsfile` hi likha rehta hai)[cite: 6].
7. Bilkul niche jaakar green/blue **`Save`** button daba de[cite: 7]!

---

### STEP 3: Pipeline Run (Build) Karein
`Save` dabate hi tu apne Project Page pe aa jayega.

1. Left Menu me ek button dikhega: **`Build Now`**[cite: 7].
2. **`Build Now`** par click kar de[cite: 7]!
3. Left me niche **Build History** me `#1` karke ek circle ghoomne lagega[cite: 7].
4. Page ke beech me tujhe Stage View dikhega:
   * **Checkout Code** 🟢
   * **Install Dependencies** 🟢
   * **Test Application** 🟢
   * **Build Docker Image** 🟢
   * **Deploy Application** 🟢

Saare boxes **Green** ho jayenge!

---

### STEP 4: Output / Logs Examiner ko Kaise Dikhyen?
Agar examiner bole "Logs dikhao":

1. Left side me **Build History** me `#1` pe click kar.
2. Left menu me **`Console Output`** pe click kar.
3. Tujhe scroll karne par **`SUCCESS`** likha hua dikh jayega[cite: 7]!

---

### 💡 Quick Recap (Mind Map for Exam)
* **GitHub**: `app.py` + `Dockerfile` + `requirements.txt` + `Jenkinsfile`[cite: 2, 6]
* **Jenkins**: `New Item` ➔ `Pipeline` ➔ `Pipeline script from SCM` ➔ `Git` ➔ URL Paste ➔ `Save` ➔ `Build Now`[cite: 6, 7]

Bas itna hi hai, tu easily full marks score karega! All the best for tomorrow! 👍
