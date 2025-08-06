# 강화 운세 챗봇 Webhook 서버

🎯 카카오톡 오픈빌더에 연동할 수 있는 Flask 기반의 간단한 강화 운세 서버입니다.

## ✅ 배포 방법 (Railway)

1. 이 저장소를 Fork 합니다
2. [https://railway.app](https://railway.app) → New Project → Deploy from GitHub
3. 이 저장소를 선택하고 포트 번호는 `5000` 입력
4. 배포 후 Domain 주소 + `/webhook`을 붙이면 Webhook URL이 됩니다

## 🗨️ 오픈빌더 설정

- 사용자 발화: `강화운세`, `오늘 강화 잘 될까`, `누렙 해도 될까`
- Webhook 스킬 연결: `https://xxx.up.railway.app/webhook`

## ✅ 예시 응답

📛 강화 대성공의 날  
🧿 평소보다 성공 확률이 높습니다!  
💡 지금 도전해보세요!