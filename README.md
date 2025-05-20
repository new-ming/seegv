
![main](https://github.com/user-attachments/assets/2678c774-98cc-4974-b1ce-095acf91beca)

<h1 align="center">django 프로젝트</h1>
<h3 align="center">영화관 사이트 SEEGV</h3>

<br><br><br>

## 목차
- [개요](https://github.com/new-ming/ClassIT_won#개요)
- [기술 스택](https://github.com/new-ming/ClassIT_won#기술-스택)
- [프로젝트 설계](https://github.com/new-ming/ClassIT_won#프로젝트-설계)
- [핵심 기능](https://github.com/new-ming/ClassIT_won#핵심-기능)
- [주요기능 실행화면](https://github.com/new-ming/ClassIT_won#주요기능-실행화면)
- [개선사항](https://github.com/new-ming/ClassIT_won#개선사항)


## 개요 
* 프로젝트 목표 : Python을 사용하여 진행된 Django 프로젝트
* 개발기간 : 24/3/18 ~ 24/5/6
<br>

## 기술 스택
  - Language : `Python(3.8)`, `JavaScript(ES6)`
  - Library & Framework : `Django (3.2.24)`, `jQuery (3.6.0)`, `Bootstrap (5.3.3)`
  - Database : `Oracle Database (21c - ojdbc8)`
  - Target : `Web Browser`
  - Tool : `Visual Studio Code`
  - ETC : `Git`
<br>

## 프로젝트 설계,구현 PPT
 
<div align="center">
    
|||
| :-------------: | :-------------: | 
|||
|||
|||
|||
|||
|||
</div>
<br>



## 핵심 기능
  #### 클래스
   - 클래스 검색
   - 클래스 개별 정보 제공
  #### 예약
   - 시간과 인원을 선택하여 클래스를 예약할 수 있다.
   - 포트원 API를 통해 카카오와 KG이니시스 결제를 구현하였다.
  #### 회원정보(Security)
   - 회원가입
   - 로그인
   - 아이디 찾기
   - 비밀번호 초기화
   - 개인정보 수정
  #### 유저
   - 클래스 예약 정보 확인/취소
   - 리뷰 작성/수정/삭제
   - QnA질문 작성/수정/삭제
  #### 클래스 관리자
   - 예약 확인/승인
   - QnA답변 작성/삭제
  #### 최종관리자
   - 클래스 신규 등록

  


## 주요기능 실행화면
  ### 메인화면
   * **클래스보기**
   * **클래스 추천**
   * **회원가입/마이페이지/관리페이지**
   * **로그인/로그아웃**
  
  ### 클래스 검색 페이지
  * 클래스 검색
    * 카테고리 선택과 키워드 입력을 통해 `검색`이 가능합니다.<br>
  * 클래스 리스트
    * 개별 클래스를 선택하면 `클래스 상세페이지`로 이동합니다.<br>

  ![클래스잇 클래스검색(비로그인)](https://github.com/user-attachments/assets/2a296a00-a4fe-4134-8cc6-8d1d13fdf26b)
  
  ### 개별클래스
   * **클래스 상세 설명**
     * 개별 클래스 페이지
       * 클래스 `예약` 기능 
       * 선택된 클래스의 `상세설명`과 `카카오지도 API`를 통해 위치를 표시하고 있습니다.
       * 해당 클래스의 `리뷰게시판`과 `QnA게시판`이 생성됩니다.<br>
      
     ![클래스잇 상세페이지(비로그인)](https://github.com/user-attachments/assets/b34080b7-a279-40ef-b350-5d377e422621)
     
   * **클래스 예약**
     * 일정과 인원 설정
       * 클래스 일정과 예약 인원을 선택할 수 있으며 `결제페이지`로 이동합니다.
     * 결제페이지
       * 예약하는 클래스 정보/ 결제정보/ 사용자 정보 확인
     * open API를 통한 결제>
       * 카카오페이와 KG이니시스의 `결제` 시스템이 이용 가능합니다.<br>
       
     ![(사용자)상세페이지-결제](https://github.com/user-attachments/assets/e7a32c51-317e-4a38-97f1-d702268951bb)
       
   * **후기게시판**
     * 후기 확인
       * 해당 클래스의 후기가 `페이징` 되어 보여집니다.<br>
       
     ![(사용자)상세페이지-리뷰](https://github.com/user-attachments/assets/b1929659-c319-4654-be9e-d3fbfcf27e5e)
       
   * **문의게시판**
      * 문의 확인
        * 해당 클래스의 문의사항이 `페이징` 되어 보여집니다.<br>
        
      ![(사용자)상세페이지-문의](https://github.com/user-attachments/assets/0e1263d4-4c45-4e05-af5d-ab0b117bfa97)  
      
      * 문의 추가
        * 로그인 되어있는 회원은 문의하기 버튼이 생성됩니다.
        * 버튼을 클릭하면 `모달`을 통해 문의사항을 입력, 등록이 가능합니다.<br>
        
      ![(사용자)상세페이지-문의추가](https://github.com/user-attachments/assets/b0bec65c-ec81-483e-af78-fe328da01281) 
       
      * 문의 삭제
        * 문의 글을 입력한 회원에게는 `삭제버튼`이 보여집니다.
        * 삭제버튼 클릭 시 문의글 삭제가 가능합니다.<br>
        
     ![(사용자)상세페이지-문의삭제](https://github.com/user-attachments/assets/8086dff4-3e7a-4043-864e-a84b6c5af38a)

      * 답변 확인
        * 답글이 있는 경우 답변 버튼을 눌러 답글을 확인 가능합니다.
      * 답변 추가
        * 해당 클래스의 관리자 혹은 문의글을 입력한 회원이 답글을 누르면 답글 아래 답글을 입력할 수 있는 `입력란`이 생성됩니다.<br>
        
      ![(사용자)상세페이지-문의댓글추가](https://github.com/user-attachments/assets/b17197bc-1a61-45e6-969f-00e8fcb6495f) 
     
      * 답변 삭제
        * 답변을 입력한 회원에게는 삭제 버튼이 보여지며 클릭 시 답변 삭제가 가능합니다.
          
      ![(사용자)상세페이지-문의댓글삭제](https://github.com/user-attachments/assets/1bb80742-11c6-4e04-b647-0af3dc260b38)

  ### 클래스 추천
   * 문답 페이지
      * 문답을 통해 해당하는 개별 클래스로 연결됩니다.
      
  ![클래스잇 추천클래스](https://github.com/user-attachments/assets/b0a28948-0b35-4851-abbf-e87e55b08215)
  
  ### 마이페이지
  ![(사용자)마이페이지](https://github.com/user-attachments/assets/abab136f-9d39-4096-9221-4bebba7dc7b5)
  
   * **회원정보 확인**
     * 회원정보 확인
     * 회원정보 수정
       * 수정 버튼을 눌러 회원정보 수정이 가능합니다.
         
     ![(사용자)상세페이지-정보수정](https://github.com/user-attachments/assets/4f1b0d8c-a9d7-4387-aa0c-96654fa1ba53)
  
   * **예약/리뷰**
     * 예약클래스 정보
       * 날짜에 따라서 예정된 클래스와 완료 된 클래스로 구분됩니다.
       * 예정된 클래는 수강일 1일 전까지 `취소버튼` 활성화됩니다.
       * 승인이 거부되면 버튼이 표시되지 않습니다.
       * 취소버튼을 클릭 시 예약정보가 삭제됩니다. (결제취소는 구현되지 않았습니다.)
       * 완료된 클래스는 `리뷰쓰기 버튼`이 활성화되며 리뷰 작성 후에는 `리뷰보기 버튼`이 활성화됩니다
       * 승인이 거부된 예약은 버튼이 표시되지 않습니다.
         
     ![(사용자)마이페이지-예약리뷰](https://github.com/user-attachments/assets/7f4806aa-2c04-408c-8f6c-f418197a0454)

     * 리뷰 작성
       * 작성된 리뷰가 없는 예약정보는 리뷰작성 버튼이 활성화됩니다.
       * 리뷰작성 버튼을 클릭하면 `모달`창을 통해 리뷰 입력이 가능하며 등록버튼을 통해 등록이 완료됩니다.

     ![(사용자)마이페이지-예약리뷰-리뷰작성](https://github.com/user-attachments/assets/35594af0-e105-414b-9229-9eb6f24577ad) 

     * 리뷰 확인
       * 작성된 리뷰가 있는 예약정보는 `리뷰보기 버튼`이 활성화 됩니다.
       * 리뷰보기 클릭시 입력한 리뷰를 확인 할 수 있습니다.
      
     ![(사용자)마이페이지-예약리뷰-리뷰보기](https://github.com/user-attachments/assets/631642f9-14c5-4950-9508-5d485c664cd8)
 
     * 리뷰 수정
       * 리뷰확인 `모달`에서 `수정버튼`을 클릭하면 리뷰내용을 수정 할 수 았습니다
       * 저장 버튼 클릭 시 수정된 리뷰를 저장 할 수 있습니다.

     ![(사용자)마이페이지-예약리뷰-리뷰수정](https://github.com/user-attachments/assets/ca0d6d76-992e-4e1f-8d31-a5b034a5879e)

     * 리뷰 삭제
        * 리뷰확인 `모달`에서 `삭제버튼`을 클릭하면 리뷰를 삭제 할 수 있습니다.

     ![(사용자)마이페이지-예약리뷰-리뷰삭제](https://github.com/user-attachments/assets/67f8ba2c-801e-4c89-81ed-749b9736c6c3)
       
   * **QnA**
     * 질문 및 답변 확인
        * 답변 여부에 따라서 미답변/답변완료로 구분됩니다.
        * `질문`과 연결 된 `답글` 함께 보여집니다.
        * 질문을 기준으로 `페이징`되어 보여집니다.

     ![(사용자)마이페이지-qna](https://github.com/user-attachments/assets/ceb971ce-0b85-4616-bc27-f5728e4db1e9)

          
     * 질문 삭제
        * 질문 삭제 버튼을 누르면 작성했던 질문을 삭제 할 수 있습니다.
     * 입력한 답글 삭제
        * 답변 삭제 버튼을 누르면 작성했던 답글을 삭제 할 수 있습니다.
          
     ![(사용자)마이페이지-qna-질문 댓글 삭제](https://github.com/user-attachments/assets/68f9e22b-fce6-45cd-8174-e22769ed7fc8)

  ### 관리페이지
   * **예약관리**
     * 예약 정보 확인
        * 승인 여부에 따라 구분되어 예약 정보를 볼 수 있습니다.
        * 승인 여부가 0:승인예정 일 경우 `승인/거절 버튼`이 활성화 됩니다.
     * 승인/거부
        * 승인/거절 버튼을 누르면 선택한 대로 승인 여부가 변경되며 해당 테이블로 이동합니다.
      
      ![(관리자)관리자페이지-예약승인](https://github.com/user-attachments/assets/fd64b3b7-90e4-4e52-87ee-7261dc53e74f)
      ![(관리자)관리자페이지-예약거절](https://github.com/user-attachments/assets/fd3b5e48-d645-4453-b7ef-13d18addf1eb)

   * **QnA**
     * 질문 및 답변 확인
        * 답변 여부에 따라서 미답변/답변완료로 구분됩니다.
        * 질문과 연결된 답글이 함께 보여집니다.
        * 질문을 기준으로 `페이징`되어 보여집니다.
      
       
     * 답변 추가
        * 미 답변 테이블에서 답변 달기 버튼을 선택하면 답변을 입력공간이 생깁니다.
        * 입력 후 등록 버튼을 누르면 답변이 등록되며 해당 질문은 답변 완료 테이블로 이동하게 됩니다.

      ![(관리자)관리자페이지-qna답변추가](https://github.com/user-attachments/assets/d3b755af-b69b-4297-8439-ef35698afbbe)

          
     * 답변 삭제
        * 답변 완료 테이블에서 답변 삭제 버튼을 누르면 해당 답변은 삭제됩니다.
        * 담당자의 답변이 없는경우 미 답변으로 답변 여부가 변경되어 미 답변 테이블로 이동하게 됩니다.
      
     ![(관리자)관리자페이지-qna답변 삭제](https://github.com/user-attachments/assets/d154d698-145b-45b5-b5cc-ecc8da3386be)

      
  ### 전체관리자


## 개선사항
 * 마이페이지에 정보가 없을 때는 테이블을 비우지 않고 "내역이 없습니다." 등의 문자를 표시



<br><br><br><br><br><br><br><br><br>
