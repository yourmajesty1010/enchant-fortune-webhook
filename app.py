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
        "description": "평소 성공하기 어려웠던 강화에 행운이 따릅니다.",
        "advice": "한두 번 실패했더라도 포기하지 말고 재도전해보세요."
    },
    {
        "title": "성공 예감",
        "description": "안정적인 강화에 적합한 날입니다.",
        "advice": "무리한 도전보다는 낮은 단계의 강화를 여러 번 시도해보세요."
    },
    {
        "title": "평범한 하루",
        "description": "특별할 것도, 나쁠 것도 없는 평범한 날입니다.",
        "advice": "꼭 필요한 강화가 아니라면 재료를 아끼고 다음 기회를 노리세요."
    },
    {
        "title": "불길한 예감",
        "description": "성공 확률이 평소보다 낮아 보입니다.",
        "advice": "오늘은 강화를 쉬고 다른 즐거움을 찾아보세요."
    },
    {
        "title": "퍼거스가 당신을 주시합니다",
        "description": "퍼거스의 웃음소리가 들립니다. 파괴 확률이 높습니다.",
        "advice": "오늘은 강화 금지입니다!"
    }
]

@app.route("/webhook", methods=["POST"])
def webhook():
    selected = random.choice(fortunes)
    response_text = f"""
📛 {selected['title']}

🧿 {selected['description']}

💡 조언: {selected['advice']}
    """.strip()
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": response_text
                    }
                }
            ]
        }
    })

if __name__ == "__main__":
    app.run(port=5000)