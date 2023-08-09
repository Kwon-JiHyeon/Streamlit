from datetime import datetime as dt
import pandas as pd
from page import st_page as spg
import foliummap as fum

st.title('시험용 메세지입니다.')

tod = todays.strftime('%Y년 %m월 %d일 입니다.')

#st.header는 제목에 사용
st.header(f'오늘은 {tod} 입니다.')

item = st.sidebar.selectbox('아무나 메뉴입니다.',['선택1', '콤보2', '세트3'])

if item == '선택1':
    spg.app()
elif item == '콤보2':
    st.write('2번 콤보를 선택했습니다.')
    df = pd.DataFrame(np.arange(15))
    fg, ax = plt.subplots(figsize=(8,8))
    ax.plot(df)
    st.pyplot(fg)
elif item == '세트3':
    fum.app()