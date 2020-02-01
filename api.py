from flask import Flask,request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

countryList = [
        {
                "countryName":"India",
                "capital":"Delhi",
                "currency":"Rupees"
        }
    ]

class Country(Resource):
    def get(self,cname):
        if cname == "list":
            return countryList, 200
        for country in countryList:
            if country["countryName"] == cname:
                return country, 200
        return "Country not found", 404

    def put(self,cname):
        parser = reqparse.RequestParser()
        parser.add_argument("countryName",required=False)
        parser.add_argument("capital",required=False)
        parser.add_argument("currency",required=False)
        args = parser.parse_args()
        
        for country in countryList:
            if country["countryName"] == cname:
                if args["capital"]!=None:
                    country["capital"] = args["capital"]
                if args["currency"]!=None:
                    country["currency"] = args["currency"]
                return "Updated Data",200
        #countryList.append(args)
        return "Added",201


@app.route('/country',methods=['POST'])
def createCountry():
    if request.method == 'POST':
        parser = reqparse.RequestParser()
        parser.add_argument("countryName")
        parser.add_argument("capital")
        parser.add_argument("currency")
        args = parser.parse_args()
        
        for country in countryList:
            if country["countryName"] == args["countryName"]:
                return "Already exists", 200
        countryList.append(args)
        return "Added",201


api.add_resource(Country, '/country/<string:cname>')

if __name__ == '__main__':
    app.run(debug=True)