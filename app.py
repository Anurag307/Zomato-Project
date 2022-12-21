from flask import Flask , request, render_template
import pandas as pd



df = pd.read_csv(r'C:\Users\Rishikesh Singh\Zomato ML Project\data.csv')

main_df = pd.read_csv(r'C:\Users\Rishikesh Singh\Zomato ML Project\final_data.csv')








app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    data = {}
    if request.method == 'POST':
        object = request.form.to_dict()
        b= df[df['location']== object['address']][['Avg_price','Most_popular_restaurat','Serves']]
        mydict1 = b.to_dict(orient='record')
        if len(mydict1) != 0:
            data = mydict1[0]
            data['address'] = object['address']
        else:
            data['address'] = 'NO!! location found'
        popular_serves = main_df[main_df['cusines'].str.contains(object['fname'])]
        popular_serves = popular_serves[popular_serves['Ratings'] == popular_serves['Ratings'].max()]
        mydict =  popular_serves.to_dict(orient = 'record')
        if len(mydict) !=0 :
            data['Popular_Restaurant_that_serves'] = mydict[0]['Name']
            data['fname'] = object['fname']
        else:
            data['fname'] = 'Cusine not found!'
        data['lname'] = object['lname']
        

        return render_template('index.html', data = data )
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)