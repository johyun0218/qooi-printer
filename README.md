## qro 의 barcode printer 설정 및 실행

### 👙 python 웹서버 실행

 - print_start.bat 파일을 관리자 권한으로 실행 
 - 해당 파일을 바탕화면에 바로가기 해서 실행해도 됨



<details>
    <summary>📖 처음 사용자를 위한 설치</summary>

<!-- summary 아래 한칸 공백 두고 내용 삽입 -->




#### 🚕 python 설치
    https://www.python.org/downloads/

    설치 시 window path 추가 옵션 체크

#### 🚕 java 설치
    https://yungenie.tistory.com/11


#### 📂 프린트 이름 찾기 command
```bash
wmic printer get name,portname
```


#### 📂 프로젝트 시작 
##### 다운받은 폴더로 이동

* .env 파일을 메모장으로 열어(파일이 없으면 생성 ) -> 파일이름 앞에 . 이 들어가는거 유의
* 프린트 이름 찾기 command 를 명령 프롬프트 창에서 실행하여 나온 명을 
* .env 파일에 입력합니다.
    ```env
    ex)
    PRINTER_NAME="Argox CP-2140EX"
    ```

</details>
