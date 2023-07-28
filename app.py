from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# 读取数据，假设数据是 CSV 格式
data = pd.read_json('data/alpaca_gpt4_data_zh.json')

# 如果没有 'id' 列，我们使用数据的索引作为 'id'
if 'id' not in data.columns:
    data['id'] = data.index

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        # 获取页码参数，如果没有提供，默认为 1
        page = request.args.get('page', default=1, type=int)
        # 计算开始和结束的索引
        start = (page - 1) * 20  # 每页 20 条数据
        end = start + 20
        # 返回对应的数据
        return data[start:end].to_json(orient='records')
    elif request.method == 'POST':
        # 接收和保存数据
        received_data = request.get_json()
        # 找到对应的数据项
        item_index = data[data['id'] == received_data['id']].index
        if len(item_index) > 0:
            # 更新数据
            data.loc[item_index[0]] = received_data
        return jsonify({'status': 'success'})
