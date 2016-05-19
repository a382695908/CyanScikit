#coding:utf8
from csMarket.models import  Message

def tongji(request):
    try:
        name = request.session["username"]
        moneyin=moneyout=0
        mxuok=mfwok=0
        mxu=mfw=0
        mxuing=mfwing=0
        selfm=[]
        #收入
        try:
            mto_list = Message.objects.filter(m_tuo=name,m_cate_xuorfu="需求",m_result="是") | Message.objects.filter(m_from=name,m_cate_xuorfu="服务",m_result="是")
            for mto in mto_list:
                moneyin = moneyin + mto.m_price
        except:
            moneyin = moneyin
        #支出
        try:
            mfrom_list = Message.objects.filter(m_from=name,m_cate_xuorfu="需求",m_result="是")
            for mfrom in mfrom_list:
                moneyout = moneyout+mfrom.m_price
        except:
            moneyout = moneyout
        #需求交易个数
        try:
            mxuok_list1 = Message.objects.filter(m_from=name,m_cate_xuorfu="需求",m_result="是")
            mxuok = len(mxuok_list1)
        except:
            mxuok=mxuok
        try:
             mxuok_list2 = Message.objects.filter(m_to=name,m_cate_xuorfu="需求",m_result="是")
             mxuok = mxuok + len(mxuok_list2)
        except:
            mxuok = mxuok
        #服务交易个数
        try:
            mfw_list1 = Message.objects.filter(m_from=name,m_cate_xuorfu="服务",m_result="是")
            mfwok=mfwok +  len(mfw_list1)
        except:
            mfwok = mfwok
        try:
             mfw_list2 = Message.objects.filter(m_to=name,m_cate_xuorfu="服务",m_result="是")
             mfwok=mfwok +  len(mfw_list2)
        except:
            mfwok = mfwok
        #需求发布个数
        try:
            mxu_list = Message.objects.filter(m_from=name,m_cate_xuorfu="需求")
            mxu = len(mxu_list)
        except:
            mxu =  mxu
        #服务发布个数
        try:
            mfw_list = Message.objects.filter(m_from=name,m_cate_xuorfu="服务")
            mfw = len(mfw_list)
        except:
            mfw =  mfw
        #进行中的需求个数
        try:
            mxuing_list1 = Message.objects.filter(m_from=name,m_cate_xuorfu="需求",m_tuoing="是",m_result="否")
            mxuing =mxuing + len(mxuing_list1)
        except:
            mxuing = mxuing

        try:
            mxuing_list2 = Message.objects.filter(m_to=name,m_cate_xuorfu="需求",m_tuoing="是",m_result="否")
            mxuing = mxuing + len(mxuing_list2)
        except:
            mxuing = mxuing

        #进行中的服务个数
        try:
            mfwing_list1 = Message.objects.filter(m_from=name,m_cate_xuorfu="服务",m_tuoing="是",m_result="否")
            mfwing =mfwing +  len(mfwing_list1)
        except:
            mfwing = mfwing
        try:
             mfwing_list2 = Message.objects.filter(m_to=name,m_cate_xuorfu="服务",m_tuoing="是",m_result="否")
             mfwing =mfwing +  len(mfwing_list2)
        except:
            mfwing = mfwing
        return moneyin,moneyout,mxuok,mfwok,mxu,mfw,mxuing,mfwing
    except:
       return 0,0,0,0,0,0,0,0