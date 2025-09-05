from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

LABEL_TEMPLATE = "labels/asset-template.prn"
PRINTER_NAME = "Argox CP-2140EX-USB"  # 윈도우 제어판에 표시된 프린터 이름
PRN_OUTPUT = "labels/asset-output.prn"


def print_label(name: str, date: str, qr: str):
    """라벨 템플릿을 불러와 변수 치환 후 Argox 프린터로 전송"""

    print(f"라벨 출력 요청: {name}, {date}, {qr}")

    # 1) 템플릿 읽기 (바이너리 모드)
    with open(LABEL_TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    # 2) bytes → str 변환 (임시: cp1252 또는 latin-1 안전 변환)
    # template_str = template.decode("latin-1")    
    print(template)

    # 2) 데이터 치환
    content = (
        template.replace("{{name}}", name)
        .replace("{{qr_data}}", qr)
    )

    print(content)

    # content_bytes = content_str.encode("latin-1")


    # 3) 파일로 저장
    with open(PRN_OUTPUT, "w", encoding="utf-8") as f:
        f.write(content)

    # 4) 프린터로 전송
    # --- (A) USB 프린터 (윈도우 공유 프린터 방식) ---
    os.system(f'COPY /B "{PRN_OUTPUT}" "\\\\NucBoxG2\\{PRINTER_NAME}"')

    # --- (B) 네트워크 프린터 (주석 해제해서 사용) ---
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect(("192.168.0.50", 9100))  # Argox 네트워크 프린터 IP:PORT
    # sock.sendall(content.encode("utf-8"))
    # sock.close()

def print_jar(device_name: str, mng_data: str, product_data: str, purchase_data: str, qr: str):
    # print("print jar called")
    # 실행할 JAR 파일
    jar_file = "qooi-print.jar"

    printer_logger = "Y" # "Y"로 설정하면 qooi-print.jar 내부에서 로그를 logs/qooi-print.log에 기록

    # 파라미터 (예: arg1 arg2)
    params = [device_name, mng_data, product_data, purchase_data, qr, printer_logger]

    # 실행 명령어
    cmd = ["java", "-jar", jar_file] + params

    # print("Executing command:", " ".join(cmd))

    # 실행
    result = subprocess.run(cmd, 
                            capture_output=True, 
                            text=True,          # stdout/stderr을 str로 받음
                            encoding="cp949")    # 출력 인코딩 강제 (윈도우에서 cp949 필요할 수 있음))  linux: utf-8
    

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

@app.route("/print", methods=["POST"])
def print_api():
    """라벨 출력 API"""
    data = request.json
    device_name = data.get("device_name", "")
    mng_data = data.get("mng_data", "")
    product_data = data.get("product_data", "")
    purchase_data = data.get("purchase_data", "")
    qr = data.get("qr", "")

    try:
        print_jar(device_name, mng_data, product_data, purchase_data, qr)
        return jsonify({"status": "ok", "msg": "라벨 출력 완료"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500


if __name__ == "__main__":
    # 로컬에서 실행
    app.run(host="0.0.0.0", port=5001)
