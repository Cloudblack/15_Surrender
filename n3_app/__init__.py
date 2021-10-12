from flask import Flask,render_template,redirect,url_for
#n3_app.bp 나중에 부ㅡㅌ일껏


def create_app():
    app=Flask(__name__)
    from bp import sub
    app.register_blueprint(sub.sub_bp)

    @app.route('/')
    def index():
        return render_template('index.html')    
    
    
    #app.register_blueprint(sub_bp)      



    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)