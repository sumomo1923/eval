from django.db import models
from django.contrib.auth.models import User

STUDENT_NUM = [
    ('학습자_00', ''),
    ('학습자_01', '학습자_01'),
    ('학습자_02', '학습자_02'),
    ('학습자_03', '학습자_03'),
    ('학습자_04', '학습자_04'),
    ('학습자_05', '학습자_05'),
    ('학습자_06', '학습자_06'),
    ('학습자_07', '학습자_07'),
    ('학습자_08', '학습자_08'),
    ('학습자_09', '학습자_09'),
    ('학습자_10', '학습자_10'),
    ('학습자_11', '학습자_11'),
    ('학습자_12', '학습자_12'),
    ('학습자_13', '학습자_13'),
    ('학습자_14', '학습자_14'),
    ('학습자_15', '학습자_15'),
    ('학습자_16', '학습자_16'),
    ('학습자_17', '학습자_17'),
    ('학습자_18', '학습자_18'),
    ('학습자_19', '학습자_19'),
    ('학습자_20', '학습자_20'),
    ('학습자_21', '학습자_21'),
    ('학습자_22', '학습자_22'),
    ('학습자_23', '학습자_23'),
    ('학습자_24', '학습자_24'),
    ('학습자_25', '학습자_25'),
    ('학습자_26', '학습자_26'),
    ('학습자_27', '학습자_27'),
    ('학습자_28', '학습자_28'),
    ('학습자_29', '학습자_29'),
    ('학습자_30', '학습자_30'),
    ('학습자_31', '학습자_31'),
    ('학습자_32', '학습자_32'),
    ('학습자_33', '학습자_33'),
    ('학습자_34', '학습자_34'),
    ('학습자_35', '학습자_35'),
    ('학습자_36', '학습자_36'),
    ('학습자_37', '학습자_37'),
    ('학습자_38', '학습자_38'),
    ('학습자_39', '학습자_39'),
    ('학습자_40', '학습자_40'),
    ('학습자_41', '학습자_41'),
    ('학습자_42', '학습자_42'),
    ('학습자_43', '학습자_43'),
    ('학습자_44', '학습자_44'),
    ('학습자_45', '학습자_45'),
    ('학습자_46', '학습자_46'),
    ('학습자_47', '학습자_47'),
    ('학습자_48', '학습자_48'),
    ('학습자_49', '학습자_49'),
    ('학습자_50', '학습자_50'),
    ('학습자_51', '학습자_51'),
    ('학습자_52', '학습자_52'),
]

ITEM_TYPE = [
    ('w0', ''),
    ('단어', '단어'),
    ('문장', '문장'),
    ]

EVAL_COMPONENT = [
    ('', ''),
    ('모음_단모음', '모음_단모음'),
    ('모음_이중모음', '모음_이중모음'),
    ('자음(받침 포함)_ㄹ', '자음(받침 포함)_ㄹ'),
    ('자음_ㅎ', '자음_ㅎ'),
    ('자음_ㅂ, ㅃ, ㅍ', '자음_ㅂ, ㅃ, ㅍ'),
    ('자음_ㄷ, ㄸ, ㅌ', '자음_ㄷ, ㄸ, ㅌ'),
    ('자음_ㅅ, ㅆ', '자음_ㅅ, ㅆ'),
    ('자음_ㅈ, ㅉ, ㅊ', '자음_ㅈ, ㅉ, ㅊ'),
    ('자음_ㄱ, ㄲ, ㅋ', '자음_ㄱ, ㄲ, ㅋ'),
    ('자음_받침_ㅁ, ㄴ, ㅇ, ㅂ, ㄷ, ㄱ', '자음_받침_ㅁ, ㄴ, ㅇ, ㅂ, ㄷ, ㄱ'),
    ('평서문: 연음, 비음화', '평서문: 연음, 비음화'),
    ('평서문: 연음, 경음화, 격음화', '평서문: 연음, 경음화, 격음화'),
    ('명령문: 연음, 경음화, 격음화, ㅎ탈락/약화', '명령문: 연음, 경음화, 격음화, ㅎ탈락/약화'),
    ('의문사 있는 의문문: 연음, ㄴ첨가, ㅎ탈락/약화, 격음화', '의문사 있는 의문문: 연음, ㄴ첨가, ㅎ탈락/약화, 격음화'),
    ('의문사 없는 의문문: 연음, 경음화', '의문사 없는 의문문: 연음, 경음화'),
    ('의문사 없는 의문문: 연음, 유음화, ㅎ탈락/약화', '의문사 없는 의문문: 연음, 유음화, ㅎ탈락/약화'),
    ('선택 의문문: 연음/유음화, ㅎ탈락/약화', '선택 의문문: 연음, 유음화, ㅎ탈락/약화'),
    ('청유문: 연음, 경음화, 구개음화', '청유문: 연음, 경음화, 구개음화'),
    ('감탄문: 연음, 경음화, 비음화', '감탄문: 연음, 경음화, 비음화'),
    ('평서문: 연음, 경음화, 비음화', '평서문: 연음, 경음화, 비음화'),

]

ITEM_TEXT = [
    ('', ''),
    ('가구', '가구'),
    ('가끔', '가끔'),
    ('가족', '가족'),
    ('거리', '거리'),
    ('궤도', '궤도'),
    ('그것', '그것'),
    ('기차', '기차'),
    ('꼬리', '꼬리'),
    ('꽃', '꽃'),
    ('끝', '끝'),
    ('나의 가방', '나의 가방'),
    ('날씨', '날씨'),
    ('더워요', '더워요'),
    ('돈', '돈'),
    ('뒤', '뒤'),
    ('뚱뚱하다', '뚱뚱하다'),
    ('메모', '메모'),
    ('몰라요', '몰라요'),
    ('바다', '바다'),
    ('바쁘다', '바쁘다'),
    ('밖', '밖'),
    ('밤', '밤'),
    ('밥', '밥'),
    ('비싸다', '비싸다'),
    ('빠르다', '빠르다'),
    ('사과', '사과'),
    ('사랑', '사랑'),
    ('소개', '소개'),
    ('숲', '숲'),
    ('시간', '시간'),
    ('시키다', '시키다'),
    ('쓰다', '쓰다'),
    ('아이', '아이'),
    ('아프다', '아프다'),
    ('야구', '야구'),
    ('얘기', '얘기'),
    ('어느', '어느'),
    ('여기', '여기'),
    ('예약', '예약'),
    ('오이', '오이'),
    ('왜냐하면', '왜냐하면'),
    ('요리', '요리'),
    ('우산', '우산'),
    ('웨이터', '웨이터'),
    ('의자', '의자'),
    ('이따가', '이따가'),
    ('이유', '이유'),
    ('이틀', '이틀'),
    ('자동차', '자동차'),
    ('저희', '저희'),
    ('주말', '주말'),
    ('진짜', '진짜'),
    ('찌개', '찌개'),
    ('친하다', '친하다'),
    ('크다', '크다'),
    ('튼튼하다', '튼튼하다'),
    ('포도', '포도'),
    ('하나', '하나'),
    ('할아버지', '할아버지'),
    ('해외', '해외'),
    ('회의', '회의'),
    ('작년에 생일 선물로 받은 신발입니다.', '작년에 생일 선물로 받은 신발입니다.'),
    ('집에 큰 창문이 없어서 답답해요.', '집에 큰 창문이 없어서 답답해요.'),
    ('좋아하는 노래를 듣고 싶으면 이렇게 하세요.', '좋아하는 노래를 듣고 싶으면 이렇게 하세요.'),
    ('오늘은 할 일이 너무 많은데 뭐부터 시작할까요?', '오늘은 할 일이 너무 많은데 뭐부터 시작할까요?'),
    ('꽃집 앞에서 오 분만 기다릴 수 있어요?', '꽃집 앞에서 오 분만 기다릴 수 있어요?'),
    ('아침에는 버스보다 지하철이 더 편리해요?', '아침에는 버스보다 지하철이 더 편리해요?'),
    ('연락처는 이메일 주소를 쓸까요? 전화번호를 쓸까요?', '연락처는 이메일 주소를 쓸까요? 전화번호를 쓸까요?'),
    ('내일은 도서관에서 같이 공부합시다.', '내일은 도서관에서 같이 공부합시다.'),
    ('새로 나온 음료수 먹어 봤는데 진짜 맛있네!', '새로 나온 음료수 먹어 봤는데 진짜 맛있네!'),
    ('식당에 갔는데 문을 닫아서 그냥 왔어요. ', '식당에 갔는데 문을 닫아서 그냥 왔어요. '),
    ]

class Student(models.Model):
    name = models.CharField("학습자 번호", choices=STUDENT_NUM, max_length=100, default="")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Eval_item(models.Model):
    my_id = models.IntegerField(blank=True)
    item_text = models.CharField("평가 단어/문장", choices=ITEM_TEXT, max_length=100, default="")
    item_component = models.CharField("평가 요소", max_length=200, choices=EVAL_COMPONENT, default="")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_text

class AudioFile(models.Model):
    student_number = models.CharField("학습자 번호", choices=STUDENT_NUM, max_length=100, default="")
    item = models.ForeignKey(Eval_item, on_delete=models.CASCADE, verbose_name='평가 단어/문장')
    item_type = models.CharField("평가 대상 종류", max_length=200, choices=ITEM_TYPE, default="")
    audio_file = models.FileField("학습자 음성 파일", upload_to='', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    eval_completed = models.CharField("평가 완료 여부", max_length=10, default='미완료')

    def __str__(self):
        return self.student_number

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='평가자', default="")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='학습자 번호', default="")
    eval_item = models.ForeignKey(Eval_item, on_delete=models.CASCADE, verbose_name='평가 대상', default="")
    rating_ho = models.IntegerField("총체적 평가", default='')
    rating_un = models.IntegerField("이해도", default='')
    rating_fu = models.IntegerField("유창도", default='')
    rating_ac = models.IntegerField("정확도", default='')
    rating_ph = models.IntegerField("자음/모음", default='')
    rating_accent = models.IntegerField("억양/강세", default='')
    rating_rule = models.IntegerField("발음 규칙", default='')
    rating_pause = models.IntegerField("휴지/머뭇거림", default='')
    eval_completed = models.BooleanField("평가 완료 여부", default='미완료')
    uploaded_at = models.DateTimeField("평가 일시", auto_now_add=True)

    def __str__(self):
        return self.eval_item.item_text