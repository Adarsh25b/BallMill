from flask import Flask, render_template,request
import joblib
import math


app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html',result1="not yed inputed", result2="not yet inputed")

@app.route('/predict', methods=['POST'])
def predict():
	
		x1=float(request.form.get('F'))
		x2=float(request.form.get('P'))
		x3=float(request.form.get('D'))
		x4=float(request.form.get('desired'))
		Pr=10.225-0.221*x1+20.017*x2-0.043*x3-0.022*x1*x2-0.00005952*x1*x3-0.004*x2*x3-1.4973*x2*x2+0.00005642*x3*x3
		print(Pr)
		inc=(x4-Pr)/20.017

		x5=x2+inc
		result1=x5/x2
		inc2=(Pr-x4)/(0.0430)
		x6=x3+inc2
		result2=pow(x3/x6,20/9)
		
		cvsf= math.log(x6/x3)
		result3=cvsf/0.063
        
         
		return render_template('index.html', result1='{0:.2f}'.format(result1), result2='{0:.2f}'.format(result2), result3='{0:.2f}'.format(result3) )

if __name__=='__main__':
	app.run(host="0.0.0.0", port=5000)


