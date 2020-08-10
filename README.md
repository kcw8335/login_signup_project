# login_signup_project 실행 방법

- python 3.6.8
- django 3.1

- 디렉터리(폴더)를 생성한 후에 디렉터리를 경로로 visual studio code를 실행해줍니다.
- git clone https://github.com/kcw8335/login_signup_project - git clone 명령어로 프로젝트를 복사해줍니다.

- python -m venv virtual_machine - 가상환경 생성
- source virtual_machine/Scripts/activate - 가상환경 실행

- pip list 명령어를 이용하여 설치된 패키지들을 확인
- python -m pip install --upgrade pip - pip 버전 업그레이드
- pip install django - django 설치

- cd login_signup_project/ - manage.py가 있는 디렉터리로 경로를 이동

- python manage.py makemigrations - 마이그레이션 파일들을 생성
- python manage.py migrate - 생성된 마이그레이션 파일들을 적용
- python manage.py createsuperuser - 관리자 계정 생성
- python manage.py runserver - 개발자 서버 실행
