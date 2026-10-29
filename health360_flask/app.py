from flask import Flask, render_template

app = Flask(__name__)

TABLEAU_STORY_URL = (
    "https://public.tableau.com/views/"
    "Health360ComprehensiveHealthcareRiskDiseaseAnalytics_17929898861220/Story1"
    "?:language=en-GB&:showVizHome=no&:toolbar=yes"
)
TABLEAU_DASHBOARD_URL = (
    "https://public.tableau.com/views/"
    "Health360ComprehensiveHealthcareRiskDiseaseAnalytics_17929898861220/Dashboard1"
    "?:language=en-GB&:showVizHome=no&:toolbar=yes"
)

@app.route("/")
def home():
    return render_template("index.html", active="overview")

@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        active="dashboard",
        tableau_url=TABLEAU_DASHBOARD_URL
    )

@app.route("/story")
def story():
    return render_template(
        "story.html",
        active="story",
        tableau_url=TABLEAU_STORY_URL
    )

if __name__ == "__main__":
    app.run(debug=True)
