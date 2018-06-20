#encoding=utf-8
from __future__ import division

import sys
import os
import datetime
import time
import math
import ujson
import uuid
import urllib
import random
import traceback
from django.db import transaction
from urlparse import urlparse, parse_qsl

import requests
from django.contrib import auth
from django.template import RequestContext
from django.core.cache import cache
from django_redis import get_redis_connection
from django.core.servers.basehttp import FileWrapper
from django.http import StreamingHttpResponse
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Count, Max, F, Q,Min,Sum
from django.contrib.auth.decorators import login_required

from andy_manager import settings
import websys.webconfig as webconfig
from websys.models import (
UserInfo,BannerInfo,TableInfo,GameInfo,Feedback,GameRecord,RoomInfo,WithholdInfo,UserExpand,
)

import  websys.fun as fun
import  websys.ReturnCode as errcode

from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                    #玩家登陆
                    url(r'^platform_login', 'websys.view.mjhall.user_platformlogin', name='user_platformlogin'),
                       url(r'^account_login', 'websys.view.mjhall.user_accountlogin', name='user_accountlogin'),
                       url(r'^account_reg', 'websys.view.mjhall.user_accountregister', name='user_accountregister'),
                       url(r'^userinfo', 'websys.view.mjhall.user_getinfo', name='user_getinfo'),
                       url(r'^useradd', 'websys.view.mjhall.user_addmore', name='user_addmore'),
                       #开房间,加入房间，作实（撤销）房间
                    url(r'^createroom', 'websys.view.mjhall.user_createroom', name='createroom'),
                       url(r'^costfront', 'websys.view.mjhall.user_joinroom', name='joinroom'),
                       url(r'^costoprate', 'websys.view.mjhall.user_operateroom', name='operateroom'),
                       url(r'^roomover', 'websys.view.mjhall.user_roomover', name='roomover'),
                       url(r'^findroom', 'websys.view.mjhall.user_findroom', name='findroom'),
                       url(r'^roomMSG', 'websys.view.mjhall.user_roomMSG', name='roomMSG'),
                       url(r'^roominfo', 'websys.view.mjhall.user_getroominfo', name='roominfo'),
                       #当局结算
                    url(r'^gamesettle', 'websys.view.mjhall.user_gamesettle', name='gamesettle'),
                       #banner列表
                    url(r'^banner', 'websys.view.mjhall.hall_bannerlist', name='banner'),
                       #记录相关
                    url(r'^totalrecord', 'websys.view.mjhall.user_totalrecord', name='user_totalrecord'),
                    url(r'^gamerecord', 'websys.view.mjhall.user_gamerecord', name='user_gamerecord'),
                    url(r'^recorddetail', 'websys.view.mjhall.user_recorddetail', name='user_recorddetail'),
                       #反馈
                    url(r'^feedback', 'websys.view.mjhall.user_feedback', name='feedback'),
    )

#获取banner,
#http://127.0.0.1:8080/api/hall/bannerlist?a=10
@csrf_exempt
def hall_bannerlist(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)
    #print(request)

    t_uid=None
    t_path="http://"+request.META['HTTP_HOST']#+"/"+_url
    db_arr=BannerInfo.objects.all()#.values("")
    t_data=[]
    #返回值

    for ii in db_arr:
        print(ii.url,'---***----',ii.img.url)
        t_data+=[{"url":ii.url,"img": t_path+ii.img.url}]
    t_res={'code':0,'data':t_data}

    response = HttpResponse(ujson.dumps(t_res))
    return  response

#用户结算
#http://127.0.0.1:8080/api/hall/gamesettle?gameid=1&roomid=23104514&roundid=1&data=[[1,100],[2,-10]]&ts=1234567&recordid=123
# gameid u'游戏编号'
# roomid u'房间号'
# roundid u'局号'
#data [[玩家1帐号，分数],[....]]
#ts u'时间截'
@csrf_exempt
def user_gamesettle(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_bid=None
    t_res={'code':-1,'msg':''}
    if request.method == 'GET':
        need_keys=['roundid','gameid','roomid','data','ts','recordid']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_res['msg']="error parms"
            return HttpResponse(ujson.dumps(t_res))
        t_bid = t_obj['roundid']
        t_gid=t_obj['gameid']
        t_rid=t_obj['roomid']
        t_data=ujson.loads(t_obj['data'])
        t_time=float(t_obj['ts'])
        t_recordid=t_obj['recordid']
    elif request.method == 'POST':
        t_bid = request.POST.get('roundid',None)

    if not t_bid:
        t_res['msg']="empty roundid"
        return HttpResponse(ujson.dumps(t_res))

    #判断是否存在
    if(GameRecord.objects.filter(roomid=t_rid,roundid=t_bid,recordid=t_recordid).exists()):
        t_res['msg']="exists roundid"
        return HttpResponse(ujson.dumps(t_res))
    else:#新增
        #game_obj=GameInfo.objects.get(pk=t_gid)
        try:
            t_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t_time))
            with transaction.commit_on_success():
                for ii in t_data:
                    cur_pkid=ii[0]
                    cur_score=ii[1]
                    gr=GameRecord()
                    gr.gameid_id=t_gid
                    u_obj=UserInfo.objects.get(pk=cur_pkid)
                    gr.uid=u_obj
                    gr.nickname=u_obj.nickname
                    gr.roomid=t_rid
                    gr.roundid=t_bid
                    gr.score=cur_score
                    gr.start_time=t_time
                    gr.recordid=t_recordid
                    gr.save()
                    #游戏汇总表
                    if UserExpand.objects.filter(uid_id=cur_pkid,gameid_id=t_gid).exists():
                        ue=UserExpand.objects.get(uid_id=cur_pkid,gameid_id=t_gid)
                        ue.allscore+=cur_score
                        #ue.allround+=1
                        if cur_score>0:
                            ue.winround+=1
                        elif cur_score==0:
                            ue.zeroround+=1
                        else:
                            ue.loseround+=1
                    else:
                        ue=UserExpand()
                        ue.uid_id=cur_pkid
                        ue.gameid_id=t_gid
                        #ue.allround=1
                        ue.allscore=cur_score
                        if cur_score>0:
                            ue.winround=1
                        elif cur_score==0:
                            ue.zeroround=1
                        else:
                            ue.loseround=1
                    ue.save()

                #更新游戏的状态，开始时间
                if int(t_bid)==1:
                    TableInfo.objects.filter(gameid_id=t_gid,roomid=t_rid).update(game_status=4,round=1,game_time=t_time)
                else:
                    TableInfo.objects.filter(gameid_id=t_gid,roomid=t_rid).update(round=t_bid)
            #返回值
            t_res["code"]=0
        except:
            fun.add_log(traceback.format_exc(),'error')
            t_data['cdoe']=errcode.DB_Error

        response = HttpResponse(ujson.dumps(t_res))
        return  response

#****************************************房间相关***********************************************
#房间消息
#http://127.0.0.1:8080/api/hall/roomMSG?uid=1
# uid u'用户帐号'
@csrf_exempt
def user_roomMSG(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':{}}
    if request.method == 'GET':
        if 'uid' not in t_obj:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_uid = t_obj['uid']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not t_uid:
        t_data['msg']="empty http uid"
        return HttpResponse(ujson.dumps(t_data))

    #判断用户是否存在
    if(UserInfo.objects.filter(pk=t_uid).exists()):
        #u_info=UserInfo.objects.get(pk=t_uid)
        #获取全部的桌
        date_from=fun.GetTime_ByNow()
        date_to=datetime.datetime.now()
        tbs=TableInfo.objects.filter(uid_id=t_uid,create_time__range=(date_from,date_to)).values("roomid","time","point","status","isbanker","create_time")

        t_data['data']=tbs
        t_data['code']=0
        return HttpResponse(ujson.dumps(t_data))
    else:#新增
        t_data['msg']="empty uid"
        return HttpResponse(ujson.dumps(t_data))

#发现房间
#http://127.0.0.1:8080/api/hall/findroom?uid=1
# uid u'用户帐号'
@csrf_exempt
def user_findroom(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':{}}
    if request.method == 'GET':
        if 'uid' not in t_obj:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_uid = t_obj['uid']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not t_uid:
        t_data['msg']="empty http uid"
        return HttpResponse(ujson.dumps(t_data))

    #判断用户是否存在
    if(UserInfo.objects.filter(pk=t_uid).exists()):
        #u_info=UserInfo.objects.get(pk=t_uid)
        #获取全部的桌
        date_to=datetime.datetime.now()
        date_from=fun.GetTime_ByNow()
        tbs=TableInfo.objects.filter(game_status__in=[0,4],create_time__range=(date_from,date_to))
        t_create=[]
        t_join=[]
        for ii in tbs:
            cur_obj={'gameId':ii.gameid_id,'roomId':ii.roomid,'startTs':-1,'time':ii.time}
            #是否开始了
            cur_obj['startTs']=ii.game_time or -1
            if ii.uid_id==int(t_uid):
                cur_obj['createTs']=ii.create_time
                t_create.append(cur_obj)
            elif WithholdInfo.objects.filter(uid_id=t_uid,tableid_id=ii.id).exists():
                t_join.append(cur_obj)
        t_data['data']['create']=t_create
        t_data['data']['join']=t_join
        t_data['code']=0

        fun.add_log(t_data)

        return HttpResponse(ujson.dumps(t_data))
    else:#新增
        t_data['msg']="empty uid"
        return HttpResponse(ujson.dumps(t_data))


#用户开房间
#http://127.0.0.1:8080/api/hall/createroom?uid=1&gameid=1&num=10&playtype=1
# uid u'用户帐号'
# gameid u'游戏编号'
# num u'时间'
# playtype u'类型'
@csrf_exempt
def user_createroom(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':[],'params':[]}
    if request.method == 'GET':
        need_keys=['uid','gameid','playtype','num']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_uid = t_obj['uid']
        t_gid=t_obj['gameid']
        t_type=t_obj['playtype']
        t_num=t_obj['num']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not t_uid:
        t_data['msg']="empty http uid"
        t_data['code']=errcode.UserNotExists
        return HttpResponse(ujson.dumps(t_data))

    #获取唯一的房间号,测试是时间截
    t_roomid=0
    t1=str(time.time()).replace('.','')
    t_roomid=int(t1[-6:])

    #,数据库获取唯一的
    t_roomid=fun.GetRandom()
    is_in=True
    while is_in:
        cur_num=TableInfo.objects.filter(game_status__in=[0,4],gameid_id=t_gid,roomid=t_roomid).count()
        if(cur_num==0):
            is_in=False
        else:
            t_roomid=fun.GetRandom()

    try:
        #根据时长获取对应的点数
        t_needpoint=int(t_num)
        t_r_info=RoomInfo.objects.filter(parid_id=t_gid,roomid=t_num).values("consumerpoint")
        #print t_gid,'--t_num--',t_num,t_r_info
        if len(t_r_info)>0:
            t_needpoint=t_r_info[0]["consumerpoint"]

        #判断是否存在
        if(UserInfo.objects.filter(pk=t_uid).exists()):
            u_info=UserInfo.objects.get(pk=t_uid)
            t_point=u_info.gamepoint
            if t_point<t_needpoint:
                t_data['msg']="point not enough"
                t_data['code']=errcode.DiamondNotEnough
                return HttpResponse(ujson.dumps(t_data))
        else:#新增
            t_data['msg']="empty uid"
            t_data['code']=errcode.UserNotExists
            return HttpResponse(ujson.dumps(t_data))

        #过滤超时的房间
        date_min=datetime.datetime.now()+datetime.timedelta(0,-webconfig.TIMEOUT_ROOM_HOUR*60*60)
        TableInfo.objects.filter(game_status__in=[0,4],create_time__lte=date_min,gameid_id=t_gid).update(game_status=3)
        #获取玩家的当前房间列表
        cur_num=TableInfo.objects.filter(game_status__in=[0,4],uid_id=t_uid,gameid_id=t_gid).count()
        if(cur_num>=webconfig.MAX_CREAT_ROOM):
            t_data['code']=errcode.RoomNumberOverFlow
            t_data['msg']="max create room :"+str(cur_num)
            t_data['params']=[cur_num,webconfig.MAX_CREAT_ROOM]
            return HttpResponse(ujson.dumps(t_data))

        recordid=str(uuid.uuid1())

        with transaction.commit_on_success():
            u_info.gamepoint-=t_needpoint
            u_info.save()

            #插入扣卡表
            tb=TableInfo()
            tb.gameid=GameInfo.objects.get(pk=t_gid)
            tb.uid=u_info
            tb.time=t_num
            tb.point=t_needpoint
            tb.roomid=t_roomid
            tb.isbanker=1
            tb.playtype=t_type
            tb.recordid=recordid
            tb.save()

            #预扣表
            whi=WithholdInfo()
            whi.tableid_id=tb.id
            whi.uid_id=t_uid
            whi.save()
            t_data={'code':0,'msg':'','data':{"roomId":t_roomid,"pkid":tb.id}}
    except Exception, e:
        #fun.add_log(e,'error')
        fun.add_log(traceback.format_exc(),'error')
        t_data['cdoe']=errcode.DB_Error

    fun.add_log(t_data)
    #返回值
    response = HttpResponse(ujson.dumps(t_data))
    return  response

#用户加入房间（预扣)
#http://127.0.0.1:8080/api/hall/costfront?uid=1&gameid=1&roomid=123456
# uid u'用户帐号'
# gameid u'游戏编号'
# roomid u'房间号'
@csrf_exempt
def user_joinroom(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':[]}
    if request.method == 'GET':
        need_keys=['uid','gameid','roomid']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_uid = t_obj['uid']
        t_gid=t_obj['gameid']
        t_rid=t_obj['roomid']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not t_uid or not t_rid:
        t_data['msg']="empty http uid"
        return HttpResponse(ujson.dumps(t_data))

    #获取房间对象
    rm_arr=TableInfo.objects.filter(roomid=t_rid,isbanker=1,gameid_id=t_gid)
    if len(rm_arr)==0:
        t_data['msg']="empty roomid"
        return HttpResponse(ujson.dumps(t_data))

    t_needpoint=rm_arr[0].point
    t_pkid=rm_arr[0].pk

    #判断uid是否存在
    if(UserInfo.objects.filter(pk=t_uid).exists()):
        u_info=UserInfo.objects.get(pk=t_uid)
        t_point=u_info.gamepoint
        if t_point<t_needpoint:
            t_data['msg']="point not enough"
            return HttpResponse(ujson.dumps(t_data))
    else:#新增
        t_data['msg']="empty uid"
        return HttpResponse(ujson.dumps(t_data))

    #判断是否已预扣
    if(WithholdInfo.objects.filter(tableid_id=t_pkid,uid_id=t_uid).exists()):
        t_data['msg']="cost exists"
        t_data['code']=1
        return HttpResponse(ujson.dumps(t_data))

        #扣钱钱
    u_info.gamepoint-=t_needpoint
    u_info.save()

    #插入扣卡表
    # tb=TableInfo()
    # tb.gameid=GameInfo.objects.get(pk=t_gid)
    # tb.uid=u_info
    # tb.time=t_needpoint
    # tb.point=t_needpoint
    # tb.roomid=t_rid
    # tb.isbanker=0
    # tb.save()
    #预扣表
    whi=WithholdInfo()
    whi.tableid_id=t_pkid
    whi.uid_id=t_uid
    whi.save()

    #返回值
    t_data={'code':0,'msg':'','data':{"diamond":u_info.gamepoint,"roomId":t_rid,"gameId":t_gid,"pkid":whi.id}}

    response = HttpResponse(ujson.dumps(t_data))
    return  response


#获取房间配置
#http://127.0.0.1:8080/api/hall/roominfo?uid=1&gameid=1&roomid=123456
# uid u'用户帐号'
# gameid u'游戏编号'
# roomid u'房间号'
@csrf_exempt
def user_getroominfo(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':[]}
    if request.method == 'GET':
        need_keys=['uid','gameid','roomid']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_uid = t_obj['uid']
        t_gid=t_obj['gameid']
        t_rid=t_obj['roomid']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not t_uid or not t_rid:
        t_data['msg']="empty http uid"
        return HttpResponse(ujson.dumps(t_data))

    #获取房间对象
    rm_arr=TableInfo.objects.filter(roomid=t_rid,isbanker=1,gameid_id=t_gid)
    if len(rm_arr)==0:
        t_data['msg']="empty roomid"
        return HttpResponse(ujson.dumps(t_data))

    cur_rm=rm_arr[0]

    #判断uid是否存在
    if(UserInfo.objects.filter(pk=t_uid).exists()):
        #判断玩家活动的还有X个

        t_data['code']=0
        t_start=-1
        if cur_rm.game_time:
            t_start = time.mktime(cur_rm.game_time.timetuple())
        t_data['data']={'time':cur_rm.time,'createid':cur_rm.uid_id,'createname':cur_rm.uid.nickname,'round':cur_rm.round,'recordid':cur_rm.recordid,
                       'createtime':time.mktime(cur_rm.create_time.timetuple()), 'starttime':t_start,"gamestatus":cur_rm.game_status,"playtype":cur_rm.playtype}
        fun.add_log(t_data)
        return HttpResponse(ujson.dumps(t_data))
    else:#新增
        t_data['msg']="empty uid"
        return HttpResponse(ujson.dumps(t_data))


#用户操作房间（作实，撤销)
#http://127.0.0.1:8080/api/hall/operateroom?uid=1&gameid=1&roomid=123456&status=1
# uid u'用户帐号'
# gameid u'游戏编号'
# roomid u'房间号'
#status u'状态' -1撤销，1作实
@csrf_exempt
def user_operateroom(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':[]}
    if request.method == 'GET':
        need_keys=['uid','gameid','roomid']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_uid = t_obj['uid']
        t_gid=t_obj['gameid']
        t_rid=t_obj['roomid']
        #t_pkid=t_obj['pkid']
        t_status=int(t_obj['status'])
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not t_uid or not t_rid or (t_status not in [-1,1]):
        t_data['msg']="error http data"
        return HttpResponse(ujson.dumps(t_data))

    #判断是否存在
    if(UserInfo.objects.filter(pk=t_uid).exists()):
        u_info=UserInfo.objects.get(pk=t_uid)
        #获取房间对象
        rm_arr=TableInfo.objects.filter(roomid=t_rid,uid=u_info,status=0)
        if len(rm_arr)==0:
            t_data['msg']="empty roomid"
            return HttpResponse(ujson.dumps(t_data))
    else:#新增
        t_data['msg']="empty uid"
        return HttpResponse(ujson.dumps(t_data))

    tmp_tbinfo=rm_arr[0]
    #修改扣卡表
    tmp_tbinfo.status=t_status
    if(t_status==-1):#返回玩家的钱
        u_info.gamepoint+=tmp_tbinfo.point
        u_info.save()
    tmp_tbinfo.save()

    #返回值
    t_data={'code':0,'msg':'','data':{"diamond":u_info.gamepoint,"roomId":t_rid,"gameId":t_gid}}

    response = HttpResponse(ujson.dumps(t_data))
    return  response

#房间结束，作实有gamerecord的用户，撤销没有gamerecord的用户
#http://127.0.0.1:8080/api/hall/roomover?gameid=1&roomid=123456&status=2
# gameid u'游戏编号'
# roomid u'房间号'
# status u'解散的类型’
@csrf_exempt
def user_roomover(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':[]}
    if request.method == 'GET':
        need_keys=['gameid','roomid','status']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_gid=int(t_obj['gameid'])
        t_rid=int(t_obj['roomid'])
        t_st=int(t_obj['status'])
    elif request.method == 'POST':
        t_gid = request.POST.get('gameid',None)

    # if not (GameInfo.objects.filter(pk=t_gid).exists()):
    #     t_data['msg']="error gameid"
    #     return HttpResponse(ujson.dumps(t_data))

    #g_obj=GameInfo.objects.get(pk=t_gid)
    #判断是否存在
    try:

        if (TableInfo.objects.filter(roomid=t_rid,isbanker=1,gameid_id=t_gid).exists()):
            tb_info=TableInfo.objects.get(roomid=t_rid,isbanker=1,gameid_id=t_gid)
            #预扣的人
            tbs_arr=WithholdInfo.objects.filter(tableid_id=tb_info.id)
            #gamerecord有记录的人
            gr_arr=GameRecord.objects.filter(roomid=t_rid,gameid_id=t_gid).values("uid")
            # [{'uid': 1L}, {'uid': 2L}, {'uid': 3L}, {'uid': 4L}, {'uid': 1L}, {'uid': 2L}, {'uid': 3L}, {'uid': 4L}]
            ii=0#打的作实,写消息
            jj_arr=[]
            #print(len(tbs_arr),'---tbs_arr---',len(gr_arr),gr_arr)
            with transaction.commit_on_success():
                for ii_obj in tbs_arr:
                    print (ii_obj.uid,'---ii_obj.uid')
                    is_in=False
                    for kk_obj in gr_arr:
                        if ii_obj.uid.pk ==kk_obj['uid']:
                            ii_tb=tbs_arr[ii]
                            ii_tb.status=1
                            ii_tb.save()
                            is_in=True
                            break
                    if not is_in:
                        jj_arr.append(ii)
                    ii+=1
                #没打的撤销，返回金币,写消息
                print (jj_arr,'---jj_arr---',t_st)
                for jj in jj_arr:
                    ii_tb=tbs_arr[jj]
                    ii_tb.status=-1
                    ii_tb.save()
                    #返回金币
                    uu_obj=ii_tb.uid
                    uu_obj.gamepoint+=tb_info.point
                    uu_obj.save()
                t_data['code']=0

                t_data['recordid']=-1
                if len(gr_arr)>0:#有记录返回编号，方便查询详情
                    t_data['recordid']=tb_info.recordid
                #更新房间的状态
                #TableInfo.objects.filter(roomid=t_rid,gameid_id=t_gid).update(game_status=t_st,status=1)
                tb_info.game_status=t_st
                tb_info.status=1
                tb_info.save()
            #print '--*****---',tbs_arr.game_status
        else:#新增
            t_data['msg']="empty data"
            t_data['cdoe']=errcode.DB_DataNotExists
            return HttpResponse(ujson.dumps(t_data))
    except Exception, e:
        t_data['cdoe']=errcode.DB_Error
        fun.add_log(traceback.format_exc(),'error')

    fun.add_log(t_data)
    response = HttpResponse(ujson.dumps(t_data))
    return  response

#************************************用户相关操作**************************************************
#登陆验证用户(平台)
#http://127.0.0.1:8080/api/hall/platformlogin?openid=d8f33838264a11e7994f5254000d335c&nickname=qq123&pf=wx&head_img=https://www.baidu.com/img/bd_logo1.png&gender=m&phone=13800138000&ip=127.0.0.1
# openid u'用户帐号'
# nickname u'呢'
# pf u'平台'
# head_img u'头像'
# gender u'性别'
# phone u'手机号'
#ip u'玩家IP'
# "code": 0,
#     "data": {
#         "id": 1,
#         "name": "Terry",
#         "avatar": "imgs/usertext.jpg",
#         "diamond": 1234
#     }
@csrf_exempt
def user_platformlogin(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':{}}
    if request.method == 'GET':
        need_keys=['openid','nickname','pt','head_img','gender','ip','phone','agent_id']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))

        t_uid = t_obj['openid']
        t_name=t_obj['nickname']
        t_pf=t_obj['pt']
        t_img=t_obj['head_img']
        t_gender = t_obj["gender"]
        t_ip = t_obj["ip"]
        t_phone=t_obj["phone"]
        t_agent=t_obj["agent_id"]
    elif request.method == 'POST':
        t_uid = request.POST.get('openid',None)

    if not t_uid:
        t_data['msg']="empty openid"
        response = HttpResponse(ujson.dumps(t_data))
        return response
    #判断是否存在
    t_point=random.randint(10,100)*1000
    if(UserInfo.objects.filter(uid=t_uid).exists()):
        u_info=UserInfo.objects.get(uid=t_uid)
        t_point=u_info.gamepoint
    else:#新增
        u_info = UserInfo()
        u_info.uid = t_uid
        u_info.pf=t_pf
        u_info.create_ip = t_ip
        u_info.gamepoint=t_point
        if(int(t_agent)>-1):
            u_info.agentid_id=t_agent

    u_info.gender=t_gender
    u_info.nickname=t_name
    u_info.head_img=t_img or 'websys/static/images/user.png'
    u_info.phone=t_phone

    #t_time = time.localtime(int(t_data['created']))
    u_info.login_ip=t_ip
    u_info.login_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#time.strftime('%Y-%m-%d %H:%M:%S',t_time)
    u_info.save()

    #返回值
    t_res={"id": u_info.id,"name": u_info.nickname,"avatar":  fun.GetImgURL(request,u_info.head_img),"diamond": t_point}
    # for ikey in u_info._meta.get_all_field_names():
    #     #print(ikey,'---***----',)
    #     t_res[ikey]=getattr(u_info,ikey)
    # t_res["openid"]=t_uid

    t_data['code']=0
    t_data['data']=t_res
    response = HttpResponse(ujson.dumps(t_data))
    return  response

#http://127.0.0.1:8080/api/hall/account_login?user=qq123&pwd=123&pt=wx&agentid=-1&ip=127.0.0.1
# user u'用户帐号'
# pwd u'密码'
# pt u'平台'
# agentid u'代理id',没有-1
#ip u'玩家IP'
# "code": 0,
#     "data": {
#         "id": 1
#     }
def user_accountlogin(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':{}}
    if request.method == 'GET':
        need_keys=['user','pwd','pt','ip','agentid']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))

        t_uid = t_obj['user']
        t_pwd=t_obj['pwd']
        t_pf=t_obj['pt']
        t_ip = t_obj["ip"]
        t_agent=t_obj["agentid"]
    elif request.method == 'POST':
        t_uid = request.POST.get('user',None)

    t_gender='m'
    t_name=t_uid

    t_phone='10086'

    if not t_uid:
        t_data['msg']="empty user"
        return HttpResponse(ujson.dumps(t_data))
    #判断是否存在
    t_point=random.randint(10,100)*100
    if(UserInfo.objects.filter(uid=t_uid,password=t_pwd).exists()):
        u_info=UserInfo.objects.get(uid=t_uid)
        t_point=u_info.gamepoint
    else:#新增
        t_data['msg']="user not exists"
        return HttpResponse(ujson.dumps(t_data))

        u_info = UserInfo()
        u_info.uid = t_uid
        u_info.password=t_pwd
        u_info.pf=t_pf
        u_info.create_ip = t_ip
        u_info.gamepoint=t_point
        if(int(t_agent)>-1):
            u_info.agentid_id=t_agent

    #u_info.gender=t_gender
    #u_info.nickname=t_name
    #u_info.head_img=t_img
    #u_info.phone=t_phone

    #t_time = time.localtime(int(t_data['created']))
    u_info.login_ip=t_ip
    u_info.login_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#time.strftime('%Y-%m-%d %H:%M:%S',t_time)
    u_info.save()

    #返回值
    t_res={"id": u_info.id,"name": u_info.nickname,"avatar":  fun.GetImgURL(request,u_info.head_img),"diamond": t_point}
    # for ikey in u_info._meta.get_all_field_names():
    #     #print(ikey,'---***----',)
    #     t_res[ikey]=getattr(u_info,ikey)
    # t_res["openid"]=t_uid

    t_data['code']=0
    t_data['data']=t_res
    response = HttpResponse(ujson.dumps(t_data))
    return  response

#http://127.0.0.1:8080/api/hall/account_register?user=qq123&pwd=123&pt=wx&agentid=-1&phone=10086&msgcode=123&friendid=facebook&ip=127.0.0.1
# user u'用户帐号'
# pwd u'密码'
# pt u'平台'
# agentid u'代理id',没有-1
# phone 手机
# msgcode 短信验证码
# friendid 好友id,没有-1
# ip u'玩家IP'
# "code": 0,
#     "data": {
#         "id": 1
#     }
def user_accountregister(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':1,'msg':'','data':{}}
    if request.method == 'GET':
        need_keys=['user','pwd','pt','ip','agentid',"phone","msgcode","friendid"]
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))

        t_uid = t_obj['user']
        t_pwd=t_obj['pwd']
        t_pf=t_obj['pt']
        t_ip = t_obj["ip"]
        t_agent=t_obj["agentid"]
        t_phone=t_obj["phone"]
        t_msgcode=t_obj["msgcode"]
        t_friendid=int(t_obj["friendid"])
    elif request.method == 'POST':
        t_uid = request.POST.get('user')

    t_gender='m'
    t_name=t_uid
    t_img='websys/static/images/user.png'

    if not t_uid:
        t_data['msg']="empty user"
        return HttpResponse(ujson.dumps(t_data))
    #判断是否存在
    t_point=random.randint(10,100)*100
    if(UserInfo.objects.filter(uid=t_uid).exists()):
        t_data['msg']="user exists"
        t_data['code']=2
        return HttpResponse(ujson.dumps(t_data))

        u_info=UserInfo.objects.get(uid=t_uid)
        t_point=u_info.gamepoint
    else:#新增
        u_info = UserInfo()
        u_info.uid = t_uid
        u_info.password=t_pwd
        u_info.pf=t_pf
        u_info.create_ip = t_ip
        u_info.gamepoint=t_point
        if(int(t_agent)>-1):
            u_info.agentid_id=t_agent

    u_info.gender=t_gender
    u_info.nickname=t_name
    u_info.head_img=t_img
    u_info.phone=t_phone
    if t_friendid>0:
        u_info.agentid_id=t_friendid

    #t_time = time.localtime(int(t_data['created']))
    u_info.login_ip=t_ip
    u_info.login_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#time.strftime('%Y-%m-%d %H:%M:%S',t_time)
    u_info.save()

    #返回值
    t_res={"id": u_info.id,"user": ''}
    # for ikey in u_info._meta.get_all_field_names():
    #     #print(ikey,'---***----',)
    #     t_res[ikey]=getattr(u_info,ikey)
    # t_res["openid"]=t_uid

    t_data['code']=0
    t_data['data']=t_res
    response = HttpResponse(ujson.dumps(t_data))
    return  response

#批量添加 用户
#http://127.0.0.1:8080/api/hall/useradd?user=ai&num=10
def user_addmore(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':1,'msg':'','data':{}}
    if request.method == 'GET':
        need_keys=['user','num']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))

        t_uid = t_obj['user']
        t_num = int(t_obj['num'])
    elif request.method == 'POST':
        t_uid = request.POST.get('user',None)

    u_list_to_insert = list()
    for x in range(t_num):
        cur_id=t_uid+str(x)
        t_point=random.randint(10,100)*100*(x+1)
        u_list_to_insert.append(UserInfo(uid=cur_id,nickname=u'测试'+cur_id,password=cur_id,create_ip='127.0.0.1',phone=str(t_point),gamepoint=t_point,
                                         pf='test',head_img='http://andytest.nvzhanshen.com/pt/static/egret/150314184020_wqdzpy.png'))
    UserInfo.objects.bulk_create(u_list_to_insert)

    t_data['code']=0
    return HttpResponse(ujson.dumps(t_data))


#获取用户信息
#http://127.0.0.1:8080/api/hall/userinfo?uid=1
# uid u'用户帐号'
# "code": 0,
#     "data": {
#         "id": 1,
#         "name": "Terry",
#         "avatar": "imgs/usertext.jpg",
#         "diamond": 1234
#     }
@csrf_exempt
def user_getinfo(request):
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)

    t_uid=None
    t_data={'code':-1,'msg':'','data':{}}
    if request.method == 'GET':
        if 'uid' not in t_obj:
            t_data['msg']="error parms"
            return HttpResponse(ujson.dumps(t_data))
        t_uid = t_obj['uid']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not t_uid:
        t_data['msg']="empty openid"
        return  HttpResponse(ujson.dumps(t_data))

    #判断是否存在
    if(UserInfo.objects.filter(pk=t_uid).exists()):
        u_info=UserInfo.objects.get(pk=t_uid)

    else:#新增
        t_data['msg']="uid not exists "
        return  HttpResponse(ujson.dumps(t_data))

    #返回值
    t_res={"id": u_info.id,"name": u_info.nickname,"avatar": fun.GetImgURL(request,u_info.head_img),"diamond": u_info.gamepoint,'status':u_info.status}

    t_data['code']=0
    t_data['data']=t_res
    return HttpResponse(ujson.dumps(t_data))


#********************************记录相关操作********************************************
#http://127.0.0.1:8080/api/hall/totalrecord?uid=4
#总记录
#uid帐号
@csrf_exempt
def user_totalrecord(request):
    t_res={'code':-1,'msg':''}
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)
    if request.method == 'GET':
        if 'uid' not in t_obj:
            t_res['msg']="error parms"
            return HttpResponse(ujson.dumps(t_res))
        t_uid = t_obj['uid']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not UserInfo.objects.filter(pk=t_uid).exists():
        t_res['msg']='error uid'
        return HttpResponse(ujson.dumps(t_res))
#按游戏汇总
    t_data=[]
    gb_info=GameInfo.objects.all()
    #u_info=UserInfo.objects.get(pk=t_uid)
    t_round=0
    t_win=0
    #7天内的
    date_to=datetime.datetime.now()
    date_from=fun.GetTime_ByNow(-webconfig.GAME_RECORD_DAY)
    for ii in gb_info:
        t_num=GameRecord.objects.filter(uid_id=t_uid,gameid=ii,start_time__range=(date_from,date_to)).count()
        t_win=GameRecord.objects.filter(uid_id=t_uid,gameid=ii,start_time__range=(date_from,date_to),score__gt=0).count()
        t_data.append({"id":ii.pk,"round":t_num,"win":t_win})

    t_res['code']=0
    t_res['data']=t_data
    return HttpResponse(ujson.dumps(t_res))

#http://127.0.0.1:8080/api/hall/gamerecord?uid=4&gameid=1
#记录列表
#uid帐号，gameid游戏
@csrf_exempt
def user_gamerecord(request):
    t_res={'code':-1,'msg':''}
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)
    if request.method == 'GET':
        need_keys=['uid','gameid']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_res['msg']="error parms"
            return HttpResponse(ujson.dumps(t_res))

        t_uid = t_obj['uid']
        t_gid=int(t_obj['gameid'])
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not UserInfo.objects.filter(pk=t_uid).exists():
        t_res['msg']='error uid'
        return HttpResponse(ujson.dumps(t_res))
    #按房间汇总
    t_data=[]
    date_from=fun.GetTime_ByNow(-webconfig.GAME_RECORD_DAY)
    date_to=datetime.datetime.now()
    # if(t_gid==0):#全部游戏
    #     tbs_info=TableInfo.objects.filter(uid_id=t_uid,create_time__range=(date_from,date_to)).order_by("-id")
    # else:
    #     tbs_info=TableInfo.objects.filter(uid_id=t_uid,create_time__range=(date_from,date_to),gameid_id=t_gid).order_by("-id")

    #参加的
    wh_info=WithholdInfo.objects.filter(uid_id=t_uid,create_time__range=(date_from,date_to))
    t_round=0
    t_score=0
    for jj in wh_info:#每个房间
        cur_info=jj.tableid#房间对象
        if(t_gid>0) and (t_gid!=cur_info.gameid_id):#某个游戏
            continue

        cur_obj=GameRecord.objects.filter(uid_id=t_uid,gameid_id=cur_info.gameid_id,roomid=cur_info.roomid,recordid=cur_info.recordid).aggregate(score=Sum("score"),num=Count("id"))

        cur_round=cur_obj["num"]
        if cur_round>0:
            t_round+=cur_round
            t_score+=cur_obj["score"]
            t_data.append({"id":cur_info.recordid,"ts":time.mktime(cur_info.create_time.timetuple()),"time":cur_info.time,
                           "score":cur_obj["score"]})
    t_res['code']=0
    t_res['data']={"roundTotal":t_round,"scoreTotal":t_score,"list":t_data}
    return HttpResponse(ujson.dumps(t_res))

#http://127.0.0.1:8080/api/hall/recorddetail?uid=4&recordid=23791531
#记录详情
#uid帐号，recordid编号
@csrf_exempt
def user_recorddetail(request):
    t_res={'code':-1,'msg':''}
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)
    if request.method == 'GET':
        need_keys=['uid','recordid']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_res['msg']="error parms"
            return HttpResponse(ujson.dumps(t_res))
        t_uid = t_obj['uid']
        t_recordid=t_obj['recordid']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    if not UserInfo.objects.filter(pk=t_uid).exists():
        t_res['msg']='error uid'
        return HttpResponse(ujson.dumps(t_res))
#分解roomid,roundid
    #t_roomid,t_roundid=kk=t_gid.split('_')

    t_data=[]
    #获取房主
    t_creatorId=-1
    tbs=TableInfo.objects.filter(recordid=t_recordid,isbanker=1).values("uid")
    if len(tbs)<=0:
        t_res['msg']='error roomid'
        return HttpResponse(ujson.dumps(t_res))
    else:
        tb_info=TableInfo.objects.get(recordid=t_recordid,isbanker=1)
    t_creatorId=tbs[0]["uid"]

    t_ts=-1#开始时间
    t_secs=-1#时长
    u_info=UserInfo.objects.get(pk=t_uid)
    t_round=0

    gr_arr=GameRecord.objects.filter(recordid=t_recordid).values('uid_id').annotate(score=Sum('score'))
    #用户的呢称和头像
    #user_obj=UserInfo.objects.filter(pk__in =user_arr)
    for ii in gr_arr:
        user_obj=UserInfo.objects.get(pk=ii["uid_id"])
        t_data.append({"id":ii["uid_id"],"avatar": fun.GetImgURL(request,user_obj.head_img),"name":user_obj.nickname,"score":ii["score"]})

    t_res['code']=0
    t_res['data']={"roomId":tb_info.roomid,"creatorId":t_creatorId,"creatorName":u_info.nickname,"creatorAvatar":fun.GetImgURL(request,u_info.head_img),"gameId":tb_info.gameid_id,
                   "ts":time.mktime(tb_info.create_time.timetuple()),"time":tb_info.time,"status":tb_info.game_status,"players":t_data}
    return HttpResponse(ujson.dumps(t_res))

#用户反馈http://127.0.0.1:8080/api/hall/feedback?uid=1&type=1&gameid=1&name=chong&phone=10086&problem=黑游戏
#uid玩家帐号，type类型，gameid游戏id,name名称，phone手机号，problem问题
#{"msg":"","code":0}
def user_feedback(request):
    t_res={'code':0,'msg':''}
    t_obj=fun.Decode_Request_MJ(request)
    fun.add_log(t_obj)
    if request.method == 'GET':
        need_keys=['uid','type','gameid','name','phone','problem']
        if len(set(need_keys)-set(t_obj.keys()))>0:
            t_res['msg']="error parms"
            return HttpResponse(ujson.dumps(t_res))

        t_uid = t_obj['uid']
        t_type=t_obj['type']
        t_gid=t_obj['gameid']
        t_name=t_obj['name']
        t_phone=t_obj['phone']
        t_problem=t_obj['problem']
    elif request.method == 'POST':
        t_uid = request.POST.get('uid',None)

    fb=Feedback()
    if(t_uid!=''):
        fb.uid_id=int(t_uid)
    fb.gameid_id=int(t_gid)
    fb.typeid=t_type
    fb.username=t_name
    fb.phone=t_phone
    fb.problem=t_problem
    fb.save()

    t_res['code']=0

    return HttpResponse(ujson.dumps(t_res))

