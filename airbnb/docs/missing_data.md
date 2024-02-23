# 결측치 처리
이 문서는 AB_NYC_2019.csv 파일의 결측치 처리에 대한 설명입니다.

## 결측치 개요
- name & host_name에 대한 결측치 처리
- last_review & reviews_per_month에 대한 결측치 처리

## name & host_name 열의 결측치 처리
- 처리 방법 설명: name과 host_name을 'empty_data'로 대체하기로 결정
- 처리 방법 선택 이유: 약 50,000 개의 데이터에서 이 두 데이터는 37 개 밖에 되지 않음.  
그러나 대체를 함으로써 name과 host_name을 등록하지 않은 경우, 이용객수를 파악하는데 용이할 것이라 판단.

## last_review & reviews_per_month 열의 결측치 처리
- 처리 방법 설명: last_review와 reviews_per_month도 각각에 맞게 대체하기로 결정.
- 처리 방법 선택 이유: 우선 결측치가 약 18%를 차지할 정도로 많음. 그리고 결측치가 생긴 이유는 number_of_reviews가 0인 경우.  
즉, 아무도 리뷰를 작성하지 않았기 때문에 결측치가 되었다. 따라서 last_review는 현재 날짜로 대체, reviews_per_month는 0으로 대체.

## 결론
결측치는 인과관계가 분명하게 있다. 그러니 주도면밀하게 데이터를 분석하는 능력이 있어야 한다.