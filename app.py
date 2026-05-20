# ─────────────────────────────────────────────
# 페이지 1: 홈 (캡처 화면 재현 버전)
# ─────────────────────────────────────────────
def page_home():
    # ── 메인 타이틀 ──────────────────────────────
    st.markdown(
        f"""
        <div style='padding: 20px 0 8px 0;'>
            <h1 style='background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
                       -webkit-background-clip: text;
                       -webkit-text-fill-color: transparent;
                       font-size: 44px; font-weight: 900; 
                       margin: 0; letter-spacing: -1px;'>
                {year}학년도 입학생
            </h1>
            <h2 style='color: #1f2937; font-size: 36px; font-weight: 900; 
                       margin: 4px 0 16px 0; letter-spacing: -1px;'>
                고교학점제 이수 가이드북
            </h2>
            <p style='color: #6b7280; font-size: 14px; margin: 0;'>
                신선여자고등학교 · 고교학점제 기반 학생 맞춤형 과목 선택 가이드
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # ── 메트릭 카드 3개 ────────────────────────────
    # 데이터 계산
    grad_credits = curriculum.get("graduation_credits", 192)

    # 학교지정(필수) 과목 수 카운트
    required_count = 0
    elective_count = 0
    for grade in curriculum.get("grades", []):
        for sem in grade.get("semesters", []):
            for s in sem.get("subjects", []):
                if s.get("type") == "필수":
                    required_count += 1
                else:
                    elective_count += 1

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div style='background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
                        border-radius: 16px; padding: 36px 20px; text-align: center;
                        min-height: 200px;
                        box-shadow: 0 1px 3px rgba(0,0,0,0.04);'>
                <h1 style='color: #6366f1; font-size: 56px; font-weight: 900; 
                           margin: 0; letter-spacing: -2px;'>{grad_credits}</h1>
                <p style='color: #1f2937; font-size: 16px; font-weight: 700; 
                          margin: 16px 0 6px 0;'>졸업 필수 학점</p>
                <p style='color: #9ca3af; font-size: 12px; margin: 0;'>
                    교과 174 + 창체 18
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div style='background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
                        border-radius: 16px; padding: 36px 20px; text-align: center;
                        min-height: 200px;
                        box-shadow: 0 1px 3px rgba(0,0,0,0.04);'>
                <h1 style='color: #6366f1; font-size: 56px; font-weight: 900; 
                           margin: 0; letter-spacing: -2px;'>{required_count}</h1>
                <p style='color: #1f2937; font-size: 16px; font-weight: 700; 
                          margin: 16px 0 6px 0;'>학교지정 과목</p>
                <p style='color: #9ca3af; font-size: 12px; margin: 0;'>
                    필수 이수
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div style='background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
                        border-radius: 16px; padding: 36px 20px; text-align: center;
                        min-height: 200px;
                        box-shadow: 0 1px 3px rgba(0,0,0,0.04);'>
                <h1 style='color: #6366f1; font-size: 56px; font-weight: 900; 
                           margin: 0; letter-spacing: -2px;'>{elective_count}</h1>
                <p style='color: #1f2937; font-size: 16px; font-weight: 700; 
                          margin: 16px 0 6px 0;'>학생선택 과목</p>
                <p style='color: #9ca3af; font-size: 12px; margin: 0;'>
                    그룹별 택N
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── 구분선 ────────────────────────────────────
    st.markdown(
        "<hr style='margin: 40px 0 24px 0; border: none; "
        "border-top: 1px solid #e5e7eb;'>",
        unsafe_allow_html=True,
    )

    # ── 사용법 안내 ───────────────────────────────
    st.markdown(
        """
        <h3 style='color: #1f2937; font-size: 22px; font-weight: 800; 
                   margin: 0 0 16px 0;'>
            📖 이 가이드북 사용법
        </h3>
        <ol style='color: #374151; font-size: 15px; line-height: 2.2; 
                   padding-left: 24px; margin: 0;'>
            <li>
                <b>🗺️ 핵심 이수 경로</b> 
                — 졸업까지 반드시 이수해야 하는 영역과 학점을 확인하세요.
            </li>
            <li>
                <b>📚 학년별 교과목 탐색</b> 
                — 학년·학기별 과목 카드를 살펴보세요.
            </li>
            <li>
                <b>🧮 시간표 시뮬레이터 ⭐</b> 
                — 직접 과목을 체크해보고 졸업 요건 충족 여부를 확인할 수 있어요.
            </li>
            <li>
                <b>🎓 2028 대입 권장 과목</b> 
                — 진로 계열별 추천 과목을 안내합니다.
            </li>
            <li>
                <b>📄 결과 출력</b> 
                — 시뮬레이션 결과를 PDF/HTML로 저장해 상담 자료로 활용하세요.
            </li>
        </ol>
        """,
        unsafe_allow_html=True,
    )

    # ── 푸터 ──────────────────────────────────────
    st.markdown(
        "<hr style='margin: 40px 0 16px 0; border: none; "
        "border-top: 1px solid #e5e7eb;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p style='text-align: center; color: #9ca3af; font-size: 12px; margin: 0;'>
            © 신선여자고등학교 고교학점제 이수 가이드북 · Made with Streamlit
        </p>
        """,
        unsafe_allow_html=True,
    )
