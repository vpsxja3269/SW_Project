import streamlit as st
import openai

# OpenAI API 인증 설정
openai.api_key = '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'

# OpenAI API로 대화 생성하는 함수
def generate_response(input_text):
    response = openai.Completion.create(
        engine='davinci',
        prompt=input_text,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Streamlit 애플리케이션
def main():
    st.title("대화형 인공지능")

    # 사용자 입력 받기
    user_input = st.text_input("사용자 입력", key="user_input", value="")

    # 사용자 입력이 있을 경우에만 대화 생성
    if user_input:
        # OpenAI API로 대화 생성
        response = generate_response(user_input)

        # 생성된 대화 결과 출력
        st.text_area("대화 결과", value=response, height=400, key="output")

if __name__ == '__main__':
    main()