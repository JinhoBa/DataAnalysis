import matplotlib.pyplot as plt
from get_score import score_list


from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 설정
categories = ['홀란', '비니시우스', '사카', '필 포든']
values1 = [340,240,220,220]
values2 = score_list

# 그래프 그리기
plt.bar(categories, values1, width=0.4, align='center', label='트렌트퍼마켓 기준가치')
plt.bar(categories, values2, width=0.4, align='edge', label='자체 평가 가치')

# 축과 제목 설정
plt.xlabel('선수명')
plt.ylabel('가격(백만유로)')
plt.title('축구 유망주 가격 비교')

# 범례 추가
plt.legend()

# 그래프 보여주기
plt.show()