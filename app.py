from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta


JWT_SECRET_KEY = 'NJUCM'
USERNAME = 'njucm'
PASSWORD = 'njucm'

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
jwt = JWTManager(app)


@app.route('/')
def index():
    return jsonify({'message': 'success!'})

@app.route('/auth', methods=['POST'])
def auth():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != USERNAME or password != PASSWORD:
        return jsonify({"msg": "Bad username or password"}), 401
    expires = timedelta(days=30)
    access_token = create_access_token(identity=username, expires_delta=expires)
    print(access_token)
    return jsonify(access_token=access_token)


@app.route('/wd', methods=['POST'])
@jwt_required()
def wd():
    question = request.args.get('question', None)
    return jsonify({'message': f'这往往与心脏有关，但在中医中，这是与“心火旺盛”或“心有热”相关，可能导致失眠或睡眠质量差。'})

@app.route('/zx', methods=['POST'])
@jwt_required()
def kyzx():
    name = request.args.get('name', None)
    gender = request.args.get('gender', None)
    age = request.args.get('age', None)
    disease = request.args.get('disease', None)
    question = request.args.get('question', None)
    return jsonify({
    "tzpd": {
        "zytz": {
            "qttz": "疲乏无力、语音低弱、易出汗、面色苍白。性格温和、内向。易患呼吸系统疾病、免疫力较低。",
            "cjbx": "常感口燥咽干，喜欢喝水，但不喜欢喝热饮。手足心热，五心烦热。常感觉身体疲倦，潮热汗出。",
            "fbqx": "易患心脑血管疾病，如冠心病、脑梗塞、静脉曲张等。",
            "tz": "气郁质"
        },
        "jytz": {
            "qttz": "畏寒、手脚冰凉、面色白、喜欢温暖、汗少、小便清长、大便稀。性格比较内向、做事谨慎。易感冒、消化系统功能较弱、易有疲劳感。",
            "cjbx": "食欲旺盛，消化吸收功能良好。体型适中，肌肉发达。不易生病，适应环境变化能力强。",
            "fbqx": "易患呼吸系统疾病，如慢性支气管炎、感冒等。",
            "tz": "阴虚质"
        }
    },
    "yscf": {
        "ztjy": "阳虚质的调理建议需要以增强身体阳气为主，从饮食、生活习惯以及心理调适等多方面综合施策。",
        "qzts": "阳虚质的情志调理重点在于培养稳定、积极的心态和情绪，以促进内在阳气的生成和调和。首先，建议阳虚质的人士应当维护规律的生活作息，保证充足的睡眠，避免熬夜，因为不规律的作息会损伤阳气。",
        "qjty": "阳虚质的起居调养应当着重在营造一个温暖和舒适的生活环境，并且保持规律的作息时间。在日常生活中，应当注意居室的保暖，避免冷风直接吹拂，尤其是在寒冷的季节里。穿着方面，要根据天气变化适时增减衣物，避免身体受凉，特别是要保暖腹部和下肢。晚上睡觉时应选择足够的被褥，并保持睡房的适宜温度，避免受寒。此外，建议阳虚体质的人早睡早起，尽量在夜间十点前入睡，以充分利用夜间的阴静来养阳气。"
    },
    "ydfa": {
        "jtfa": [
            {
                "mc": "拉伸运动",
                "fa": "瑜伽中的某些体位法可以帮助行气和化湿，如“山式”、“猫式”、“牛式”等。建议每周2-3次，每次45-60分钟。"
            },
            {
                "mc": "散步",
                "fa": "舒缓身心、调和气血、健脾化湿。每周进行3-4次，每次30分钟。"
            }
        ],
        "ztjy": " 建议湿痰质体质的人进行规律、适量、中低强度的锻炼，避免过度劳累，每次锻炼后都应保持身体轻松、舒适、心情愉悦。合适的锻炼可以促进血液循环，帮助身体排除多余的湿气。",
        "zysx": [
            "确识起生记",
            "动律相根市",
            "变发量间会"
        ]
    },
    "zywz": [
        {
            "fa": "今",
            "md": "就住写水们意子得此等造感府话命。",
            "cz": "根者民按包断实型派十情党车养。",
            "zy": "身千石节离老及同后置出月使相解需个。"
        },
        {
            "fa": "有",
            "md": "进半口经反价广按光资论结眼热。",
            "cz": "备果主才住斯还任没里量价设采入。",
            "zy": "决切往机毛离拉林教以记眼起日八。"
        }
    ],
    "ysfa": {
        "tjsw": {
            "zytz": {
                "mc": "是往图",
                "fa": "白明商她些整教山置走比般志太子点各。管酸周区构写老计类酸断红合线步。江真别月音信并西北行照品全资认。传很区更这备众命引论亲照府信子学。较法何指感百办自影先支要等油化状即。"
            },
            "jytz": {
                "mc": "经所交完年",
                "fa": "在任酸没和无入以满这教中我。族重工程日家非二好还参新日。展体究不组联再科需性应毛。自查严此器然会只接变温空调细。务油史好家她定子将论两劳养无高院。治位得我适空中式理统省江马满交革。农商属把响族层华生七原极也算。"
            }
        },
        "jj": {
            "zytz": {
                "mc": "元团带把候方调",
                "fa": "引条在它目由即历年约质布非。飞机低建建维通立义带存改片。争热治议经整头况理组可以期理飞部期论。包温再最用听完型儿运道通。"
            },
            "jytz": {
                "mc": "革复更",
                "fa": "关好候性成才论论看单术无于历量划按生。又天前确该着量易做行深青按。般从温先般强矿步放广件好导多铁在。小调保身种历东转性马形得般要并。"
            }
        }
    }
})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)