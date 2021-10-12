from flask import Blueprint
from flask import Flask,render_template,redirect,url_for,request
import joblib
import pandas as pd



sub_bp=Blueprint('sub',__name__, url_prefix='/sub')


@sub_bp.route('/')
def index():
    return render_template('index2.html')  

@sub_bp.route('/post',methods=['GET','POST'])
def post():
    if request.method == 'POST':
        blue_lv = int(request.form['bp1lv'])+int(request.form['bp2lv'])+int(request.form['bp3lv']) +int(request.form['bp4lv']) +int(request.form['bp5lv'])
        blue_mn = int(request.form['bp1mn'])+int(request.form['bp2mn'])+int(request.form['bp3mn']) +int(request.form['bp4mn']) +int(request.form['bp5mn'])    
        blue_kl = int(request.form['bp1kl'])+int(request.form['bp2kl'])+int(request.form['bp3kl']) +int(request.form['bp4kl']) +int(request.form['bp5kl'])    
        blue_as = int(request.form['bp1as'])+int(request.form['bp2as'])+int(request.form['bp3as']) +int(request.form['bp4as']) +int(request.form['bp5as'])    
        blue_tw = int(request.form['bttw'])      
        blue_dr = int(request.form['btdr'])    
        blue_win = int(request.form['btwin'])    
        red_lv = int(request.form['rp1lv'])+int(request.form['rp2lv'])+int(request.form['rp3lv']) +int(request.form['rp4lv']) +int(request.form['rp5lv'])
        red_mn = int(request.form['rp1mn'])+int(request.form['rp2mn'])+int(request.form['rp3mn']) +int(request.form['rp4mn']) +int(request.form['rp5mn'])    
        red_kl = int(request.form['rp1kl'])+int(request.form['rp2kl'])+int(request.form['rp3kl']) +int(request.form['rp4kl']) +int(request.form['rp5kl'])    
        red_as = int(request.form['rp1as'])+int(request.form['rp2as'])+int(request.form['rp3as']) +int(request.form['rp4as']) +int(request.form['rp5as'])    
        red_tw = int(request.form['rttw'])      
        red_dr = int(request.form['rtdr'])        
    data=blue_lv,blue_mn,blue_kl,blue_as,blue_tw,red_lv,red_mn,red_kl,red_as,red_tw,blue_dr,red_dr,blue_win
    blue,red,z,blue_,red_,red_p,blue_p =put_test(*data)
        
    return render_template('post.html',blue=blue,red=red,z=z,blue_=blue_,red_=red_,red_p=red_p,blue_p =blue_p )  


target='win_blue'
def split_xy(data):
    """변수이름 어떻게 다르게 출력하지..?"""
    y=data[target]
    x=data.drop(target,axis=1)
    return y,x

data_columns=['level_blue', 'minionsKilled_blue', 'kill_blue', 'assi_blue',
       'tower_blue', 'win_blue', 'level_red', 'minionsKilled_red', 'kill_red',
       'assi_red', 'tower_red', 'dragon_blue', 'dragon_red']

model = joblib.load('pred_lol.pkl')



def put_test(blue_lv,blue_mn,blue_kl,blue_as,blue_tw,red_lv,red_mn,red_kl,red_as,red_tw,blue_dr,red_dr,blue_win):
    dictdata={'level_blue':blue_lv,
        'minionsKilled_blue':blue_mn,
        'kill_blue':blue_kl,
        'assi_blue':blue_as,
        'tower_blue':blue_tw,
        'win_blue':blue_win,
        'level_red':red_lv,
        'minionsKilled_red':red_mn,
        'kill_red':red_kl,
        'assi_red':red_as,
        'tower_red':red_tw,
        'dragon_blue':blue_dr,
        'dragon_red':red_dr,
        }
    testdf = pd.DataFrame(columns=data_columns,data=dictdata,index=[0])
    y,x=split_xy(testdf)
    pred=model.predict_proba(x)   
    blue=round(pred[0][1]*100,1)
    red=round(pred[0][0]*100,1)
    if y[0] == 1:
        z='결과: 블루승'
    else:
        z='결과: 레드승'
    def letter(color):
        if color<=10:
            return "응 운빨존망겜","https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/A1Z/image/WsLigveFP4PEXdXoAgWeC_I5gTQ.jpg"
        if 10<color<=20:
            return "제발 그만해!! 나 무서워 ,,　　　　　　　　　　　　이러다가는 멘탈 다 터져,, 점수 다 떨군단 말이여,,","https://lh3.google.com/u/0/d/1_uJCLKNBtpS1VOaseEJN1EcKjMSvk_zF=w1892-h887-iv1"
        if 20<color<=40:
            return '자네.. 아직도 팀원을 믿나?',"https://coinpan.com/files/attach/images/198/866/703/255/51ca12bdfb5f57bb7b8c53ff6bae94db.jpg"
        if 40<color<=50:
            return "진정한 적은 내부에있어..!","https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/A1Z/image/XCsWnTM9gmmVpdex-usyXSDgRK8.jpg"
        if 50<color<=60:
            return "정글차이","https://lh3.google.com/u/0/d/1rMH1xOi5Qdc6-t--kF1tyafCbT73xP53=w1892-h887-iv1"
        if 60<color<=80:
            return "롤 재밌다!!!","https://lh3.google.com/u/0/d/1tq4bWBscoRHWm1_9AY_IcznhqldkVxAG=w1892-h887-iv1"
        else:
            return "이게 바로 롤?","https://lh3.google.com/u/0/d/1u4ASuGgEHr5m4XBYNkwzQRRCim2KDNRI=w1892-h887-iv1"
        


    blue_,blue_p=letter(blue)
    red_,red_p=letter(red)
    

    return blue,red,z,blue_,red_,red_p,blue_p  


# @sub_bp.route('/test')
# def test():
#     return render_template('index.html2')      

