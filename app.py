import streamlit as st

st.title("우리 가족 MBTI 테스트")
st.write("이 테스트는 우리 가족의 MBTI 유형을 알아보는 간단한 테스트입니다. 각 질문에 답변해 주세요.")

# 이름 입력 받기
name = st.text_input("이름을 입력하세요:")

if name:
    st.write(f"안녕하세요, {name}님! 아래 질문에 답변해 주세요.")

    # 질문 리스트
    st.subheader("E/I 질문")

    q1 = st.radio(
        "사람들과 함께 있을 때 에너지를 얻는 편이다.",
        ["예", "아니오"],
        key="q1"
    )

    q2 = st.radio(
        "새로운 사람을 만나는 것이 즐겁다.",
        ["예", "아니오"],
        key="q2"
    )

    q3 = st.radio(
        "혼자 있는 시간보다 여럿이 함께 있는 시간이 좋다.",
        ["예", "아니오"],
        key="q3"
    )

    q4 = st.radio(
        "모임에서 먼저 말을 거는 편이다.",
        ["예", "아니오"],
        key="q4"
    )

    st.subheader("S/N 질문")

    q5 = st.radio(
        "현실적인 사실이 아이디어보다 중요하다.",
        ["예", "아니오"],
        key="q5"
    )

    q6 = st.radio(
        "새로운 가능성을 상상하는 것을 좋아한다.",
        ["예", "아니오"],
        key="q6"
    )

    st.subheader("T/F 질문")

    q7 = st.radio(
        "결정을 내릴 때 논리가 감정보다 중요하다.",
        ["예", "아니오"],
        key="q7"
    )

    q8 = st.radio(
        "상대방의 기분을 우선 고려하는 편이다.",
        ["예", "아니오"],
        key="q8"
    )

    st.subheader("J / P 유형")

    q9 = st.radio(
        "계획을 세워두는 것이 편하다.",
        ["예", "아니오"],
        key="q9"
    )

    q10 = st.radio(
        "상황에 따라 즉흥적으로 행동하는 것을 좋아한다.",
        ["예", "아니오"],
        key="q10"
    )



    if st.button("결과 보기"):

        e_score = 0
        i_score = 0

        s_score = 0
        n_score = 0

        t_score = 0
        f_score = 0

        j_score = 0
        p_score = 0

        if q1 == "예":
            e_score += 1
        else:
            i_score += 1

        if q2 == "예":
            e_score += 1
        else:
            i_score += 1

        if q3 == "예":
            e_score += 1
        else:
            i_score += 1

        if q4 == "예":
            e_score += 1
        else:
            i_score += 1

        if q5 == "예":
            s_score += 1
        else:
            n_score += 1

        if q6 == "예":
            n_score += 1
        else:
            s_score += 1

        if q7 == "예":
            t_score += 1
        else:
            f_score += 1

        if q8 == "예":
            f_score += 1
        else:
            t_score += 1

        if q9 == "예":
            j_score += 1
        else:
            p_score += 1

        if q10 == "예":
            p_score += 1
        else:
            j_score += 1

        st.write("E 점수:", e_score)
        st.write("I 점수:", i_score)

        st.write("S 점수:", s_score)
        st.write("N 점수:", n_score)

        if e_score >= i_score:
            ei = "E"
        else:
            ei = "I"

        if s_score >= n_score:
            sn = "S"
        else:
            sn = "N"

        if t_score >= f_score:
            tf = "T"
        else:
            tf = "F"

        if j_score >= p_score:
            jp = "J"        

        else:
            jp = "P"

        mbti = ei + sn + tf + jp
            
        st.success(f"{name}님의 MBTI 유형은 {mbti}입니다!")

        # if e_score > i_score:
        #     st.write(f"{name}님의 MBTI 유형은 {ei}{sn}입니다!")
        # elif i_score > e_score:
        #     st.write(f"{name}님의 MBTI 유형은 {ei}{sn}입니다!")
        # else:
        #     st.write(f"{name}님의 MBTI 유형은 {ei}{sn}입니다!")

        # st.write("선택한 답변:", q1)
    # # 답변 저장
    # answers = []

    # for question in questions:
    #     answer = st.radio(question, ("예", "아니오"))
    #     answers.append(answer)

    # if st.button("결과 확인"):
    #     # MBTI 유형 계산 (간단한 예시)
    #     mbti_score = sum(1 for answer in answers if answer == "예")
        
    #     if mbti_score <= 2:
    #         mbti_type = "ISTJ"
    #     elif mbti_score == 3:
    #         mbti_type = "ISFJ"
    #     elif mbti_score == 4:
    #         mbti_type = "INFJ"
    #     else:
    #         mbti_type = "INTJ"

    #     st.write(f"{name}님의 MBTI 유형은 {mbti_type}입니다!")