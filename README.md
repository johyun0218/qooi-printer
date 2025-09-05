### 📂 프로젝트 구조

```
qooi-printer/
 ├─ app.py
 ├─ run.py
 ├─ requirements.txt
 └─ qooi-print.jar
```


### python 설치
    https://www.python.org/downloads/

    설치 시 window path 추가 옵션 체크




### 프로젝트 시작 

```python
python -m venv venv
venv\Scripts\activate # 맥) source venv/bin/activate 
pip install -r requirements.txt

python run.py

```


### 프린트 이름 찾기 command
```bash
wmic printer get name,portname
```

