🌱 ESG Dashboard

An ESG (Environmental, Social, Governance) Dashboard built using:

- React.js
- Django REST Framework
- PostgreSQL
- Recharts

This application allows users to upload CSV files containing utility, fuel, or travel data and generates ESG metrics such as CO₂ emissions and ESG scores.

---

* Features

✅ CSV Upload  
✅ ESG Score Calculation  
✅ CO₂ Emissions Tracking  
✅ Utility Data Processing  
✅ Travel Data Processing  
✅ ESG Dashboard UI  
✅ Interactive Charts using Recharts  
✅ Django REST API Backend  
✅ React Frontend  

---

# 🛠 Tech Stack

## Frontend
- React.js
- Recharts

## Backend
- Django
- Django REST Framework

## Database
- PostgreSQL

---

# 📂 Supported CSV Formats

## Utility Data

Example columns:

`csv
KWH
12000
15000

*Backend runs on:
http://127.0.0.1:8000

*Frontend Setup
cd esg-dashboard
npm install
npm start

Frontend runs on:
http://localhost:3000

Utility Emissions
CO₂ = KWH × emission factor
Travel Emissions
CO₂ = Distance_KM × 0.15
ESG Score
ESG Score = 100 - (emissions / 10)
 API Endpoints
Upload CSV
POST /api/companies/upload/
Company List
GET /api/companies/
ESG History
GET /api/companies/history/<company_id>/


Screenshots
Dashboard
<img width="1886" height="853" alt="image" src="https://github.com/user-attachments/assets/b87def3c-a213-4fc6-aaae-284647dd15de" />
backend
<img width="1247" height="637" alt="image" src="https://github.com/user-attachments/assets/0ae5cb74-3b71-4118-9258-f49d9beccb76" />


ESG Results and Chart Visualization
<img width="1322" height="599" alt="image" src="https://github.com/user-attachments/assets/44aeb7b6-4369-4329-a01c-7fb4b2555e0b" />
<img width="1311" height="599" alt="image" src="https://github.com/user-attachments/assets/8729dbf4-e1c0-4813-b076-e1b51ab01ba9" />
<img width="1335" height="600" alt="image" src="https://github.com/user-attachments/assets/4b4c17c9-ae42-4ba4-8be5-a4ec13720cca" />

Backend Deployment:
https://esg-backend-4uo5.onrender.com/





