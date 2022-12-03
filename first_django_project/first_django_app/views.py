from django.shortcuts import render

# Create your views here.
# HTTPResponseというクラスをインポート
from django.http import HttpResponse

# View関数を任意に定義
def index(request):
    # 変数設定
    params = {"message_me": "Hello World"}
    # 出力
    return render(request,'App_Folder_HTML/index.html',context=params)