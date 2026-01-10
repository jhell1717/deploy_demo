import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor

X = np.random.uniform(-10,10,(5000,1))
y = y = 3*X[:,0]**2 + 2*X[:,0] + 5 + np.random.normal(0, 5, 5000)

model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("Model trained and saved")
