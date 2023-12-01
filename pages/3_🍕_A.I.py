import streamlit as st
import openai

# OpenAI API 인증 설정
openai.api_key = '안알려주시롱'

# OpenAI API로 대화 생성하는 함수
def generate_response(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Streamlit 애플리케이션
def main():
    st.title("Opem AI Study")

    # 사용자 입력 받기
    user_input = st.text_input("사용자 입력", value="")

    # 사용자 입력이 있을 경우에만 대화 생성
    if user_input:
        # OpenAI API로 대화 생성
        response = generate_response(user_input)

        # 질문과 답변 출력
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("질문:")
            st.write(user_input)
        with col2:
            st.subheader("답변:")
            st.text_area("답변 보기", value=response, height=200)

if __name__ == '__main__':
    main()
