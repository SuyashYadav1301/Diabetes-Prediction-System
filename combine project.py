import os
from pathlib import Path
from django.conf import settings
from django.urls import path
from django.shortcuts import render
from django.core.management import execute_from_command_line
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Configure Django settings
BASE_DIR = Path(__file__).resolve().parent
settings.configure(
    DEBUG=True,
    SECRET_KEY="django-insecure-+@pi&%4=xn&bx*=ryy7w+#44$dmf0!okqq0d7qmt-k=07s24z(",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ],
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.security.SecurityMiddleware",
    ],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.request",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        }
    ],
)

# Views
def home(request):
    return render(request, "home.html")


def predict(request):
    return render(request, "predict.html")


def result(request):
    # Load dataset
    data = pd.read_csv("diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Train Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)

    # Get user inputs
    vals = [float(request.GET.get(f"n{i}", 0)) for i in range(1, 9)]
    pred = model.predict([vals])

    # Generate result
    result_text = "Positive" if pred == [1] else "Negative"
    return render(request, "predict.html", {"result2": result_text})


# URL patterns
urlpatterns = [
    path("", home),
    path("predict/", predict),
    path("predict/result/", result),
]

# Templates
TEMPLATE_HOME = """
<!DOCTYPE html>
<html>
<head>
    <title>Diabetes Prediction</title>
</head>
<body>
    <h1>Welcome to Diabetes Prediction</h1>
    <a href="/predict/">Predict Diabetes</a>
</body>
</html>
"""

TEMPLATE_PREDICT = """
<!DOCTYPE html>
<html>
<head>
    <title>Predict Diabetes</title>
</head>
<body>
    <h1>Diabetes Prediction Form</h1>
    <form action="/predict/result/" method="get">
        <label for="n1">Glucose Level:</label><input type="text" name="n1"><br>
        <label for="n2">Blood Pressure:</label><input type="text" name="n2"><br>
        <label for="n3">Skin Thickness:</label><input type="text" name="n3"><br>
        <label for="n4">Insulin Level:</label><input type="text" name="n4"><br>
        <label for="n5">BMI:</label><input type="text" name="n5"><br>
        <label for="n6">Diabetes Pedigree Function:</label><input type="text" name="n6"><br>
        <label for="n7">Age:</label><input type="text" name="n7"><br>
        <label for="n8">Other Factor:</label><input type="text" name="n8"><br>
        <button type="submit">Predict</button>
    </form>
    {% if result2 %}
    <h2>Prediction Result: {{ result2 }}</h2>
    {% endif %}
</body>
</html>
"""

# Create required folders and files
os.makedirs(BASE_DIR / "templates", exist_ok=True)
with open(BASE_DIR / "templates/home.html", "w") as f:
    f.write(TEMPLATE_HOME)
with open(BASE_DIR / "templates/predict.html", "w") as f:
    f.write(TEMPLATE_PREDICT)

# Main entry point
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    execute_from_command_line(["manage.py", "runserver"])