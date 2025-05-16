

import random
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from artcraftapp.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
# Create your views here.

def index(request):
    data1=category.objects.all()
    data=product.objects.filter(quantity__gt=0)
    return render(request,'index.html',{'data1':data1,'data':data})
def sign_in_process(request):
    u=request.POST.get("username")
    p=request.POST.get("password")
    obj=authenticate(username=u,password=p)
    if obj is not None:
        if obj.is_superuser == 1:
            request.session['suname'] = u
            request.session['slogid'] = obj.id
            return redirect('/admin_home/')
        else:
          messages.add_message(request, messages.INFO, 'Invalid User.')
          return redirect('/index/')
    else:
        newp=p
        try:
            obj1=login.objects.get(username=u,password=newp)

            if obj1.Usertype=="Artist":
                if(obj1.status=="Approved"):
                    request.session['suname'] = u
                    request.session['slogid'] = obj1.login_id
                    return redirect('/artist/')
                elif(obj1.status=="Not Approved"):
                    messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                    return redirect('/login/')
                else:
                    messages.add_message(request, messages.INFO, 'Invaltyryid User.')
                    return redirect('/login/')
            elif  obj1.Usertype=="User":
                request.session['suname'] = u
                request.session['slogid'] = obj1.login_id
                return redirect('/Customer/')

            else:
                 messages.add_message(request, messages.INFO, 'Infghfgvalid User.')
                 return redirect('/login/')
        except login.DoesNotExist:
         messages.add_message(request, messages.INFO, 'Invalid User.')
         return redirect('/login/')
def admin_home(request):
    if 'suname' in request.session:
     return render(request,'Master/index.html')
    else:
      return redirect('/login/')
def artist(request):
    if 'suname' in request.session:
     return render(request,'Artist/index.html')
    else:
      return redirect('/login/')
#User
def customer_action(request):
    tbl1=login()
    username=request.POST.get("username")
    data = {
       'username_exists':      login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
    }
    if(data["username_exists"]==False):
        tbl1.username=request.POST.get("username")
        password=request.POST.get("password")
        tbl1.password=password
        tbl1.Usertype="User"
        tbl1.status="Approved"
        tbl1.save()
        obj=login.objects.get(username=username,password=password)

        u=user_register()
        u.login_id = obj.login_id
        u.Name=request.POST.get("Name")
        u.phone_number =request.POST.get("phone")
        u.Email=request.POST.get("Email")
        u.Address=request.POST.get("address")
        u.save()
        messages.add_message(request, messages.INFO, 'Registered successfully.')
        return redirect('/login/')
    else:
        messages.add_message(request, messages.INFO, 'User name is already Exist. Sorry Registration Failed.')
        return redirect('/customer_registration/')

def artist_action(request):
    tbl1=login()
    username=request.POST.get("username")
    data = {
       'username_exists':      login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
    }
    if(data["username_exists"]==False):
        tbl1.username=request.POST.get("username")
        password=request.POST.get("password")
        tbl1.password=password
        tbl1.Usertype="Artist"
        tbl1.status="Not Approved"
        tbl1.save()
        obj=login.objects.get(username=username,password=password)

        u=artist_register()
        u.login_id = obj.login_id
        u.Name=request.POST.get("Name")
        u.phone_number =request.POST.get("phone")
        u.Email=request.POST.get("Email")
        u.Address=request.POST.get("address")
        u.save()
        messages.add_message(request, messages.INFO, 'Registered successfully.')
        return redirect('/login/')
    else:
        messages.add_message(request, messages.INFO, 'User name is already Exist. Sorry Registration Failed.')
        return redirect('/artist_registration/')
def Customer(request):

    if 'suname' in request.session:

        data1=category.objects.all()
        data=product.objects.filter(quantity__gt=0)
        return render(request,'Customer/index.html',{'data1':data1,'data':data})
    else:
         return redirect('/index/')

def cust_product_art(request):

    if 'suname' in request.session:
        painting_name=request.POST.get("art")
        data1=category.objects.all()
        data=product.objects.filter(product__contains="%"+painting_name+"%")
        return render(request,'Customer/product.html',{'data1':data1,'data':data})
    else:
         return redirect('/index/')
def cust_product_artist(request):

    if 'suname' in request.session:
        artist=request.POST.get("artist")
        data1=category.objects.all()
        data=product.objects.filter(painter_name__contains="%"+artist+"%")
        return render(request,'Customer/product.html',{'data1':data1,'data':data})
    else:
         return redirect('/index/')

def cust_product_category(request):

    if 'suname' in request.session:
        category1=request.POST.get("category")
        data1=category.objects.all()
        data=product.objects.filter(category_id=category1)
        return render(request,'Customer/product.html',{'data1':data1,'data':data})
    else:
         return redirect('/index/')



def admin_home(request):
    if 'suname' in request.session:
     return render(request,'Master/index.html')
    else:
      return redirect('/index/')
def login_page(request):

     return render(request,'login.html')
def customer_registration(request):

     return render(request,'customer_registration.html')
def artist_registration(request):

     return render(request,'artist_registration.html')
def admin_logout(request):
    logout(request)
    return redirect('/index/')
def user_logout(request):
    logout(request)
    request.session.delete()
    return redirect('/index/')


#admin


def check_username(request):
    username = request.GET.get("username")
    data = {
       'username_exists':      login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
    }
    if(data["username_exists"]==False):
        data["success"]="Available"

    return JsonResponse(data)


#Approval

def approve_artist(request):
   if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select p.* from  tbl_artist as p  where p.login_id in (select login_id from tbl_login where Usertype='Artist' and status='Not Approved')")
        data=cursor.fetchall()
        return render(request,'Master/approve_artist.html',{'data':data})
   else:
       return redirect('/index/')
def approve(request,id):
    if 'suname' in request.session:
        tbl=login.objects.get(login_id=id)
        tbl.status="Approved"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/approve_artist/')
    else:
       return redirect('/index/')
def reject(request,id):
    if 'suname' in request.session:
        tbl=login.objects.get(login_id=id)
        tbl.status="Rejected"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Rejected successfully.')
        return redirect('/approve_artist/')
    else:
        return redirect('/login')

def artist_list(request):
   if 'suname' in request.session:
            cursor=connection.cursor()
            cursor.execute("select p.* from  tbl_artist as p  where p.login_id in (select login_id from tbl_login where Usertype='Artist' and status='Approved')")
            data=cursor.fetchall()
            return render(request,'Master/approved_artist.html',{'data':data})
   else:
        return redirect('/login')
def user_list(request):
   if 'suname' in request.session:
            cursor=connection.cursor()
            cursor.execute("select  * from  tbl_user_register")
            data=cursor.fetchall()
            return render(request,'Master/user_list.html',{'data':data})
   else:
        return redirect('/login')
#product List


def save_category(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        tbl=category()
        tbl.category=request.POST.get("category")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_category/')
    else:
        return redirect('/login')
def add_category(request):
 if 'suname' in request.session:
    data=category.objects.all()
    return render(request,'Master/category.html',{'data':data})
 else:
      return redirect('/index/')
def edit_category(request,id):
 if 'suname' in request.session:
    data=category.objects.get(category_id=id)
    return render(request,'Master/edit_category.html',{'data':data})
 else:
      return redirect('/index/')


def update_category(request,id):
 if 'suname' in request.session:
    tbl=category.objects.get(category_id=id)
    tbl.category=request.POST.get("category")
    tbl.save()
    messages.add_message(request, messages.INFO, 'Updated successfully.')
    return redirect('/add_category/')
 else:
      return redirect('/index/')
def delete_category(request,id):
 if 'suname' in request.session:
    tbl=category.objects.get(category_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/add_category/')
 else:
      return redirect('/index/')
#product
def save_product(request):
    if 'suname' in request.session:
        tbl=product()

        tbl.category_id=request.POST.get("category")
        tbl.product=request.POST.get("product")
        tbl.quantity=request.POST.get("quantity")
        tbl.price=request.POST.get("price")
        tbl.description=request.POST.get("description")
        tbl.features=request.POST.get("features")
        tbl.painter_name=request.POST.get("painter_name")
        image=request.FILES['image']
        split_tup = os.path.splitext(image.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,image)
        url1=obj.url(file)
        tbl.image=url1

        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_product/')
    else:
        return redirect('/login')
def product_list(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data1=category.objects.all()
        cursor=connection.cursor()
        cursor.execute("select p.*,c.* from  tbl_product as p inner join   tbl_category as c on p.category_id =c.category_id")
        data=cursor.fetchall()

        return render(request,'Master/product_list.html',{'data':data,'data1':data1})
    else:
       return redirect('/login')
def add_product(request):
 if 'suname' in request.session:
    data=category.objects.all()
    return render(request,'Master/product.html',{'data':data})
 else:
      return redirect('/index/')
def edit_product(request,id):
 if 'suname' in request.session:
    logid=request.session['slogid']
    data1=category.objects.all()
    data=product.objects.get(product_id=id)
    return render(request,'Master/edit_product.html',{'data':data,'data1':data1})
 else:
      return redirect('/index/')
def update_product(request,id):
 if 'suname' in request.session:
        tbl=product.objects.get(product_id=id)
        if len(request.FILES) != 0:

            image=request.FILES['image']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,image)
            url1=obj.url(file)
            tbl.image=url1
        tbl.description=request.POST.get("description")
        tbl.features=request.POST.get("features")
        tbl.product=request.POST.get("product")
        tbl.quantity=request.POST.get("quantity")
        tbl.price=request.POST.get("price")
        tbl.painter_name=request.POST.get("painter_name")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/product_list')
 else:
      return redirect('/index/')
def delete_product(request,id):
 if 'suname' in request.session:
    tbl=product.objects.get(product_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/product_list')
 else:
      return redirect('/index/')

def save_notification(request):
    if 'suname' in request.session:
        tbl=notification()
        tbl.subject=request.POST.get("subject")
        tbl.description=request.POST.get("description")
        image=request.FILES['image']
        split_tup = os.path.splitext(image.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,image)
        url1=obj.url(file)
        tbl.image=url1

        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_notification')
    else:
        return redirect('/index/')
def notification_list(request):
    if 'suname' in request.session:

        data=notification.objects.all()
        return render(request,'Master/notification_list.html',{'data':data})
    else:
       return redirect('/login')
def add_notification(request):
 if 'suname' in request.session:
    return render(request,'Master/notification.html')
 else:
      return redirect('/index/')
def edit_notification(request,id):
 if 'suname' in request.session:
    data=notification.objects.get(notification_id=id)
    return render(request,'Master/edit_notification.html',{'data':data})
 else:
      return redirect('/index/')
def update_notification(request,id):
 if 'suname' in request.session:
        tbl=notification.objects.get(notification_id=id)
        if len(request.FILES) != 0:

            image=request.FILES['image']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,image)
            url1=obj.url(file)
            tbl.image=url1
        tbl.subject=request.POST.get("subject")
        tbl.description=request.POST.get("description")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/manage_notification')
 else:
      return redirect('/index/')
def delete_notification(request,id):
 if 'suname' in request.session:
    tbl=notification.objects.get(notification_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/manage_notification')
 else:
      return redirect('/index/')


     # ----------------Admin Complaint -------------
def view_complaints(request):
    if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_complaint  as c inner join  tbl_user_register as u  on c.user_login_id =u.login_id where c.reply='Nil'  order by c.complaint_id desc")
        data=cursor.fetchall()
        return render(request,'Master/view_complaints.html',{'data':data})
    else:
       return redirect('/login')
def replied_list(request):
    if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_complaint  as c inner join  tbl_user_register as u  on c.user_login_id =u.login_id where c.reply!='Nil' order by c.complaint_id desc")
        data=cursor.fetchall()
        return render(request,'Master/replied_complaints.html',{'data':data})
    else:
       return redirect('/login')
def adm_reply_complaint(request,id):
    if 'suname' in request.session:

        return render(request,'Master/reply_complaint.html',{'id':id})
    else:
       return redirect('/login')
def add_reply(request,id):
    tbl=complaint.objects.get(complaint_id=id)
    tbl.reply=request.POST.get("reply")
    tbl.save()
    return redirect('/replied_list')

def Complaint_frm(request):
    if 'suname' in request.session:

        return render(request,'Customer/complaint.html')
    else:
       return redirect('/index/')
def save_complaint(request):
    if 'suname' in request.session:
        tbl=complaint()
        tbl.user_login_id=request.session['slogid']
        tbl.complaint_subject=request.POST.get("subject")
        tbl.complaint=request.POST.get("complaint")
        tbl.reply="Nil"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/Complaint')
    else:
       return redirect('/index/')
def Complaint_list(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        data1 = complaint.objects.filter(user_login_id=id)
        return render(request,'Customer/Complaint_list.html',{'data1':data1})
     else:
       return redirect('/index/')
def delete_complaint(request,id):
    if 'suname' in request.session:
        tbl=complaint.objects.get(complaint_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/Complaint_list')
    else:
       return redirect('/index/')


#...........................
def display_product(request):
        category_id = request.GET.get("category_id")
        str1="<table class='table table-striped table-bordered'><thead><th>Id</th><th>Painting Name</th><th>Painter </th><th>Quanitity</th><th>Image</th><th>Price</th><th>Details</th><th>Category</th><th>#</th></thead>"
        cursor=connection.cursor()
        cursor.execute("select p.*,c.* from  tbl_product as p inner join   tbl_category as c on p.category_id =c.category_id  where p.category_id="+str(category_id))
        data=cursor.fetchall()
        count=1
        for i in data:
          str1+="<tr><td>"+str(count)+"</td><td>"+str(i[2])+"</td><td>"+str(i[8])+"</td><td>"+str(i[3])+"</td><td><img src="+str(i[5])+" width='100' height='80'></td><td>"+str(i[4])+" <td><div><b>Description</b>"+str(i[7])+"</div><div><b>Features</b>"+str(i[6])+"</div></td><td>"+str(i[11])+"</td><td><a href='/edit_product/"+str(i[0])+"' class='btn btn-info'>Edit</a></td>  <td><a href='/delete_product/"+str(i[0])+"' onclick='return ConfirmDialog();' class='btn btn-danger'>Delete</a></td></tr>"
          count=count+1
        return HttpResponse(str1)
def checkout(request):
     if 'suname' in request.session:
        logid=request.session['slogid']

        check_no1=random.randint(100,999999)
        for i in range(1,20):
            if(request.POST.get("item_id_"+str(i))):

                item_id=request.POST.get("item_id_"+str(i))
                tbl=product.objects.get(product_id=item_id)
                item_image=tbl.image
                item_name=tbl.product
                amount=request.POST.get("amount_"+str(i))
                quantity=request.POST.get("quantity_"+str(i))

                obj=order()
                obj.product_id=item_id
                obj.amount=int(amount)*int(quantity)
                obj.quantity=quantity
                obj.status='Not Paid'
                obj.user_login_id=logid
                obj.check_no_order=check_no1
                obj.save()

            #    // list=[item_name,quantity,amount,item_image,i,item_id]


        cursor=connection.cursor()
        cursor.execute("select p.*,c.* from  tbl_order as p inner join   tbl_product as c on p.product_id =c.product_id  where p.check_no_order="+str(check_no1))
        data=cursor.fetchall()
        return render(request,'Customer/checkout.html',{'data':data,'check_no1':check_no1})
     else:
      return redirect('/index/')
def add_qty(request):
    oid=request.GET.get("oid")
    newqty=request.GET.get("newqty")
    order.objects.filter(order_id=oid).update(quantity=newqty)
    data=[]
    try:

        cursor=connection.cursor()
        cursor.execute("select p.price from  tbl_order as o inner join   tbl_product as p on p.product_id =o.product_id  where o.order_id="+str(oid))
        data2=cursor.fetchall()

        for i in data2:
            nprice=int(i[0])*int(newqty)
            order.objects.filter(order_id=oid).update(amount=nprice)
            data1 = {
            'price':nprice
                    }
    except Exception:
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(data1)
def sub_qty(request):
    oid=request.GET.get("oid")
    newqty=request.GET.get("newqty")
    order.objects.filter(order_id=oid).update(quantity=newqty)
    data=[]
    try:

        cursor=connection.cursor()
        cursor.execute("select p.price from  tbl_order as o inner join   tbl_product as p on p.product_id =o.product_id  where o.order_id="+str(oid))
        data2=cursor.fetchall()

        for i in data2:
            nprice=int(i[0])*int(newqty)
            order.objects.filter(order_id=oid).update(amount=nprice)
            data1 = {
            'price':nprice
                    }
    except Exception:
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(data1)
def remove_order(request):
    if 'suname' in request.session:
        oid=request.GET.get("oid")
        tbl=order.objects.get(order_id=oid)
        tbl.delete()

def order_list(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.product,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.Address  from  tbl_order as o inner join   tbl_product as p on p.product_id =o.product_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_user_register as u  on o.user_login_id=u.login_id where status='Paid' order by  o.entry_date")
        data=cursor.fetchall()
        return render(request,'Master/order.html',{'data':data})
    else:
      return redirect('/index/')
def deliver(request,id):
    if 'suname' in request.session:
        tbl=order.objects.get(order_id=id)
        tbl.status="Delivered"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Delivered successfully.')
        return redirect('/order_list/')
    else:
       return redirect('/index/')
def deliverd_list(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.product,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.Address  from  tbl_order as o inner join   tbl_product as p on p.product_id =o.product_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_user_register as u  on o.user_login_id=u.login_id where  status='Delivered' order by  o.entry_date")
        data=cursor.fetchall()
        return render(request,'Master/deliverd_list.html',{'data':data})
    else:
      return redirect('/index/')
def cust_events(request):
    if 'suname' in request.session:

        data=notification.objects.all()
        return render(request,'Customer/events.html',{'data':data})
    else:
       return redirect('/login')
def payment(request,id):
    if 'suname' in request.session:
        data=order.objects.filter(check_no_order=id)
        sum=0
        for i in data:
            sum+=i.amount


        return render(request,'Customer/payment.html',{'sum':sum,'check_no1':id})
    else:
       return redirect('/index/')
def pay_action(request):
    if 'suname' in request.session:
        id=request.POST.get("cno")
        order.objects.filter(check_no_order=id).update(status="Paid")

        cursor=connection.cursor()
        cursor.execute("select o.quantity as oqty,p.quantity as pqty,p.product_id from  tbl_order as o inner join   tbl_product as p on p.product_id =o.product_id  where o.check_no_order="+str(id))
        data=cursor.fetchall()
        newqty=0
        for i in data:
            newqty=int(i[1])-int(i[0])
            pid=i[2]
            product.objects.filter(product_id=pid).update(quantity=newqty)

        return redirect('/clear_cart/')
    else:
       return redirect('/index/')

def myorder(request):
    if 'suname' in request.session:
        logid= request.session['slogid']

        cursor=connection.cursor()
        cursor.execute("select o.*,p.product,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.address,p.painter_name from  tbl_order as o inner join   tbl_product as p on p.product_id =o.product_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_user_register as u  on o.user_login_id=u.login_id  where o.status!='Not Paid'  and o.user_login_id="+str(logid)+" order by  o.entry_date")
        data=cursor.fetchall()
        return render(request,'Customer/myorder.html',{'data':data})

    else:
       return redirect('/index/')
def clear_cart(request):
    if 'suname' in request.session:

        return render(request,'Customer/clear_cart.html')
    else:
       return redirect('/index/')

def cust_product(request):
    if 'suname' in request.session:
        shop_login_id=request.POST.get("shop")
        category_id=request.POST.get("category")
        data=product.objects.filter(shop_login_id=shop_login_id,category_id=category_id)
        return render(request,'Customer/product.html',{'data':data})
    else:
       return redirect('/index/')
def single(request,id):
    if 'suname' in request.session:

        data=product.objects.get(product_id=id)
        return render(request,'Customer/single.html',{'data':data})
    else:
       return redirect('/index/')

def Feedback(request):
    if 'suname' in request.session:
        data=state.objects.all()

        return render(request,'Customer/feedback.html',{'data':data})
    else:
       return redirect('/index/')
def save_feedback(request):
    if 'suname' in request.session:
        tbl=feedback()
        tbl.user_login_id=request.session['slogid']
        tbl.feedback_subject=request.POST.get("subject")
        tbl.feedback=request.POST.get("feedback")

        tbl.reply="Nil"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/Feedback')
    else:
       return redirect('/index/')
def Feedback_list(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select f.* from tbl_feedback as f  where f.user_login_id="+str(id))
        data=cursor.fetchall()

        return render(request,'Customer/feedbacklist.html',{'data1':data})
    else:
       return redirect('/login')

def view_feedback(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_feedback  as c inner join  tbl_user_register as u  on c.user_login_id =u.login_id where c.reply='Nil' order by c.feedback_id desc")
        data=cursor.fetchall()
        return render(request,'Master/view_feedback.html',{'data':data})
    else:
       return redirect('/login')
def view_replied_feedback(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_feedback  as c inner join  tbl_user_register as u  on c.user_login_id =u.login_id where c.reply!='Nil' order by c.feedback_id desc")
        data=cursor.fetchall()
        return render(request,'Master/replied_feedback.html',{'data':data})
    else:
       return redirect('/login')
def adm_reply_feedback(request,id):
    if 'suname' in request.session:

        return render(request,'Master/reply_feedback.html',{'id':id})
    else:
       return redirect('/login')
def add_feedback_reply(request,id):
    tbl=feedback.objects.get(feedback_id=id)
    tbl.reply=request.POST.get("reply")
    tbl.save()
    return redirect('/view_replied_feedback')



def save_raw_materials(request):
    if 'suname' in request.session:
        tbl=raw_materials()
        tbl.raw_materials=request.POST.get("raw_materials")
        tbl.description=request.POST.get("description")
        tbl.price=request.POST.get("price")
        tbl.quantity=request.POST.get("quantity")
        image=request.FILES['image']
        split_tup = os.path.splitext(image.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,image)
        url1=obj.url(file)
        tbl.image=url1

        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_raw_materials')
    else:
        return redirect('/index/')
def raw_materials_list(request):
    if 'suname' in request.session:

        data=raw_materials.objects.all()
        return render(request,'Master/raw_materials_list.html',{'data':data})
    else:
       return redirect('/login')
def add_raw_materials(request):
 if 'suname' in request.session:
    return render(request,'Master/raw_materials.html')
 else:
      return redirect('/index/')
def edit_raw_materials(request,id):
 if 'suname' in request.session:
    data=raw_materials.objects.get(raw_materials_id=id)
    return render(request,'Master/edit_raw_materials.html',{'data':data})
 else:
      return redirect('/index/')
def update_raw_materials(request,id):
 if 'suname' in request.session:
        tbl=raw_materials.objects.get(raw_materials_id=id)
        if len(request.FILES) != 0:

            image=request.FILES['image']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,image)
            url1=obj.url(file)
            tbl.image=url1
        tbl.raw_materials=request.POST.get("raw_materials")
        tbl.description=request.POST.get("description")
        tbl.price=request.POST.get("price")
        tbl.quantity=request.POST.get("quantity")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/manage_raw_materials')
 else:
      return redirect('/index/')
def delete_raw_materials(request,id):
 if 'suname' in request.session:
    tbl=raw_materials.objects.get(raw_materials_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/manage_raw_materials')
 else:
      return redirect('/index/')


 #Artist Work

def save_upload_work(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        tbl=artist_work()
        tbl.artist_work=request.POST.get("artist_work")
        tbl.description=request.POST.get("description")
        tbl.price=request.POST.get("price")
        tbl.quantity=request.POST.get("quantity")
        tbl.artist_login_id=logid
        image=request.FILES['image']
        split_tup = os.path.splitext(image.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,image)
        url1=obj.url(file)
        tbl.image=url1

        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/upload_work')
    else:
        return redirect('/index/')
def uploaded_work_list(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        data=artist_work.objects.filter(artist_login_id=logid)
        return render(request,'Artist/upload_work_list.html',{'data':data})
    else:
       return redirect('/login')
def upload_work(request):
 if 'suname' in request.session:
    return render(request,'Artist/upload_work.html')
 else:
      return redirect('/index/')
def edit_upload_work(request,id):
 if 'suname' in request.session:
    data=artist_work.objects.get(artist_work_id=id)
    return render(request,'Artist/edit_upload_work.html',{'data':data})
 else:
      return redirect('/index/')
def update_upload_work(request,id):
 if 'suname' in request.session:
        tbl=artist_work.objects.get(artist_work_id=id)
        if len(request.FILES) != 0:
            image=request.FILES['image']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,image)
            url1=obj.url(file)
            tbl.image=url1

        tbl.artist_work=request.POST.get("artist_work")
        tbl.description=request.POST.get("description")
        tbl.price=request.POST.get("price")
        tbl.quantity=request.POST.get("quantity")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/manage_upload_work')
 else:
      return redirect('/index/')
def delete_upload_work(request,id):
 if 'suname' in request.session:
    tbl=artist_work.objects.get(artist_work_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/manage_upload_work')
 else:
      return redirect('/index/')
def view_raw_materials(request):
    if 'suname' in request.session:

        data=raw_materials.objects.filter(quantity__gte=1)
        return render(request,'Artist/view_raw_materials.html',{'data':data})
    else:
       return redirect('/login')

def Buy_raw_materials(request,id):
    if 'suname' in request.session:
        data=raw_materials.objects.get(raw_materials_id=id)
        return render(request,'Artist/raw_materials_buy_now.html',{'data':data})
    else:
      return redirect('/index/')


def payment_raw_matierial(request,id):
    if 'suname' in request.session:

        quantity=request.POST.get("quantity")
        total=request.POST.get("tot_amount")
        raw_materials_id=id

        return render(request,'Artist/raw_material_payment.html',{'id':raw_materials_id,'quantity':quantity,'total':total})
    else:
      return redirect('/index/')

def payment_action_raw_matierial(request):
    if 'suname' in request.session:

        obj=order_raw_materials()
        obj.raw_materials_id=request.POST.get("product_id")
        obj.amount=request.POST.get("amount")
        obj.quantity=request.POST.get("quantity")
        obj.artist_login_id=request.session['slogid']
        obj.status="Paid"
        obj.save()
        raw_materials_id=request.POST.get("product_id")
        tbl=raw_materials.objects.get(raw_materials_id=raw_materials_id)
        oldqty=tbl.quantity
        newqty=request.POST.get("quantity")
        qty=int(oldqty)-int(newqty)
        tbl.quantity=qty
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/view_raw_materials/')
    else:
        return redirect('/index/')
def raw_materials_order_list(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.raw_materials,p.description,p.image from tbl_order_raw_materials as o inner join  tbl_raw_materials as p on p.raw_materials_id=o.raw_materials_id  where o.artist_login_id="+str(logid))
        data=cursor.fetchall()

        return render(request,'Artist/raw_materials_order_list.html',{'data':data})
    else:
       return redirect('/index/')

def adm_delivered_raw_materials(request):
    if 'suname' in request.session:

        cursor=connection.cursor()
        cursor.execute("select o.*,p.raw_materials,p.description,p.image,a.name,a.phone_number,a.Email,a.Address from tbl_order_raw_materials as o inner join  tbl_raw_materials as p on p.raw_materials_id=o.raw_materials_id inner join tbl_artist as a on o.artist_login_id=a.login_id  where o.status='Delivered'")
        data=cursor.fetchall()

        return render(request,'Master/adm_delivered_raw_materials.html',{'data':data})
    else:
       return redirect('/index/')
def deliver_raw_materials(request,id):
    if 'suname' in request.session:
        tbl=order_raw_materials.objects.get(raw_materials_order_id=id)
        tbl.status="Delivered"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Delivered successfully.')
        return redirect('/adm_order_raw_materials/')
    else:
       return redirect('/index/')
def adm_order_raw_materials(request):
    if 'suname' in request.session:

        cursor=connection.cursor()
        cursor.execute("select o.*,p.raw_materials,p.description,p.image,a.name,a.phone_number,a.Email,a.Address from tbl_order_raw_materials as o inner join  tbl_raw_materials as p on p.raw_materials_id=o.raw_materials_id inner join tbl_artist as a on o.artist_login_id=a.login_id  where o.status='Paid'")
        data=cursor.fetchall()

        return render(request,'Master/adm_raw_materials_order_list.html',{'data':data})
    else:
       return redirect('/index/')







def artist_work_list(request):
    if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_artist_work  as c inner join   tbl_artist as u  on c.artist_login_id =u.login_id")
        data=cursor.fetchall()
        return render(request,'Customer/artist_work_list.html',{'data':data})
    else:
       return redirect('/login')

def buy_artist_work(request,id):
    if 'suname' in request.session:
        data=artist_work.objects.get(artist_work_id=id)
        return render(request,'Customer/artist_work_buy_now.html',{'data':data})
    else:
      return redirect('/index/')


def payment_artist_work(request,id):
    if 'suname' in request.session:

        quantity=request.POST.get("quantity")
        total=request.POST.get("tot_amount")
        artist_work_id=id

        return render(request,'Customer/artist_work_payment.html',{'id':artist_work_id,'quantity':quantity,'total':total})
    else:
      return redirect('/index/')

def payment_action_artist_work(request):
    if 'suname' in request.session:

        obj=order_artist_work()
        obj.artist_work_id =request.POST.get("product_id")
        obj.amount=request.POST.get("amount")
        obj.quantity=request.POST.get("quantity")
        obj.user_login_id=request.session['slogid']
        obj.status="Paid"
        obj.save()
        artist_work_id=request.POST.get("product_id")
        tbl=artist_work.objects.get(artist_work_id=artist_work_id)
        oldqty=tbl.quantity
        newqty=request.POST.get("quantity")
        qty=int(oldqty)-int(newqty)
        tbl.quantity=qty
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/artist_work_list/')
    else:
        return redirect('/index/')


def artist_work_order_list(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.artist_work,p.description,p.image from tbl_order_artist_work as o inner join  tbl_artist_work as p on p.artist_work_id=o.artist_work_id  where o.user_login_id="+str(logid))
        data=cursor.fetchall()

        return render(request,'Customer/artist_work_order_list.html',{'data':data})
    else:
       return redirect('/index/')


def delivered_work_order(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.artist_work,p.description,p.image,a.name,a.phone_number,a.Email,a.Address from tbl_order_artist_work as o inner join  tbl_artist_work as p on p.artist_work_id=o.artist_work_id inner join tbl_user_register as a on o.user_login_id=a.login_id  where o.status='Delivered' and p.artist_login_id="+str(logid))
        data=cursor.fetchall()

        return render(request,'Artist/delivered_work_order.html',{'data':data})
    else:
       return redirect('/index/')
def deliver_work_order(request,id):
    if 'suname' in request.session:
        tbl=order_artist_work.objects.get(artist_order_id=id)
        tbl.status="Delivered"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Delivered successfully.')
        return redirect('/work_order/')
    else:
       return redirect('/index/')
def work_order(request):
    if 'suname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.artist_work,p.description,p.image,a.name,a.phone_number,a.Email,a.Address from tbl_order_artist_work as o inner join  tbl_artist_work as p on p.artist_work_id=o.artist_work_id inner join tbl_user_register as a on o.user_login_id=a.login_id  where o.status='Paid' and p.artist_login_id="+str(logid))
        data=cursor.fetchall()

        return render(request,'Artist/work_order.html',{'data':data})
    else:
       return redirect('/index/')

def artist_work_comment(request,id):
    if 'suname' in request.session:

        cursor=connection.cursor()
        sql="select c.*,u.* from  tbl_work_comment  as c inner join   tbl_user_register as u  on c.user_login_id =u.login_id where c.artist_work_id="+str(id)
        cursor.execute(sql)
        data=cursor.fetchall()

        return render(request,'Customer/comments.html',{'id':id,'data':data})
    else:
       return redirect('/login')
def save_comments(request,id):
    if 'suname' in request.session:

        obj=work_comment()
        obj.artist_work_id =id
        obj.comment=request.POST.get("comment")

        obj.user_login_id=request.session['slogid']
        obj.status="Paid"
        obj.save()

        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/artist_work_comment/'+str(id))
    else:
        return redirect('/index/')

def comment_list(request,id):
    if 'suname' in request.session:

        cursor=connection.cursor()
        sql="select c.*,u.* from  tbl_work_comment  as c inner join   tbl_user_register as u  on c.user_login_id =u.login_id where c.artist_work_id="+str(id)
        cursor.execute(sql)
        data=cursor.fetchall()

        return render(request,'Artist/comments.html',{'id':id,'data':data})
    else:
       return redirect('/login')


def raw_materials_list_user(request):
    if 'suname' in request.session:

        data=raw_materials.objects.all()

        return render(request,'Customer/raw_materials_list_user.html',{'data':data})
    else:
       return redirect('/login')


