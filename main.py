import streamlit as st
from langchain_openai import ChatOpenAI

# OpenAI API 키 가져오기
openai_api_key = st.secrets["OPENAI_API_KEY"]

# OpenAI API 키가 없는 경우 에러 메시지 표시 후 종료
if not openai_api_key:
    st.error("OpenAI API 키가 설정되지 않았습니다. .env 파일에 설정해주세요.")
    st.stop()

# ChatOpenAI 클래스의 인스턴스 생성
chat_model = ChatOpenAI(api_key=openai_api_key)

# 스트림릿 앱 제목 설정
st.title('인공지능 대화 시스템')

# 대화 상대의 말투 입력
partner_tone = st.text_area('대화 상대의 말투를 나타내는 문장')

# 사용자로부터 대화 시작 문장 입력 받기
user_input = st.text_input('대화 시작')

# 사용자가 버튼을 클릭하면 대화 생성
if st.button('대화 생성'):
    # 대화 상대의 말투를 입력 문장에 추가하여 모델에 전달
    input_with_tone = f"{partner_tone}\n{user_input}"
    
    # 사용자 입력과 함께 대화 생성
    with st.spinner('대화 생성 중...'):
        try:
            response = chat_model.invoke(input_with_tone)
            st.write('대화 상대의 응답:', response.content)
        except Exception as e:
            st.error(f"대화 생성 중 오류가 발생했습니다: {str(e)}")