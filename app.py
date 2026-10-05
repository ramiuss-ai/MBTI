import streamlit as st

st.write("MBTI APP START")

questions = [
    {
        "text": "1. 처음 참석한 모임에서도 모르는 사람에게 먼저 말을 거는 편이다.",
        "type": "EI",
        "positive": "E"
    },

    {
        "text": "2. 여럿이 함께 하는 활동을 마치고 나면 오히려 에너지가 생긴다.",
        "type": "EI",
        "positive": "E"
    },

    {
        "text": "3.회의나 모임에서 자신의 의견을 적극적으로 표현하는 편이다.",
        "type": "EI",
        "positive": "E"
    },

    {
        "text": "4.주말에 시간이 비어 있으면 사람들을 만나는 계획을 세우고 싶어진다",
        "type": "EI",
        "positive": "E"
    },

        {
        "text": "5. 새로운 사람들과 관계를 맺는 과정이 즐겁게 느껴진다",
        "type": "EI",
        "positive": "E"
    },

    {
        "text": "6. 중요한 결정을 내릴 때는 다른 사람과 이야기하기 보다 혼자 생각하는 시간이 필요하다.",
        "type": "EI",
        "positive": "I"
    },

    {
        "text": "사람들과 오랜 시간을 보낸 뒤에는 혼자 만의 시간이 꼭 필요하다.",
        "type": "EI",
        "positive": "I"
    },

    {
        "text": "8. 낯선 사람들과 대화는 즐겁기 보다 에너지가 소모 되는 느낌이 든다.",
        "type": "EI",
        "positive": "I"
    },

    {
        "text": "9. 생각을 충분히 정리한 뒤에 말하는 것이 편하다.",
        "type": "EI",
        "positive": "I"
    },

    {
        "text": "여럿이 있는 자리보다 혼자 하거나 소수와 함께하는 활동을 선호한다.",
        "type": "EI",
        "positive": "I"
    },

    {
        "text": "11. 새로운 일을 배울 때에는 이론 보다 실제 예시가 있어야 이해가 잘 돤다.",
        "type": "SN",
        "positive": "S"
    },

    {
        "text": "12. 결정을 내릴 때는 과거의 경험을 중요한 근거로 삼는 편이다.",
        "type": "SN",
        "positive": "S"
    },

    {
        "text": "설명을 들을 때 큰 그림보다 세부 내용을 먼저 확인하는 편이다.",
        "type": "SN",
        "positive": "S"
    },

    {
        "text": "14. 실제로 검증되지 않은 아이디어 보다는 이미 입증된 방법을 선호한다.",
        "type": "SN",
        "positive": "S"
    },

    {
        "text": "15. 대화를 할 때 사실과 경험을 중심으로 이야기 하는 편이다.",
        "type": "SN",
        "positive": "S"
    },

    {
        "text": "16. 하나의 사실을 보면 그 사실이 의미하는 가능성을 먼저 떠올린다",
        "type": "SN",
        "positive": "N"
    },

        {
        "text": "17. 현실적인 제약보다 새로운 아이디어를 생각하는 과정이 즐겁다",
        "type": "SN",
        "positive": "N"
    },

    {
        "text": "18.대화 중에도 숨겨진 의미나 패턴을 찾으려고 하는 편이다.",
        "type": "SN",
        "positive": "N"
    },

    {
        "text": "19. 현재 상황보다 앞으로 일어날 가능성에 더 관심이 많다.",
        "type": "SN",
        "positive": "N"
    },

    {
        "text": "20. 가끔은 실제 현실보다 상상 속 아이디어에 더 몰입하기도 한다.",
        "type": "SN",
        "positive": "N"
    },

    {
        "text": "21. 의사 결정을 할 때 사람의 감정보다 객관적인 사실을 우성 고려한다.",
        "type": "TF",
        "positive": "T"
    },

    {
        "text": "22. 문제가 발생하면 원인을 분석하고 해결책을 찾는 것부터 시작한다.",
        "type": "TF",
        "positive": "T"
    },

    {
        "text": "23. 친한 사람이라도 잘못한 부분은 솔직하게 지적해야 한다고 생각한다.",
        "type": "TF",
        "positive": "T"
    },

    {
        "text": "24. 회의에서 의견이 충돌하면 논리적으로 더 타당한 쪽을 지지 한다.",
        "type": "TF",
        "positive": "T"
    },

    {
        "text": "25. 결정을 내릴 때 공평성과 일관성을 중요하게 생각한다",
        "type": "TF",
        "positive": "T"
    },

    {
        "text": "26. 결정을 내릴 때 관련된 사람들의 감정을 먼저 고려하는 편이다.",
        "type": "TF",
        "positive": "F"
    },

    {
        "text": "27. 갈등 상황에서 옭고 그름 보다 관계를 유지하는 것이 중요하다고 생각한다.",
        "type": "TF",
        "positive": "F"
    },

    {
        "text": "28. 누군가 고민을 이야기 하면 해결책보다 공감을 해주는 편이다.",
        "type": "TF",
        "positive": "F"
    },

    {
        "text": "29. 원칙에 맞더라도 상대방이 상처를 받을 수 있다면 표현을 조심하는 편이다.",
        "type": "TF",
        "positive": "F"
    },

    {
        "text": "30. 주변 사람들이 조화롭게 지내는 것을 중요하게 생각한다.",
        "type": "TF",
        "positive": "F"
    },

    {
        "text": "31. 여행을 가기 전에 숙소와 일정을 미리 정해두어야 마음이 편하다.",
        "type": "JP",
        "positive": "J"
    },

    {
        "text": "32. 해야 할 일이 생기면 계획표나 체크리스트를 만드는 편이다.",
        "type": "JP",
        "positive": "J"
    },

    {
        "text": "33. 마감 일이 가까워지기 전에 미리 일을 끝내두는 것을 선호한다.",
        "type": "JP",
        "positive": "J"
    },
    {
        "text": "34. 예상치 못한 일정 변경이 생기면 스트레스를 받는 편이다",
        "type": "JP",
        "positive": "J"
    },

    {
        "text": "35. 중요한 결정을 내린 뒤에는 다시 고민하지 않는다.",
        "type": "JP",
        "positive": "J"
    },

        {
        "text": "36. 여행을 가도 현지에서 즉흥적으로 계획을 바꾸는 것을 즐긴다.",
        "type": "JP",
        "positive": "P"
    },

    {
        "text": "37. 일을 진행 할 때 여러 가능성을 열어 두는 편이다.",
        "type": "JP",
        "positive": "P"
    },

    {
        "text": "38. 마감 직전에 집중력이 더 높아지는 편이다.",
        "type": "JP",
        "positive": "P"
    },

    {
        "text": "39. 새로운 선택지가 생기면 기존 계획을 바꾸는 데 큰 부담이 없다",
        "type": "JP",
        "positive": "P"
    },

    {
        "text": "40. 결정을 내리기 전에 가능한 한 많은 옵션을 검토하고 싶다.",
        "type": "JP",
        "positive": "P"
    },
]

mbti_descriptions = {

    "ISTJ": "📋 현실주의자형 - 책임감이 강하고 맡은 일을 끝까지 해내는 편입니다. 체계와 원칙을 중요하게 생각하며 신뢰를 주는 사람으로 평가받습니다.",

    "ISFJ": "🛡️ 수호자형 - 배려심이 많고 주변 사람들을 챙기는 데 익숙합니다. 조용하지만 헌신적이며 가족과 가까운 사람들을 소중하게 생각합니다.",

    "INFJ": "🌱 옹호자형 - 사람과 세상에 대한 깊은 통찰력을 가지고 있습니다. 자신만의 가치관이 분명하며 의미 있는 목표를 추구합니다.",

    "INTJ": "🧠 전략가형 - 장기적인 계획을 세우는 것을 좋아합니다. 독립적이며 문제를 분석하고 해결하는 데 강점을 가지고 있습니다.",

    "ISTP": "🔧 장인형 - 직접 경험하며 배우는 것을 선호합니다. 문제 해결 능력이 뛰어나고 위기 상황에서도 침착하게 대응하는 편입니다.",

    "ISFP": "🎨 예술가형 - 현재의 순간을 소중히 여기며 감성이 풍부합니다. 자신의 가치와 취향을 중요하게 생각하고 자유로운 삶을 선호합니다.",

    "INFP": "📖 중재자형 - 상상력이 풍부하고 이상을 중요하게 생각합니다. 사람들의 가능성을 믿으며 자신의 신념에 진심으로 몰입합니다.",

    "INTP": "🔬 사색가형 - 새로운 지식과 아이디어를 탐구하는 것을 좋아합니다. 논리적인 사고를 즐기며 항상 더 나은 방법을 고민합니다.",

    "ESTP": "⚡ 사업가형 - 행동력이 뛰어나고 새로운 경험을 즐깁니다. 상황 판단이 빠르며 도전적인 환경에서 에너지를 얻는 편입니다.",

    "ESFP": "🎉 연예인형 - 사람들과 함께하는 시간을 즐기며 분위기를 밝게 만드는 재능이 있습니다. 현재를 즐기고 삶의 재미를 중요하게 생각합니다.",

    "ENFP": "✨ 활동가형 - 열정적이고 창의적이며 새로운 가능성을 찾아 나서는 것을 좋아합니다. 사람들에게 영감을 주는 경우가 많습니다.",

    "ENTP": "🔥 토론가형 - 호기심이 많고 새로운 관점을 탐구하는 것을 즐깁니다. 아이디어가 풍부하며 토론과 문제 해결에 강한 모습을 보입니다.",

    "ESTJ": "🏆 경영자형 - 조직을 이끌고 목표를 달성하는 능력이 뛰어납니다. 실용적이고 책임감이 강하며 효율성을 중요하게 생각합니다.",

    "ESFJ": "🤝 집정관형 - 사람들과의 관계를 중요하게 생각하고 주변을 잘 챙깁니다. 협력적이며 공동체 안에서 신뢰받는 경우가 많습니다.",

    "ENFJ": "🌟 선도자형 - 사람들의 성장과 가능성을 이끌어내는 데 능숙합니다. 따뜻한 공감 능력과 리더십을 동시에 갖추고 있습니다.",

    "ENTJ": "👑 통솔자형 - 목표를 향해 나아가는 추진력이 강합니다. 전략적으로 사고하며 조직과 사람들을 이끄는 데 능력을 발휘합니다."
}


st.title("우리 가족 MBTI 테스트")
st.write("이 테스트는 우리 가족의 MBTI 유형을 알아보는 간단한 테스트입니다. 각 질문에 답변해 주세요.")

# 이름 입력 받기
name = st.text_input("이름을 입력하세요:")

answers = []

for i, question in enumerate(questions):

    answer = st.radio(
        question["text"],
        ["선택하세요", "예", "아니오"],
        key=f"q{i}"
    )

    answers.append(answer)

completed = sum(
    1 for answer in answers
    if answer != "선택하세요"
)

total_questions = len(questions)

progress = completed / total_questions

st.subheader("📊 테스트 진행률")

st.progress(progress)

st.caption(
    f"{completed}/{total_questions} 문항 완료 "
    f"({progress * 100:.0f}%)"
)
# st.write(answers)

if st.button("결과 보기"):

    if completed < total_questions:
        st.warning("모든 문항에 답변해주세요.")
        st.stop()

    e_score = 0
    i_score = 0

    s_score = 0
    n_score = 0

    t_score = 0
    f_score = 0

    j_score = 0
    p_score = 0

    for i, question in enumerate(questions):

        answer = answers[i]

        if question["type"] == "EI":

            if question["positive"] == "E":

                if answer == "예":
                    e_score += 1
                else:
                    i_score += 1

            elif question["positive"] == "I":

                if answer == "예":
                    i_score += 1
                else:
                    e_score += 1

        if question["type"] == "SN":

            if question["positive"] == "S":

                if answer == "예":
                    s_score += 1
                else:
                    n_score += 1

            elif question["positive"] == "N":

                if answer == "예":
                    n_score += 1
                else:
                    s_score += 1

        if question["type"] == "TF":

            if question["positive"] == "T":

                if answer == "예":
                    t_score += 1
                else:
                    f_score += 1

            elif question["positive"] == "F":

                if answer == "예":
                    f_score += 1
                else:
                    t_score += 1

        if question["type"] == "JP":

            if question["positive"] == "J":

                if answer == "예":
                    j_score += 1
                else:
                    p_score += 1

            elif question["positive"] == "P":

                if answer == "예":
                    p_score += 1
                else:
                    j_score += 1

# 유형별 스코어 출력
    with st.expander("📊 세부 점수 보기"):
        col1, col2 = st.columns(2)

        with col1:
            st.metric("E", e_score)

        with col2:
            st.metric("I", i_score)

        col3, col4 = st.columns(2)

        with col3:
            st.metric("S", s_score)

        with col4:
            st.metric("N", n_score)

        col5, col6 = st.columns(2)

        with col5:
            st.metric("T", t_score)
        with col6:
            st.metric("F", f_score)

        col7, col8 = st.columns(2)

        with col7:
            st.metric("J", j_score)
        with col8:
            st.metric("P", p_score)

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

# 최종 MBTI 유형 계산
    st.divider()

    mbti = ei + sn + tf + jp

    st.success(f"{name}님의 MBTI 결과")

    # st.header(f"🎉 {mbti}")

    st.markdown(
    f"""
    ## 🎉 {mbti}

    ### {name}님의 성격 유형
    """
)

    if mbti in mbti_descriptions:
        st.info(mbti_descriptions[mbti])
    else :
        st.info("해당 MBTI 유형에 대한 설명이 없습니다.")

        