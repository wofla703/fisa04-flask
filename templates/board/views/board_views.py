# Blueprint 기능을 사용해서 collection/no1/
# Blueprint 기능을 사용해서 collection/no2/
from flask import Blueprint, render_template
from ..models import Question


# 특정 / url / 하위에 있는 함수들을 일괄적으로 관리하기 위해 사용
#  코드에서 부르는 상대적 이름,실제 파일명,url에 매칭되는 경로 
bbp = Blueprint('collection',__name__,url_prefix='/board')

# 1. html화면에 표시

@bbp.route('/boardlist')
def list():    
    question = Question.query.all()
    return render_template('board_List.html',question_list=question)

# 2. 필요한 함수들

# 개별 게시글을 조회할 수 있는 함수 필요
@bbp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('boardDetail.html',question=question)

# 개별 게시글을 작성하는 함수 

# 개별 게시글을 수정하는 함수

# 댓글 작성하는 함수

# 댓글 수정하는 함수

# 댓글 삭제하는 함수 

@bbp.route('/no1')
def hello2():
    return f'{__name__} 첫번째'
    
@bbp.route('/no2')
def hello3():
    return f'{__name__} 두번째'
    