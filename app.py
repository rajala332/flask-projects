from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

# Simple in-memory account (not persistent)
account = {
    "name": "John Doe",
    "balance": 1000.0
}

@app.route("/", methods=["GET", "POST"])
def account_page():
    message = ""
    if request.method == "POST":
        action = request.form.get("action")
        amount = request.form.get("amount")

        if amount:
            try:
                amount = float(amount)
                if amount <= 0:
                    message = "Amount must be greater than 0."
                else:
                    if action == "deposit":
                        account["balance"] += amount
                        message = f"Deposited ₹{amount:.2f}"
                    elif action == "withdraw":
                        if account["balance"] >= amount:
                            account["balance"] -= amount
                            message = f"Withdrew ₹{amount:.2f}"
                        else:
                            message = "Insufficient balance!"
            except ValueError:
                message = "Please enter a valid number."

    return render_template("account.html", account=account, message=message)

if __name__ == "__main__":
    app.run(debug=True)
