[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23574048&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** 26ai.lycd@vinuni.edu.vn
**Student ID:** 2A202600356  
**Name:** Cao Diệu LY
---

## Mo ta

Lab nay minh xay dung mot ETL pipeline don gian (Extract -> Validate -> Transform -> Load):
- Extract: doc du lieu tu `raw_data.json`
- Validate: loai record khong hop le (price <= 0, category rong)
- Transform: chuan hoa `category` (Title Case), tinh `discounted_price = price * 0.9`, them cot `processed_at`
- Load: luu ket qua ra `processed_data.csv`

Ngoai ra minh chay stress test bang `agent_simulation.py` de so sanh hanh vi cua AI agent khi dung du lieu **clean** vs **garbage/poisoned**.

---

## Cach chay (How to Run)

### Prerequisites
```bash
pip install pandas
```

### Chay ETL Pipeline
```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)
1) Tao du lieu rac (poisoned):
```bash
python generate_garbage.py
```
2) Chay agent voi 2 bo du lieu:
```bash
python agent_simulation.py
```

---

## Cau truc thu muc

```
solution.py              # ETL Pipeline script
raw_data.json            # Input
processed_data.csv       # Output cua pipeline
experiment_report.md     # Bao cao thi nghiem
agent_simulation.py      # Stress test agent (clean vs garbage)
generate_garbage.py      # Tao garbage_data.csv (poisoned)
README.md                # File nay
```

---

## Ket qua

- ETL: Doc 5 records tu `raw_data.json`, loai 2 records khong hop le (1 record co `price <= 0`, 1 record co `category` rong), con lai 3 records hop le va ghi ra `processed_data.csv`.
- Stress test (agent):
  - Clean data: agent chon san pham hop ly (Laptop).
  - Garbage/poisoned data: agent bi dan dat boi outlier gia rat lon va chon "Nuclear Reactor".

