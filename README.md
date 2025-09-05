### 📂 프로젝트 구조

```
qooi-printer/
 ├─ app.py
 ├─ requirements.txt
 └─ labels/
     └─ asset-template.prn   (자산 라벨 템플릿)
```


### python 설치
    https://www.python.org/downloads/

    설치 시 window path 추가 옵션 체크




### 프로젝트 시작 

```python
python -m venv venv
venv\Scripts\activate # 맥) source venv/bin/activate 
pip install -r requirements.txt

```


### 프린트 찾기 성공

wmic printer get name,portname

copy app.py  "\\NucBoxG2\Argox CP-2140EX-USB"

N
q400
Q200,24
b20,20,0,4,2,2,80,M,"1234567890"
A150,20,0,3,1,1,N,"홍길동1"
A150,60,0,3,1,1,N,"{{date}}"
P1