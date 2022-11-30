"""
https://blog.naver.com/PostView.nhn?blogId=chandong83&logNo=221436424539&categoryNo=29&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
https://deep-learning-study.tistory.com/244


ㅡㅡㅡㅡ
조도 센서를 활용하여 어두운 상황에서 카메라 밝기(명암 조절)를 조절
어두운 상황에서 임계값을 조절하면 원하지 않는 결과가 나왔어서 ~
캐니를 활용하여 검출을 하는 방법도 있지만 우선 임계값만 조절을 하여 ~했다.

만약 교수님이 캐니를 어떤식으로 활용할거냐 하면
(이건 아마 안 물어보실 것 같음)
캐니가 어두운 상황에서 엣지 인식이 잘 되어서 _INV를 활용하여 이미지 처리를 할 예정이다.
가우시안 블러나 적응형 MEAN 등을 사용하여 인식율을 높일 것 이다.


ㅡㅡㅡㅡ


user'+str(count)+'.jpg

예시
user0.jpg
user1.jpg
...
user100.jpg



반복문:
    조도센서 값 가져오기
    임계값 조절이나 조건문(= LED 또는 여러 상황에 대비하여 직접 개발)
    데이터 학습된 것을 기반으로 얼굴 인식

만약에 키패드를 누르면 계속 입력은 받는데

근데 입력하다가 얼굴 인식을 하겠다 하면
입력 받는 것을 멈추거나 아니면 저장을 해두고 얼굴 인식으로 넘어가야 하는데


방법은 여러가지
1. 인터럽트 사용하기
2. 얼굴 인식 기능에 얼굴이 인식이 안 될 경우 작동 안 함. > 대기 모드
3. 키 입력이 될 경우 얼굴 인식 빠져나오기
4. 반복문에 같이 다 때려넣기


# 키패드
if (key == [0,1])
    1

keyPass = []
keyPass.append = key

print(keyPass)
= 123456

if keyPass == password:
    unlock
else:
    알람이나 경고

"""