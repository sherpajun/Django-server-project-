# django 환경을 불러오기 위해서는 model 
import os

from django.db.models.base import ModelBase

import member

# add_data함수는 django에 저장하는 기능을 갖고 있지 않음! 따라서 추가 필요
# python이 실행될 때 DJANGO_SETTINGS_MODULE 환경 변수에
# 현재 프로젝트의 settings.py파일 경로를 등록
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cardpr.settings")

# 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듬
import django
django.setup()

import pandas as pd
from member.models import Member

def add_data():
	card_data = pd.read_csv('C:/min/13weeks_MiniProject(2)/minipr2/carddata.csv')
	for i in range(len(card_data)):
		Member(gender=card_data['gender'][i], car=card_data['car'][i],
    		reality=card_data['reality'][i], child_num=card_data['child_num'][i], 
    		income_total=card_data['income_total'][i]*0.1, income_type=card_data['income_type'][i],
    		edu_type=card_data['edu_type'][i], family_type=card_data['family_type'][i],
    		house_type=card_data['house_type'][i], FLAG_MOBIL=card_data['FLAG_MOBIL'][i],
    		work_phone=card_data['work_phone'][i], phone=card_data['phone'][i],
    		email=card_data['email'][i], occyp_type=card_data['occyp_type'][i],
    		family_size=card_data['family_size'][i], credit=card_data['credit'][i],
    		Decile=card_data['Decile'][i]
    		).save()
	return "success"

if __name__=='__main__':
	add_data()