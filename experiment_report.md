# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** 2A202600356 
**Name:** Cao Diệu Ly 
**Date:** 2026-04-15

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent: Based on my data, the best choice is Laptop at $1200.0. | 9 | Du lieu clean nen gia/ten san pham hop ly, agent chon dung san pham gia tri cao. |
| Garbage Data (`garbage_data.csv`) | Agent: Based on my data, the best choice is Nuclear Reactor at $999999. | 2 | Du lieu bi garbage/poisoned (outlier gia rat lon), agent bi dan dat va chon san pham vo ly. |

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Voi garbage/poisoned data, chat luong du lieu khong con dang tin cay nen agent suy luan dua tren dau vao bi sai. Truong hop nay co mot outlier gia rat lon ($999999) gan voi san pham "Nuclear Reactor", lam cho quy tac chon "mon hang tot nhat/gia tri nhat" bi lech hoan toan. Neu du lieu co wrong data types (gia la chu, null/NaN), duplicate IDs, hoac category bi rong/sai chuan, thi agent (va ca cac buoc tong hop trong pipeline) de bi nham lan khi so sanh, sap xep hoac loc.

Quan trong nhat la outliers va records bi "poisoned" co the ap dao thong ke, dan den ket luan sai, du prompt co hay den dau. Vi vay quan sat/validate du lieu (range check, schema check, loai null, xu ly outlier) la bat buoc de agent on dinh va giam rui ro bi tan cong/nhieu du lieu.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** Dong y. Neu du lieu dau vao bi rac/poisoned thi agent se hoc va suy luan tren "su that gia", dan den quyet dinh sai. Prompt chi giup dien dat/huong dan, con do tin cay cua ket qua phu thuoc rat nhieu vao chat luong du lieu va cac buoc validate/monitor trong pipeline.

