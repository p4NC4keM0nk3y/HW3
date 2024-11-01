from flask import Flask, render_template_string
import psycopg2

HTML_TEMPLATE = """
<table border="1">
    <tr>
        <th>Basket A Fruits</th>
        <th>Basket B Fruits</th>
    </tr>
    {% for a, b in zip_fruits %}
    <tr>
        <td>{{ a if a else '' }}</td>
        <td>{{ b if b else '' }}</td>
    </tr>
    {% endfor %}
</table>
"""
app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname="fruits", 
        user="insertyourusernamehere",
        password="insertyourpasswordhere",
        host="localhost",
        port="5432"
    )


@app.route('/api/update_basket_a')
def update_basket_a():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        conn.commit()
        cur.close()
        conn.close()
        return "Success!"

@app.route('/api/unique')
def unique_fruits():
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a ORDER BY fruit_a")
        basket_a_fruits = [row[0] for row in cur.fetchall()]
        
        cur.execute("SELECT DISTINCT fruit_b FROM basket_b ORDER BY fruit_b")
        basket_b_fruits = [row[0] for row in cur.fetchall()]
        
        max_len = max(len(basket_a_fruits), len(basket_b_fruits))
        basket_a_fruits += [''] * (max_len - len(basket_a_fruits))
        basket_b_fruits += [''] * (max_len - len(basket_b_fruits))
        
        cur.close()
        conn.close()
        
        return render_template_string(HTML_TEMPLATE, zip_fruits=zip(basket_a_fruits, basket_b_fruits))

if __name__ == '__main__':
    app.run(debug=False)