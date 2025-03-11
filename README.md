# Beer-Recommendation-System
A hybrid recommendation system using user-based, item-based filtering, and Bayesian optimization.
# 🍺 Beer Recommendation System

##  Overview
A **hybrid recommendation system** using **user-based filtering, item-based filtering, and Bayesian optimization** to recommend beers to users.

##  Features
- **User-Based Filtering**: Recommends beers based on similar users' preferences.
- **Item-Based Filtering**: Suggests beers based on beer similarity.
- **Hybrid Model**: Combines both approaches with beer popularity for better accuracy.
- **Bayesian Optimization**: Optimizes weight parameters to improve recommendations.

## 📊 Performance Metrics
| Model               | RMSE  | MAE  |
|--------------------|------|------|
| User-Based        | 3.6741 | 3.6053 |
| Item-Based        | 3.6956 | 3.6207 |
| **Hybrid Model**  | **3.5727**  | **3.5056**  |


## ⚙️ Installation
Clone the repository:
```bash
git clone https://github.com/DeepShikhaM/Beer-Recommendation-System.git
cd Beer-Recommendation-System

pip install -r requirements.txt

jupyter notebook BeerMart.ipynb

```

For any questions or improvements, feel free to reach out!

