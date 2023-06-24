import os
import pandas as pd
import sqlite3 as sql
import dataframe_image as dfi

from flask_cors import CORS
from flask_restful import Resource, Api
from flask import Flask, jsonify, request

import file_path_constants as FPC
from query_constants import queries

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'
con = sql.connect(
    FPC.db_path, check_same_thread=False)

output = []


def findAllAnswers():
    for query in queries:
        output.append(pd.read_sql_query(query, con))
    return


class GameBackend(Resource):
    def post(self):
        try:
            query = request.form['query']
            level = request.form['level']

            queryResult = pd.read_sql_query(query, con)
            result = queryResult.equals(output[int(level)])
            
            if FPC.output_image_path.exists():
                os.remove(FPC.output_image_path)
            dfi.export(
                queryResult,
                FPC.output_image_path,
                table_conversion='matplotlib'
            )
            response = jsonify({'data': result})
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
            if FPC.output_image_path.exists():
                os.remove(
                    FPC.output_image_path)
            response = jsonify({'error': 'Its a syntax error'})
            response.status_code = 400
            return response


# adding the defined resources along with their corresponding urls
api.add_resource(GameBackend, '/check')

# driver function
if __name__ == '__main__':
    findAllAnswers()
    app.run(debug=True)
