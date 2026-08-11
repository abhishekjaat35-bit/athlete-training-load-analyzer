# 📊 Athlete Training Load Analyzer

A Python sports-data analytics project that analyzes athlete training sessions using **Pandas** and the **session-RPE (sRPE) method**.

This is **Day 8** of my Sports Performance & Sports Data Analytics Python portfolio.

---

## 🎯 Project Objective

The purpose of this project is to transform training-session data into useful athlete and team-level training-load information.

The program analyzes:

- Training duration
- Session RPE (sRPE)
- Session training load
- Total athlete load
- Average athlete load
- Average RPE
- Total training duration
- Session-type load
- Daily team training load
- Athlete load ranking

---

## 📊 Data Flow

```text
Training Session CSV
        ↓
      Pandas
        ↓
Data Cleaning & Conversion
        ↓
Session-RPE Training Load
        ↓
Athlete-Level Analysis
        ↓
Session-Type Analysis
        ↓
Daily Team Load
        ↓
Athlete Ranking
        ↓
Training Load Report
```

---

## 🧮 Training Load Formula

This project uses a simple session-RPE method:

```text
Training Load = Session Duration × Session RPE
```

Example:

```text
Duration = 75 minutes
sRPE = 7

Training Load = 75 × 7
              = 525 AU
```

Where:

```text
AU = Arbitrary Units
```

---

## 📁 Project Structure

```text
athlete-training-load-analyzer/
│
├── training_load_analyzer.py
├── training_data.csv
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🗂️ Dataset

The project uses a small **synthetic dataset** containing athlete training sessions.

### Variables

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Date | Training-session date |
| Session_Type | Type of training |
| Duration_min | Session duration in minutes |
| sRPE | Session rating of perceived exertion |
| Training_Load | Calculated session load |

Example:

```csv
Athlete,Date,Session_Type,Duration_min,sRPE
Rahul,2026-08-03,Strength,75,7
Rahul,2026-08-04,Speed,60,8
Rahul,2026-08-05,Recovery,45,3
```

The dataset contains **synthetic data only** and does not represent real athletes.

---

## 🐍 Python Technologies

This project uses:

- Python
- Pandas
- CSV data
- DataFrames
- `groupby()`
- `agg()`
- `sort_values()`
- `to_datetime()`
- Data filtering
- Statistical summaries

---

## ▶️ Installation

Install Pandas:

```bash
pip install pandas
```

Verify the installation:

```bash
python -c "import pandas; print(pandas.__version__)"
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/athlete-training-load-analyzer.git
```

Enter the project directory:

```bash
cd athlete-training-load-analyzer
```

Run the program:

```bash
python training_load_analyzer.py
```

---

## 📈 Analysis Performed

### 1. Session Training Load

Each training session receives a training-load score:

```text
Duration × sRPE
```

---

### 2. Team Training Load

The program calculates:

```text
Total Team Load
Average Session Load
Highest Training-Load Session
```

---

### 3. Athlete Analysis

For each athlete, the program calculates:

```text
Number of Sessions
Total Training Load
Average Training Load
Average RPE
Total Training Duration
```

---

### 4. Athlete Ranking

Athletes are ranked according to their total training load:

```text
1. Highest total load
2. Second highest
3. Third highest
```

This provides a simple comparison of accumulated external training stress as represented by the selected sRPE model.

---

### 5. Session-Type Analysis

Training load is grouped according to:

```text
Strength
Speed
Recovery
Conditioning
```

This allows comparison of the contribution of different session types to the overall training load.

---

### 6. Daily Training Load

The program aggregates training load by date to identify changes in the team's daily training demand.

---

## 💻 Example Output

```text
======================================================================
             ATHLETE TRAINING LOAD ANALYZER
======================================================================

TRAINING SESSION DATA
======================================================================

...

======================================================================
TEAM TRAINING LOAD SUMMARY
======================================================================
Total Training Load  : ...
Average Session Load : ...
Highest Load Session : ...

======================================================================
ATHLETE TRAINING LOAD SUMMARY
======================================================================

...

======================================================================
ATHLETE LOAD RANKING
======================================================================

1. ...
2. ...
3. ...

======================================================================
SESSION TYPE ANALYSIS
======================================================================

...

======================================================================
DAILY TEAM TRAINING LOAD
======================================================================

...

======================================================================
ANALYSIS COMPLETE
======================================================================
```

---

## 🔬 Sports Science Application

Training-load monitoring is commonly used to help coaches and sport scientists understand the amount and distribution of training performed by athletes.

Potential applications include:

- Strength & conditioning monitoring
- Team training monitoring
- Conditioning-load tracking
- Weekly workload analysis
- Training-session comparison
- Athlete monitoring dashboards
- Periodization analysis

---

## ⚠️ Scientific Limitations

The session-RPE method is a **simple internal-load monitoring approach**.

The calculated value should not be interpreted as a direct physiological measurement of training stress.

This project does not currently account for:

- Heart-rate data
- GPS distance
- High-speed running
- Accelerations/decelerations
- Player-load metrics
- Velocity data
- Wellness/readiness
- Acute and chronic workload models
- Individual physiological thresholds

Therefore, the project is intended for **educational programming and sports-data analytics practice**.

---

## 🚀 Future Improvements

Planned improvements:

- [ ] Add Pandas data validation
- [ ] Add missing-data detection
- [ ] Add weekly training load
- [ ] Add rolling averages
- [ ] Add training-load trends
- [ ] Add acute workload
- [ ] Add acute workload
- [ ] Add monotony calculations
- [ ] Add strain calculations
- [ ] Add heart-rate data
- [ ] Add GPS data
- [ ] Add wellness scores
- [ ] Add Matplotlib visualizations
- [ ] Create an athlete dashboard
- [ ] Build an automated athlete-monitoring system

---

## 🧠 Skills Learned

After completing this project, I practiced:

```text
Python
   ↓
CSV Data
   ↓
Pandas
   ↓
DataFrames
   ↓
Data Transformation
   ↓
GroupBy Analysis
   ↓
Training-Load Calculation
   ↓
Sports Performance Analytics
```

---

## 👨‍💻 Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📌 Project Status

**Day 8 — Completed ✅**