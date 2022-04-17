# wanted_pre_onboarding

## 1. 프로젝트 정보
---
본 서비스는 크라우드 펀딩 기능을 제공합니다.  
게시자는 크라우드 펀딩을 받기 위한 상품(게시물)을 등록합니다.


## 2. 설치 및 실행 방법
---
### Local 개발 및 테스트용
1. 해당 프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
```bash
	git clone https://github.com/Bruno-Jang/wanted_pre_onboarding.git
```
```bash
	cd wanted_pre_onboarding
```

2. 가상 환경 생성 및 실행
```bash
	conda create -n 프로젝트명 python=3.9	
	conda activate 프로젝트명
```
3. Python 패키지 설치
```bash
	pip install -r requirements.txt
```
4. DB 생성 후 model의 변경사항을 DB에 반영한다.
```bash
	python manage.py makemigrations
	python manage.py migrate
```
5. 서버를 실행한다.
```bash
	python manage.py runserver 0.0.0.0:8000
```


## 3. 사용 기술 및 Tools
---
1. Python 3.9
2. Django 4.0
3. MariaDB


## 4. DB modeling
---
![onboarding](https://user-images.githubusercontent.com/75561289/163313870-661c2e29-0e7d-4ab2-8c08-7bef4dd5fb8d.png)


## 5. 구현 기능
---
1. 상품 등록 API
2. 상품 수정 API
3. 상품 삭제 API
4. 상품 목록 조회 API
	- 상품의 제목 검색(Q) 및 정렬 기능(order_by)을 통한 상품 목록 조회하는 기능 구현
	- 상품의 상세 페이지 조회하는 기능 구현
5. 펀딩 API
	- 사용자가 요청한 수량에 따른 펀딩 기능 구현
6. 상품 View 유닛 테스트 작성


### 가장 신경 쓴 부분
1. 확장성을 신경쓰고자 했습니다.  
대량의 데이터, 많은 유저가 사용할 서비스라고 생각하며 코드를 작성했습니다.  
그래서 **select_related 를 활용하여 DB에 최대한 적은 수의 쿼리를 전송**하고자 했습니다.

2. RESTFUL API를 작성하기 위해 노력했습니다.  
uri, 클래스명, 변수명을 비롯한 코드들 모두 최대한 주석이 없어도 팀원분들과 공유가 가능할지를 생각하며 코드를 작성했습니다.


## 6. MariaDB 설치 (Linux 기준)
---
1. sudo apt update && sudo apt upgrade
2. sudo apt-get install -y mariadb-server


## 7. DB 재구축
---
1. 사용할 덤프 파일명 : **onboarding.sql** (root directory에 있습니다.)
2. MariaDB 접속 후 **CREATE DATABASE 데이터베이스명** 입력하여 DB 생성
3. CLI에서 **mysql -u root -p 데이터베이스명 < onboarding.sql** (mysql에서 입력하는 것 아닙니다.)


## 8. 테스트
---
아래에 포스트맨으로 작성한 문서 링크를 공유하니 참고 부탁드리겠습니다.
![상품 등록 post](https://user-images.githubusercontent.com/75561289/163701452-7553c6a1-791e-46b7-bd88-6ac81db1e854.png)
![상품 삭제 delete](https://user-images.githubusercontent.com/75561289/163701507-6f8fa760-28c6-4e21-9165-38385460e0a4.png)
![상품 상세 페이지 조회 get](https://user-images.githubusercontent.com/75561289/163701518-1085c4a8-3d92-4f7c-9cde-328385ec6d51.png)
![상품 전체 리스트 조회 get](https://user-images.githubusercontent.com/75561289/163701523-ab21a69a-cf37-4f79-8593-f3a03cab6d53.png)
![상품 정보 수정 update](https://user-images.githubusercontent.com/75561289/163701542-f25bfef9-eed7-422e-87ec-34983404825c.png)
![펀딩 기능 post](https://user-images.githubusercontent.com/75561289/163701550-276d81d3-2b4c-42b1-9ba3-8a6e266a1b99.png)

<https://documenter.getpostman.com/view/18993145/Uyr4Jeqi>
