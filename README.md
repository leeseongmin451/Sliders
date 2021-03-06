SLIDERS
==============
파이썬 모듈 PyGame을 이용하여 만든 아케이드 게임입니다.  
2~4명의 플레이어가 자신의 색깔로 땅을 색칠해가며 영역을 넓히는 땅따먹기 방식의 간단한 게임입니다.

# 실행 방법
아직 별도의 실행 파일이 없어 python version 3.8 이상이 필요합니다.  
모든 파일을 다운받아 압축을 해제하고 생성된 폴더 안에 pygame 모듈을 설치해야 합니다.  
그 상태에서 slider_game.py 파일을 실행합니다.

# 조작법
1. 플레이어 수는 최소 2명에서 최대 4명까지 가능합니다.
2. 플레이어 1 : 파란색, WSAD
3. 플레이어 2 : 빨간색, 방향키
4. 플레이어 3 : 초록색, 숫자 키패드 8546
5. 플레이어 4 : 노란색, IKJL

# 게임 구성 및 플레이 과정
## 메인 메뉴
게임 실행 시 처음 나오는 화면입니다. 제목과 시작 버튼, 그리고 설정 버튼으로 이루어져 있습니다.

![mainmenu_scene](https://user-images.githubusercontent.com/80591422/163200082-be25c819-4507-4c65-b99f-ff74758494ca.png)

## 플레이 화면 및 플레이 과정
메인 메뉴 화면에서 시작 버튼을 누르면 나오는 화면입니다.  
플레이어들이 있는 정사각형 타일 그리드와 점수 창, 벽 재배치 버튼, 그리고 게임 종료 버튼으로 이루어져 있습니다.

![gameplay_scene](https://user-images.githubusercontent.com/80591422/163200900-9640ea33-c9d1-4489-b07a-fb0549503334.png)

각 플레이어는 각자에게 할당된 조작키를 사용하여 상하좌우로 움직입니다.  
플레이어가 움직일 때마다 자신이 지나간 그리드 칸을 자신의 색깔로 색칠합니다. 색칠한 영역은 자신의 것입니다.  
자신의 색깔로 색칠된 칸의 수가 자신의 점수가 됩니다. 타 플레이어의 영역을 지나감으로서 해당 플레이어의 점수를 깎을 수도 있습니다.  
벽에 막혀 어디로도 움직이지 못하는 상황이 발생할 수 있습니다. 이때에는 "REARRANGE"버튼을 눌러 벽을 랜덤하게 재배치합니다.  
"QUIT GAME" 버튼을 눌러 메인 메뉴 화면으로 돌아갈 수 있습니다.  

## 설정 창
메인 메뉴 화면에서 설정 버튼을 누르면 나오는 화면입니다.  

![settings_scene](https://user-images.githubusercontent.com/80591422/163201599-68302778-d863-40f2-b738-ffed27bf65ad.png)

설정 창에서 변경 가능한 사항은 다음과 같습니다.  

* 플레이어 수 : 최소 2명, 최대 4명까지 설정할 수 있습니다.
* 타일 그리드 사이즈 : 최소 5x5, 최대 40x40까지 설정할 수 있습니다.
* 벽의 밀도 : 최소 5%, 최대 15%까지 설정할 수 있습니다.

# 플레이 스크린샷

![gameplay_scene](https://user-images.githubusercontent.com/80591422/163202802-73c86afb-b95c-402f-8409-789f2dda60ac.png)
