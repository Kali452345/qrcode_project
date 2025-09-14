from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

# Step 3: Create a Flask route for '/' that accepts GET and POST
@app.route('/', methods=['GET', 'POST'])
def home():
    qrcode_img = None  # Step 7: Default to no QR code image
    # Step 4: Check if the request method is POST
    if request.method == 'POST':
        # Step 5: Get the form data from the request
        data = request.form.get('data')
        if data:
            # Step 6: Generate the QR code using the received data
            qr = qrcode.make(data)
            buf = io.BytesIO()
            qr.save(buf, format='PNG')
            img_bytes = buf.getvalue()
            # Encode the image to base64 so it can be embedded in HTML
            qrcode_img = 'data:image/png;base64,' + base64.b64encode(img_bytes).decode('utf-8')
    # Step 8: Render the result (QR code image) in your template
    return render_template('index.html', qrcode_img=qrcode_img)

if __name__ == '__main__':
    app.run(debug=True)