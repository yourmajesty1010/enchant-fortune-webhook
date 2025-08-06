from flask import Flask, request, jsonify
import random

app = Flask(__name__)

fortunes = [
    {
        "title": "여신의 축복이 함께합니다!",
        "description": "에린의 모든 기운이 당신을 향해있습니다. 오늘은 무엇을 강화하든 상상 이상의 결과를 얻게 될 것입니다.",
        "advice": "망설이지 마세요! 가장 아끼는 장비에 도전할 절호의 기회입니다."
    },
    {
        "title": "강화 대성공의 날",
        "description": "대장간의 불꽃이 유난히 밝게 타오릅니다. 평소 성공하기 어려웠던 강화에 행운이 따릅니다.",
        "advice": "한두 번 실패했더라도 포기하지 말고 재도전해보세요. 결과가 달라질 수 있습니다."
    },
    {
        "title": "성공 예감",
        "description": "나쁘지 않은 감각입니다. 작은 성공들이 모여 큰 기쁨을 가져다줄 것입니다. 안정적인 강화에 적합한 날입니다.",
        "advice": "무리한 도전보다는, 낮은 단계의 강화를 여러 번 시도하여 스펙을 차근차근 올리는 것을 추천합니다."
    },
    {
        "title": "평범한 하루",
        "description": "특별할 것도, 나쁠 것도 없는 평범한 날입니다. 강화 결과는 당신의 운에 따라 정직하게 나올 것입니다.",
        "advice": "꼭 필요한 강화가 아니라면 재료를 아끼고 다음 기회를 노리는 것도 좋은 전략입니다."
    },
    {
        "title": "불길한 예감",
        "description": "장비에서 냉기가 느껴집니다... 성공 확률이 평소보다 낮아 보입니다. 작은 실수 하나가 큰 실패로 이어질 수 있습니다.",
        "advice": "오늘은 강화를 쉬고, 던전을 돌거나 친구와 대화하며 다른 즐거움을 찾아보세요."
    },
    {
        "title": "퍼거스가 당신을 주시합니다",
        "description": "대장간 근처에서 '퍼거스'의 웃음소리가 들려오는 듯합니다. 오늘 강화하는 장비는 높은 확률로 그의 손에 파괴될 것입니다.",
        "advice": "강화 버튼 근처에도 가지 마세요! 당신의 소중한 장비를 지키고 싶다면 오늘은 절대, 절대 강화 금지입니다!"
    }
]

app = Flask(__name__)

@app.route("/")
def home():
    return "강화 운세 Webhook 서버 작동 중!"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()

    selected = random.choice(fortunes)

    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"[{selected['title']}]\n\n{selected['description']}\n\n💡 오늘의 조언\n{selected['advice']}"
                        
                    }
                }
            ]
        }
    }
    return jsonify(response_body)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
