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


### 프린트 이름 찾기 command
```bash
wmic printer get name,portname
```


### 프로젝트 시작 
#### 다운받은 폴더로 이동

* .env 파일을 메모장으로 열어
* 프린트 이름 찾기 command 를 명령 프롬프트 창에서 실행하여 나온 명을 
* .env 파일에 입력합니다.
    ```env
    ex)
    PRINTER_NAME="Argox CP-2140EX-USB"
    ```

#### 파이썬 실행
```python
python -m venv venv
venv\Scripts\activate # 맥) source venv/bin/activate 
pip install -r requirements.txt

python run.py

```


