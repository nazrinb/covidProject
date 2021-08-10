@app.route('/')
def home():
    return str(get_case_num)