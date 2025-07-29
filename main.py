from flask import Flask, render_template, request
import ast

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def multiply():
    result = None
    error = None

    if request.method == "POST":
        try:
            # Safely parse user input using ast.literal_eval
            matrix1 = ast.literal_eval(request.form["matrix1"])
            matrix2 = ast.literal_eval(request.form["matrix2"])

            # Check if matrices are valid for multiplication
            if len(matrix1[0]) != len(matrix2):
                error = "Matrix dimensions do not match for multiplication."
            else:
                # Multiply matrices
                result = [
                    [sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)]
                    for row in matrix1
                ]

        except Exception as e:
            error = f"Invalid input: {e}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
